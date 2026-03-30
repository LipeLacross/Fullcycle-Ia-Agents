import google.genai as genai
from google.genai import types
from app.config import GOOGLE_API_KEY, EMBEDDING_MODEL

client = genai.Client(api_key=GOOGLE_API_KEY)


def generate_embedding(text: str) -> list[float]:
    """Generate embedding using Gemini embedding model."""
    result = client.models.embed_content(
        model=EMBEDDING_MODEL,
        contents=text,
        config=types.EmbedContentConfig(output_dimensionality=768),
    )
    return result.embeddings[0].values
