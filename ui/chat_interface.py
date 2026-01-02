from core.document_processor import DocumentProcessor
from core.vector_store import VectorStoreManager
from core.chain import RAGChain

class ChatInterface:
    def __init__(self):
        self.processor = DocumentProcessor()
        self.vs = VectorStoreManager()
        self.vs.load()
        self.rag = RAGChain(self.vs)

    def ingest(self, paths):
        all_docs = []
        for p in paths:
            all_docs.extend(self.processor.process(p))
        self.vs.add_documents(all_docs)
        self.vs.save()

    def ask(self, query):
        return self.rag.run(query)
