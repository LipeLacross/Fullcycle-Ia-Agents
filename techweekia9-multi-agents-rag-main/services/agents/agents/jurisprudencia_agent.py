from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from app.config import CLAUDE_MODEL
from tools.search_similar import search_similar

jurisprudencia_agent = Agent(
    name="agente_jurisprudencia",
    model=LiteLlm(model=CLAUDE_MODEL),
    description="Busca jurisprudência e casos similares em OUTROS processos da base.",
    instruction="""Você é um especialista em jurisprudência.
Processo atual: {current_process_name?}

Busque casos SIMILARES ao processo atual na base de dados.
Para cada caso encontrado, destaque: nome, similaridade, decisão do juiz, e pontos de precedente.
Se não encontrar, informe claramente. Responda em português brasileiro.""",
    tools=[search_similar],
    output_key="jurisprudencia_results",
)
