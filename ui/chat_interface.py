from core.document_processor import DocumentProcessor
from core.vector_store import VectorStoreManager
from core.chain import RAGChain

class ChatInterface:
    def __init__(self):
        self.processor = DocumentProcessor()
        self.vector_store = VectorStoreManager()
        self.vector_store.load()
        self.rag = RAGChain(self.vector_store)

    def ingest(self, paths):
        for p in paths:
            docs = self.processor.process(p)
            self.vector_store.add_documents(docs)
        self.vector_store.save()

    def ask(self, query, use_web=False):
        if not self.vector_store.store:
            return "❌ Please upload and index documents first."
        return self.rag.run(query, use_web)