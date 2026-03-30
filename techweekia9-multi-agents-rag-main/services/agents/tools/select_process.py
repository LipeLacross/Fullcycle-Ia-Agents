from google.adk.tools import ToolContext
from app import db


def select_process(process_id: str, tool_context: ToolContext) -> dict:
    """Select a legal process to work with, setting it as the current process in the session.
    Use this when the user wants to select or switch to a specific process.

    Args:
        process_id: The UUID of the process to select

    Returns:
        dict confirming the selected process or an error message
    """
    process = db.get_process(process_id)

    if not process:
        return {"error": f"Processo com id '{process_id}' não encontrado."}

    tool_context.state["current_process_id"] = process_id
    tool_context.state["current_process_name"] = process["name"]

    return {
        "message": f"Processo selecionado com sucesso.",
        "process_id": process_id,
        "process_name": process["name"],
        "case_type": process["case_type"],
        "status": process["status"],
    }
