from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from app.config import CLAUDE_MODEL
from tools.get_process_context import get_process_context
from tools.search_process import search_process
from tools.search_similar import search_similar

analise_agent = Agent(
    name="agente_analise",
    model=LiteLlm(model=CLAUDE_MODEL),
    description="Analisa a sentença do processo atual e gera linha de ação estratégica.",
    instruction="""Você é um analista jurídico sênior.
Processo atual: {current_process_name?}
Pesquisa do processo já realizada: {pesquisa_results?}
Precedentes encontrados anteriormente: {jurisprudencia_results?}

Use os resultados de pesquisa e precedentes acima como base principal — evite buscas duplicadas.
Se alguma informação estiver ausente, use as ferramentas disponíveis para complementar.
Gere uma linha de ação incluindo:
1. Resumo da situação atual
2. Análise da sentença (pontos fortes e fracos)
3. Próximos passos recomendados
4. Fundamentação em precedentes (se disponíveis)
Responda em português brasileiro.""",
    tools=[get_process_context, search_process, search_similar],
)
