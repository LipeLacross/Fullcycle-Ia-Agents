from google.adk.tools import ToolContext
from app import db


def get_process_context(tool_context: ToolContext) -> dict:
    """Get the full context of the current legal process including metadata and sentence.

    Returns:
        dict with process name, parties, case_type, status, and sentence_summary
    """
    process_id = tool_context.state.get("current_process_id")
    if not process_id:
        return {"error": "Nenhum processo selecionado."}

    process = db.get_process(process_id)
    if not process:
        return {"error": "Processo não encontrado."}

    return process
