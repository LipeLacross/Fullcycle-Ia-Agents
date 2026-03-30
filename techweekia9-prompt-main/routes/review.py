from fastapi import APIRouter
from pydantic import BaseModel

from llm import call_llm, client, MODEL
from techniques import execute_code, run_tot, run_react
from prompts import (
    BUGGY_CODE,
    SIMPLE_PROMPT,
    COT_PROMPT,
    TOT_GENERATE_PROMPT,
    TOT_EVALUATE_PROMPT,
    TOT_EXPAND_PROMPT,
    REACT_SYSTEM_PROMPT,
    REACT_TOOLS,
)

router = APIRouter(prefix="/api/review", tags=["Code Review"])


class ReviewResponse(BaseModel):
    technique: str
    response: str


@router.post("/simple")
def review_simple() -> ReviewResponse:
    completion = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SIMPLE_PROMPT},
            {"role": "user", "content": f"```python\n{BUGGY_CODE}\n```"},
        ],
        temperature=1.0,
    )
    return ReviewResponse(
        technique="Prompt Simples",
        response=completion.choices[0].message.content,
    )


@router.post("/cot")
def review_cot() -> ReviewResponse:
    return ReviewResponse(
        technique="Chain of Thought",
        response=call_llm(COT_PROMPT, f"```python\n{BUGGY_CODE}\n```"),
    )


@router.post("/tot")
def review_tot() -> ReviewResponse:
    result = run_tot(
        generate_prompt=TOT_GENERATE_PROMPT.format(
            code=BUGGY_CODE, context="Este é o início da análise.", k=3,
        ),
        evaluate_prompt=TOT_EVALUATE_PROMPT.replace("{code}", BUGGY_CODE),
        expand_prompt=TOT_EXPAND_PROMPT.replace("{code}", BUGGY_CODE),
        user_content="Liste as linhas de investigação.",
        conclusion_system=(
            "Você é um code reviewer. Com base nas análises abaixo, "
            "dê a conclusão final do code review com todos os bugs "
            "encontrados e o código corrigido.\n\nAnálises:\n{context}"
        ),
        conclusion_user=f"```python\n{BUGGY_CODE}\n```",
        depth=2,
    )
    return ReviewResponse(technique="Tree of Thought", response=result)


@router.post("/react")
def review_react() -> ReviewResponse:
    result = run_react(
        system_prompt=REACT_SYSTEM_PROMPT,
        user_message=f"Faça code review dessa função:\n\n```python\n{BUGGY_CODE}\n```",
        tools=REACT_TOOLS,
        execute_fn=lambda code: execute_code(code, preload=BUGGY_CODE),
    )
    return ReviewResponse(technique="ReAct", response=result)
