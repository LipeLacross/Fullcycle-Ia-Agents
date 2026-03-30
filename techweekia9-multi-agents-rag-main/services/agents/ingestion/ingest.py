import json
import logging
from app.config import DATABASE_URL
from ingestion.mock_data import generate_mock_data
from ingestion.embeddings import generate_embedding
import psycopg2

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def ingest_mock_data() -> str:
    """Ingest mock legal processes into the database. Idempotent: truncates tables first."""
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()

    # Truncate for idempotency
    cur.execute("TRUNCATE process_chunks CASCADE")
    cur.execute("TRUNCATE processes CASCADE")
    conn.commit()
    logger.info("Tables truncated.")

    data = generate_mock_data()
    total_chunks = 0

    for process in data["processes"]:
        # Insert process
        cur.execute(
            """INSERT INTO processes (name, case_type, parties, status, sentence_summary)
               VALUES (%s, %s, %s, %s, %s)
               RETURNING id""",
            (
                process["name"],
                process["case_type"],
                json.dumps(process["parties"]),
                process["status"],
                process["sentence_summary"],
            ),
        )
        process_id = cur.fetchone()[0]
        conn.commit()

        chunk_count = 0
        for chunk in process["chunks"]:
            logger.info(f"  Generating embedding for chunk {chunk_count + 1} ({chunk['section']}, p.{chunk['page_number']})...")
            embedding = generate_embedding(chunk["content"])

            embedding_str = "[" + ",".join(str(v) for v in embedding) + "]"
            cur.execute(
                """INSERT INTO process_chunks (process_id, content, section, page_number, embedding)
                   VALUES (%s, %s, %s, %s, %s::vector)""",
                (
                    process_id,
                    chunk["content"],
                    chunk["section"],
                    chunk["page_number"],
                    embedding_str,
                ),
            )
            chunk_count += 1

        conn.commit()
        total_chunks += chunk_count
        logger.info(f"Ingested process '{process['name']}' with {chunk_count} chunks")

    cur.close()
    conn.close()

    result = f"Ingested {len(data['processes'])} processes with {total_chunks} total chunks"
    logger.info(result)
    return result


if __name__ == "__main__":
    ingest_mock_data()
