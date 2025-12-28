import os
from dataclasses import dataclass
from dotenv import load_dotenv

# Load .env for local development
load_dotenv()

# Prevent HF tokenizer warning
os.environ["TOKENIZERS_PARALLELISM"] = "false"


def get_secret(key: str, default: str = "") -> str:
    """
    Safe secret loader:
    1. Environment variables (.env / system)
    2. Streamlit secrets (if present)
    3. Default value
    """
    value = os.getenv(key)
    if value is not None:
        return value

    try:
        import streamlit as st
        return st.secrets.get(key, default)
    except Exception:
        return default


@dataclass
class Settings:
    # API Keys
    GROQ_API_KEY: str = get_secret("GROQ_API_KEY")
    TAVILY_API_KEY: str = get_secret("TAVILY_API_KEY")

    # LLM config
    LLM_MODEL: str = get_secret("LLM_MODEL", "llama-3.1-8b-instant")
    LLM_TEMPERATURE: float = float(get_secret("LLM_TEMPERATURE", "0.0"))

    # HuggingFace embeddings (LOCAL)
    EMBEDDING_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"

    # Chunking
    CHUNK_SIZE: int = 1000
    CHUNK_OVERLAP: int = 200

    # Retrieval
    TOP_K: int = 3

    # FAISS
    FAISS_INDEX_PATH: str = "data/faiss_index"

    def validate(self):
        if not self.GROQ_API_KEY:
            raise ValueError("❌ GROQ_API_KEY missing")
        if not self.TAVILY_API_KEY:
            raise ValueError("❌ TAVILY_API_KEY missing")


# ✅ Singleton instance (DO NOT RENAME)
settings = Settings()
