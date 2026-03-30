from app import db


def list_processes() -> dict:
    """List all available legal processes in the database.
    Use this when the user wants to see the available processes or choose one to work with.

    Returns:
        dict with 'processes' (list of available processes with id, name, case_type and status)
    """
    processes = db.list_processes()

    if not processes:
        return {"processes": [], "message": "Nenhum processo encontrado na base de dados."}

    return {"processes": processes}
