from google.adk.tools import ToolContext
from ingestion.embeddings import generate_embedding
from app import db


def search_similar(query: str, tool_context: ToolContext) -> dict:
    """Search across ALL legal processes in the database for similar cases and jurisprudence.
    Use this to find precedents, similar decisions, or related cases.

    Args:
        query: The search query describing the legal issue or situation

    Returns:
        dict with 'results' (list of relevant chunks from OTHER processes, including process name and case info)
    """
    exclude_process_id = tool_context.state.get("current_process_id")

    embedding = generate_embedding(query)
    results = db.search_chunks(embedding, process_id=None, limit=5)

    # Filter out chunks from current process
    if exclude_process_id:
        results = [r for r in results if r.get("process_id") != exclude_process_id]

    if not results:
        return {"results": [], "message": "Nenhum caso similar encontrado."}

    # Truncate each chunk content to ~150 words to save tokens
    for r in results:
        words = r.get("content", "").split()
        if len(words) > 150:
            r["content"] = " ".join(words[:150]) + "..."

    # Enrich with process metadata
    for r in results:
        process = db.get_process(r["process_id"])
        if process:
            r["process_name"] = process["name"]
            r["case_type"] = process["case_type"]
            r["parties"] = process["parties"]

    return {"results": results}
