from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools.agent_tool import AgentTool
from app.config import CLAUDE_MODEL
from agents.pesquisa_agent import pesquisa_agent
from agents.jurisprudencia_agent import jurisprudencia_agent
from agents.analise_agent import analise_agent
from tools.list_processes import list_processes
from tools.select_process import select_process

root_agent = Agent(
    name="orquestrador_juridico",
    model=LiteLlm(model=CLAUDE_MODEL),
    description="Orquestrador principal do sistema de análise jurídica.",
    instruction="""Você coordena um sistema de análise jurídica.
Processo atual: {current_process_name?}

- Para listar processos disponíveis, use list_processes.
- Para selecionar um processo, use select_process com o process_id escolhido.
- Para perguntas sobre detalhes do processo atual, use agente_pesquisa.
- Para buscar casos similares em outros processos, use agente_jurisprudencia.
- Para gerar plano de ação estratégico, use agente_analise.
- Para análise completa, chame os três agentes em sequência: pesquisa → jurisprudencia → analise.
- Para perguntas gerais ou saudações, responda diretamente.
Responda em português brasileiro.""",
    tools=[
        list_processes,
        select_process,
        AgentTool(agent=pesquisa_agent),
        AgentTool(agent=jurisprudencia_agent),
        AgentTool(agent=analise_agent),
    ],
    #sub_agents=[pesquisa_agent, jurisprudencia_agent, analise_agent],
    # Modo sub_agents (transfer): orquestrador perde o controle após delegar.
    # Só transfere para um agente por vez — não encadeia automaticamente.
    # Vantagem: menor latência e custo para perguntas simples.
    # sub_agents=[pesquisa_agent, jurisprudencia_agent, analise_agent],
)
