from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from core.text_cleaner import TextCleaner
from config.settings import settings

class DocumentProcessor:
    def __init__(self):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=settings.CHUNK_SIZE,
            chunk_overlap=settings.CHUNK_OVERLAP
        )

    def process(self, path: str):
        ext = Path(path).suffix.lower()
        loader = PyPDFLoader(path) if ext == ".pdf" else TextLoader(path)
        docs = loader.load()

        for d in docs:
            d.page_content = TextCleaner.clean(d.page_content)
            d.metadata["source"] = Path(path).name

        return self.splitter.split_documents(docs)
