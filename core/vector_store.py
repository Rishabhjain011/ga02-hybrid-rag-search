import os
from typing import List, Optional
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from core.embeddings import EmbeddingManager
from config.settings import settings


class VectorStoreManager:
    def __init__(self):
        self.embedding_manager = EmbeddingManager()
        self.embeddings = self.embedding_manager.embeddings
        self.store: Optional[FAISS] = None

    def load(self):
        index_file = os.path.join(settings.FAISS_INDEX_PATH, "index.faiss")
        if os.path.exists(index_file):
            self.store = FAISS.load_local(
                settings.FAISS_INDEX_PATH,
                self.embeddings,
                allow_dangerous_deserialization=True,
            )
        else:
            self.store = None

    def add_documents(self, docs: List[Document]):
        """
        Explicitly control embeddings to avoid FAISS shape errors.
        """
        texts = [d.page_content for d in docs]
        metadatas = [d.metadata for d in docs]

        if not self.store:
            self.store = FAISS.from_texts(
                texts=texts,
                embedding=self.embeddings,
                metadatas=metadatas,
            )
        else:
            self.store.add_texts(
                texts=texts,
                metadatas=metadatas,
            )

    def search(self, query: str):
        if not self.store:
            return []
        return self.store.similarity_search(query, settings.TOP_K)

    def save(self):
        os.makedirs(settings.FAISS_INDEX_PATH, exist_ok=True)
        if self.store:
            self.store.save_local(settings.FAISS_INDEX_PATH)
