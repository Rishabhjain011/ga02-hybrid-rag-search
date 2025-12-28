from langchain_huggingface import HuggingFaceEmbeddings
from config.settings import settings


class EmbeddingManager:
    def __init__(self):
        self._embeddings = HuggingFaceEmbeddings(
            model_name=settings.EMBEDDING_MODEL,
            encode_kwargs={"normalize_embeddings": True},
        )

    @property
    def embeddings(self):
        return self._embeddings
