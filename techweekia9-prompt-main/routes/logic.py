from fastapi import APIRouter
from pydantic import BaseModel

from llm import call_llm, client, MODEL
from techniques import execute_code, run_tot, run_react
from prompts import (
    LOGIC_QUESTION,
    LOGIC_SIMPLE_PROMPT,
    LOGIC_COT_PROMPT,
    LOGIC_TOT_GENERATE_PROMPT,
    LOGIC_TOT_EVALUATE_PROMPT,
    LOGIC_TOT_EXPAND_PROMPT,
    LOGIC_REACT_SYSTEM_PROMPT,
    LOGIC_REACT_TOOLS,
)

router = APIRouter(prefix="/api/logic", tags=["Logic"])


class ReviewResponse(BaseModel):
    technique: str
    response: str


@router.post("/simple")
def logic_simple() -> ReviewResponse:
    completion = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": LOGIC_SIMPLE_PROMPT},
            {"role": "user", "content": LOGIC_QUESTION},
        ],
        temperature=1.0,
    )
    return ReviewResponse(
        technique="Prompt Simples",
        response=completion.choices[0].message.content,
    )


@router.post("/cot")
def logic_cot() -> ReviewResponse:
    return ReviewResponse(
        technique="Chain of Thought",
        response=call_llm(LOGIC_COT_PROMPT, LOGIC_QUESTION),
    )


@router.post("/tot")
def logic_tot() -> ReviewResponse:
    result = run_tot(
        generate_prompt=LOGIC_TOT_GENERATE_PROMPT.format(
            question=LOGIC_QUESTION, context="Este é o início da análise.", k=3,
        ),
        evaluate_prompt=LOGIC_TOT_EVALUATE_PROMPT.replace("{question}", LOGIC_QUESTION),
        expand_prompt=LOGIC_TOT_EXPAND_PROMPT.replace("{question}", LOGIC_QUESTION),
        user_content="Liste as hipóteses.",
        conclusion_system=(
            "Com base nas análises abaixo, dê a resposta final para a pergunta: "
            f'"{LOGIC_QUESTION}"\n\nAnálises:\n{{context}}'
        ),
        conclusion_user="Qual a resposta correta?",
        k=3,
        b=2,
        depth=1,
    )
    return ReviewResponse(technique="Tree of Thought", response=result)


@router.post("/react")
def logic_react() -> ReviewResponse:
    result = run_react(
        system_prompt=LOGIC_REACT_SYSTEM_PROMPT,
        user_message=LOGIC_QUESTION,
        tools=LOGIC_REACT_TOOLS,
        execute_fn=lambda code: execute_code(code),
    )
    return ReviewResponse(technique="ReAct", response=result)
