from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from app.config import CLAUDE_MODEL
from tools.search_process import search_process

pesquisa_agent = Agent(
    name="agente_pesquisa",
    model=LiteLlm(model=CLAUDE_MODEL),
    description="Busca informações e trechos dentro do processo atual selecionado.",
    instruction="""Você é um pesquisador jurídico especializado.
Processo atual: {current_process_name?}

Sua função é buscar informações relevantes DENTRO do processo atual.
Use a ferramenta search_process para buscar. O process_id já é injetado automaticamente.
Responda SOMENTE com base nos trechos encontrados.
Cite a seção e página de onde veio cada informação.
Se não encontrar informação relevante, diga claramente.
Responda em português brasileiro.""",
    tools=[search_process],
    output_key="pesquisa_results",
)
