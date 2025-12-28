from pathlib import Path
from typing import List
from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from config.settings import settings


class DocumentProcessor:
    def __init__(self):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=settings.CHUNK_SIZE,
            chunk_overlap=settings.CHUNK_OVERLAP,
        )

    def load(self, path: str) -> List[Document]:
        ext = Path(path).suffix.lower()
        if ext == ".pdf":
            return PyPDFLoader(path).load()
        if ext == ".txt":
            return TextLoader(path, encoding="utf-8").load()
        raise ValueError("Unsupported file type")

    def process(self, path: str) -> List[Document]:
        return self.splitter.split_documents(self.load(path))
