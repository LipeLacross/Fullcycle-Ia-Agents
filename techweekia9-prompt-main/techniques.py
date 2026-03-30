import json
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

from llm import call_llm, client, MODEL


# ─── Execução de código ──────────────────────────────────────────────────────

def execute_code(code: str, preload: str = "") -> str:
    """Executa código Python e retorna o output ou erro."""
    full_code = f"{preload}\n{code}" if preload else code
    result = subprocess.run(
        [sys.executable, "-c", full_code],
        capture_output=True, text=True, timeout=5,
    )
    output = result.stdout.strip() or result.stderr.strip()
    return output if output else "Código executou sem output. Use print() para ver o resultado."


# ─── Tree of Thought (engine genérico) ───────────────────────────────────────

def run_tot(
    *,
    generate_prompt: str,
    evaluate_prompt: str,
    expand_prompt: str,
    user_content: str,
    conclusion_system: str,
    conclusion_user: str,
    k: int = 3,
    b: int = 2,
    depth: int = 2,
) -> str:
    """Executa o fluxo Tree of Thought: gerar -> avaliar -> expandir -> concluir."""
    trace = []
    score_map = {"sure": 3, "likely": 2, "maybe": 1, "impossible": 0}

    # Fase 1: Gerar candidatos
    trace.append("## Fase 1 — Gerar candidatos\n")
    raw = call_llm(generate_prompt, user_content)
    thoughts = re.findall(r"\d+\.\s*(.+)", raw)[:k]

    for i, t in enumerate(thoughts, 1):
        trace.append(f"- **Candidato {i}**: {t}")
    trace.append("")

    if not thoughts:
        return raw

    # Fase 2: Avaliar cada candidato
    trace.append("## Fase 2 — Avaliar candidatos\n")

    def evaluate(thought: str) -> tuple[str, int, str]:
        prompt = evaluate_prompt.format(thought=thought)
        rating = call_llm(prompt, "Avalie.").strip().lower()
        for word in rating.split():
            if word in score_map:
                return thought, score_map[word], word
        return thought, 1, rating

    with ThreadPoolExecutor(max_workers=k) as executor:
        scored = list(executor.map(evaluate, thoughts))

    scored.sort(key=lambda x: x[1], reverse=True)
    for thought, score, rating in scored:
        emoji = {"sure": "🟢", "likely": "🟡", "maybe": "🟠"}.get(rating, "🔴")
        trace.append(f"- {emoji} **{rating}** (score {score}): {thought}")

    # Fase 3: Selecionar top-b e expandir
    selected = scored[:b]
    trace.append(f"\n**Selecionados (top {b}):** " + ", ".join(t[0] for t in selected))
    trace.append("")

    frontier = [(t, "") for t, _, _ in selected]

    for d in range(depth):
        trace.append(f"## Profundidade {d + 1} — Expandir\n")
        new_frontier = []

        def expand(item: tuple[str, str]) -> tuple[str, str, str]:
            thought, prev = item
            prompt = expand_prompt.format(thought=thought, previous=prev or "(nenhuma)")
            expansion = call_llm(prompt, "Expanda.")
            return thought, expansion, prev

        with ThreadPoolExecutor(max_workers=len(frontier)) as executor:
            expansions = list(executor.map(expand, frontier))

        for thought, expansion, _ in expansions:
            trace.append(f"### {thought}\n{expansion}\n")
            new_frontier.append((thought, expansion))

        frontier = new_frontier

    # Fase 4: Conclusão
    trace.append("## Conclusão\n")
    context = "\n".join(f"- {t}: {detail}" for t, detail in frontier)
    conclusion = call_llm(
        conclusion_system.format(context=context),
        conclusion_user,
    )
    trace.append(conclusion)

    return "\n".join(trace)


# ─── ReAct loop (engine genérico) ────────────────────────────────────────────

def run_react(
    *,
    system_prompt: str,
    user_message: str,
    tools: list[dict],
    execute_fn,
    max_iterations: int = 10,
) -> str:
    """Executa o loop ReAct: Thought -> Action -> Observation.

    O modelo decide sozinho quando agir e quando parar (tool_choice="auto").
    """
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_message},
    ]

    trace_parts = []

    for _ in range(max_iterations):
        completion = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=tools,
            tool_choice="auto",
            temperature=0,
        )

        choice = completion.choices[0]
        messages.append(choice.message)

        # Thought — o raciocínio do modelo antes/depois de cada ação
        if choice.message.content:
            trace_parts.append(choice.message.content)

        # Sem tool calls = modelo decidiu parar (Finish)
        if not choice.message.tool_calls:
            break

        # Action + Observation
        for tool_call in choice.message.tool_calls:
            args = json.loads(tool_call.function.arguments)
            codigo = args["codigo"]

            result = execute_fn(codigo)

            # Limpa print() do display para mostrar só a chamada
            display_code = codigo.strip()
            if display_code.startswith("print(") and display_code.endswith(")"):
                display_code = display_code[6:-1]

            trace_parts.append(f"**Action**: `{display_code}`")
            trace_parts.append(f"**Observation**: `{result}`")

            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": result,
            })

    return "\n".join(trace_parts)
