import json
import logging
import psycopg2
import psycopg2.extras
from app.config import DATABASE_URL

logger = logging.getLogger(__name__)

psycopg2.extras.register_uuid()


def get_connection():
    return psycopg2.connect(DATABASE_URL)


def search_chunks(query_embedding: list[float], process_id: str | None, limit: int = 5) -> list[dict]:
    try:
        conn = get_connection()
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

        embedding_str = "[" + ",".join(str(v) for v in query_embedding) + "]"


        if process_id:
            cur.execute(
                """SELECT content, section, page_number, process_id::text,
                          1 - (embedding <=> %s::vector) as similarity
                   FROM process_chunks
                   WHERE process_id = %s
                   ORDER BY embedding <=> %s::vector
                   LIMIT %s""",
                (embedding_str, process_id, embedding_str, limit),
            )
        else:
            cur.execute(
                """SELECT content, section, page_number, process_id::text,
                          1 - (embedding <=> %s::vector) as similarity
                   FROM process_chunks
                   ORDER BY embedding <=> %s::vector
                   LIMIT %s""",
                (embedding_str, embedding_str, limit),
            )

        results = [dict(row) for row in cur.fetchall()]
        cur.close()
        conn.close()
        return results
    except Exception as e:
        logger.error(f"Error searching chunks: {e}")
        return []


def get_process(process_id: str) -> dict | None:
    try:
        conn = get_connection()
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute(
            """SELECT id::text, name, case_type, parties, status, sentence_summary, created_at
               FROM processes WHERE id = %s""",
            (process_id,),
        )
        row = cur.fetchone()
        cur.close()
        conn.close()
        if row:
            result = dict(row)
            if isinstance(result.get("parties"), str):
                result["parties"] = json.loads(result["parties"])
            if result.get("created_at"):
                result["created_at"] = result["created_at"].isoformat()
            return result
        return None
    except Exception as e:
        logger.error(f"Error getting process: {e}")
        return None


def list_processes() -> list[dict]:
    try:
        conn = get_connection()
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute(
            """SELECT id::text, name, case_type, status
               FROM processes ORDER BY created_at"""
        )
        results = [dict(row) for row in cur.fetchall()]
        cur.close()
        conn.close()
        return results
    except Exception as e:
        logger.error(f"Error listing processes: {e}")
        return []
