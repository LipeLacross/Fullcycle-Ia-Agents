BUGGY_CODE = """
def aplicar_desconto(preco, desconto):
    preco_final = preco - (preco * desconto / 100)
    return preco_final
""".strip()

# ─── 1. Prompt Simples (sem estrutura) ───
SIMPLE_PROMPT = "Revise esse código." # ZERO SHOT

# ─── 2. Chain of Thought ───
COT_PROMPT = """Faça um code review dessa função Python.

Antes de dar sua resposta final, pense passo a passo e mostre todo o seu raciocínio."""

# ─── 3. Tree of Thought (ToT) ───
# Fase 1: gerar N pensamentos candidatos (branches)
TOT_GENERATE_PROMPT = """Você é um code reviewer analisando essa função Python:

```python
{code}
```

{context}

Proponha {k} linhas de investigação DIFERENTES e INDEPENDENTES para o code review.
Cada uma deve focar em um aspecto distinto (ex: validação, edge cases, tipos, lógica, performance).

Responda APENAS com a lista numerada. Cada item deve ser uma frase curta descrevendo o que investigar.
"""

# Fase 2: avaliar cada pensamento candidato
TOT_EVALUATE_PROMPT = """Você é um avaliador de code review. Analise a seguinte linha de investigação para a função:

```python
{code}
```

Linha de investigação: **{thought}**

Essa linha de investigação vai encontrar bugs reais ou problemas significativos nessa função?

Responda com APENAS uma palavra: sure / maybe / impossible"""

# Fase 3: expandir o pensamento selecionado
TOT_EXPAND_PROMPT = """Você é um code reviewer analisando essa função Python:

```python
{code}
```

Sua linha de investigação: **{thought}**

Análise anterior:
{previous}

Agora aprofunde APENAS essa linha de investigação. Mostre:
- O cenário concreto que causa o problema (com valores)
- O que acontece quando esse cenário ocorre
- Como corrigir

Seja direto, máximo 5 linhas."""

# ─── 4. ReAct (Reasoning + Acting) ───
# - Labels explícitos: Thought / Action / Observation
# - O modelo decide sozinho quando agir e quando parar (Finish)
# - Few-shot example demonstra o formato esperado
REACT_SYSTEM_PROMPT = """Você é um code reviewer. Você tem acesso a uma ferramenta que executa código Python de verdade.

A função aplicar_desconto já está carregada no ambiente. Você NÃO precisa redefini-la. Basta chamá-la diretamente com print(), exemplo: print(aplicar_desconto(100, 10))

Teste inclusive o que acontece ao passar tipos errados, como print(aplicar_desconto("abc", 10)).

Siga o padrão ReAct. O ciclo funciona assim:

1. Você escreve um **Thought** explicando o que vai testar e por quê
2. Você chama a ferramenta (Action) — o sistema executa e devolve o resultado (Observation)
3. Você escreve outro **Thought** analisando o resultado: é um bug? O que significa?
4. Repita até cobrir os cenários que julgar necessários
5. Escreva um **Thought** final resumindo tudo e apresente os bugs e o código corrigido

IMPORTANTE:
- Sempre use print() para ver o resultado da execução
- Sempre escreva um **Thought** ANTES de cada chamada de ferramenta
- Sempre escreva um **Thought** DEPOIS de receber cada resultado
- Você decide quais cenários testar e quando parar

Comece raciocinando sobre a função e decida o que testar primeiro."""

REACT_TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "executar_codigo",
            "description": "Executa código Python e retorna o resultado ou erro. Use para testar a função com diferentes valores.",
            "parameters": {
                "type": "object",
                "properties": {
                    "codigo": {
                        "type": "string",
                        "description": "Código Python para executar. A função aplicar_desconto já está disponível no escopo.",
                    }
                },
                "required": ["codigo"],
            },
        },
    }
]

# ═══════════════════════════════════════════════════════════════════════════════
# EXEMPLO 2 — Pegadinha Lógica (Strawberry)
# ═══════════════════════════════════════════════════════════════════════════════

LOGIC_QUESTION = "Quantas vezes a letra 'r' aparece na palavra 'strawberry'?"

# ─── 1. Prompt Simples (sem técnica) ───
LOGIC_SIMPLE_PROMPT = "Responda a pergunta do usuário."

# ─── 2. Chain of Thought ───
LOGIC_COT_PROMPT = """Responda a pergunta do usuário.

Antes de dar sua resposta final, percorra a palavra letra por letra, listando cada uma com seu número de posição. Depois conte apenas as letras alvo. Mostre todo o seu trabalho."""

# ─── 3. Tree of Thought ───
LOGIC_TOT_GENERATE_PROMPT = """Analise esta pergunta:

"{question}"

{context}

Proponha {k} abordagens DIFERENTES e INDEPENDENTES para resolver.
Cada uma deve usar um método diferente (ex: soletrar cada letra, dividir em sílabas, usar uma técnica de contagem diferente).

Responda APENAS com a lista numerada. Cada item deve ser uma frase curta descrevendo a abordagem."""

LOGIC_TOT_EVALUATE_PROMPT = """Avalie a seguinte abordagem para a pergunta:

"{question}"

Abordagem: **{thought}**

Essa abordagem vai produzir a resposta correta de forma confiável?

Responda com APENAS uma palavra: sure / maybe / impossible"""

LOGIC_TOT_EXPAND_PROMPT = """Responda esta pergunta:

"{question}"

Sua abordagem: **{thought}**

Análise anterior:
{previous}

Agora execute APENAS esta abordagem em detalhe. Mostre:
- O trabalho completo passo a passo
- A contagem a que chegou
- Sua confiança no resultado

Seja completo mas conciso."""

# ─── 4. ReAct ───
# Mesmo padrão ReAct com labels explícitos.
LOGIC_REACT_SYSTEM_PROMPT = """Você é um analista cuidadoso. Você tem acesso a uma ferramenta que executa código Python para verificar suas respostas.

Siga o padrão ReAct. O ciclo funciona assim:

1. Você escreve um **Thought** explicando o que vai verificar e por quê
2. Você chama a ferramenta (Action) — o sistema executa e devolve o resultado (Observation)
3. Você escreve outro **Thought** analisando o resultado: o que confirma ou refuta?
4. Repita até ter confiança na resposta
5. Escreva um **Thought** final resumindo tudo e apresente sua resposta verificada

IMPORTANTE:
- Sempre use print() para ver o resultado da execução
- Sempre escreva um **Thought** ANTES de cada chamada de ferramenta
- Sempre escreva um **Thought** DEPOIS de receber cada resultado
- NÃO confie na sua própria contagem — sempre verifique com código
- Você decide o que verificar e quando parar

Comece raciocinando sobre a pergunta e decida o que verificar primeiro."""

LOGIC_REACT_TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "executar_codigo",
            "description": "Executa código Python e retorna o resultado. Use para verificar contagem de letras programaticamente.",
            "parameters": {
                "type": "object",
                "properties": {
                    "codigo": {
                        "type": "string",
                        "description": "Código Python para executar. Use print() para ver o resultado.",
                    }
                },
                "required": ["codigo"],
            },
        },
    }
]
