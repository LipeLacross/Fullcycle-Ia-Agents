CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE processes (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL,
    case_type VARCHAR(100) NOT NULL,
    parties JSONB NOT NULL,
    status VARCHAR(50) NOT NULL,
    sentence_summary TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE process_chunks (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    process_id UUID NOT NULL REFERENCES processes(id),
    content TEXT NOT NULL,
    section VARCHAR(100),
    page_number INTEGER,
    embedding vector(768),
    metadata JSONB DEFAULT '{}',
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_chunks_process_id ON process_chunks(process_id);
CREATE INDEX idx_chunks_embedding ON process_chunks
    USING hnsw (embedding vector_cosine_ops)
    WITH (m = 16, ef_construction = 64);
