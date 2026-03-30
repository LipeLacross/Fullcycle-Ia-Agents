from google.adk.tools import ToolContext
from ingestion.embeddings import generate_embedding
from app import db


def search_process(query: str, tool_context: ToolContext) -> dict:
    """Search for relevant information within a specific legal process.
    Use this when the user asks about details of the current process.

    Args:
        query: The search query in natural language

    Returns:
        dict with 'results' (list of relevant text chunks with section and page info)
    """
    process_id = tool_context.state.get("current_process_id")
    if not process_id:
        return {"error": "Nenhum processo selecionado.", "results": []}

    embedding = generate_embedding(query)
    results = db.search_chunks(embedding, process_id=process_id, limit=5)

    if not results:
        return {"results": [], "message": "Nenhum trecho relevante encontrado."}

    return {"results": results}
