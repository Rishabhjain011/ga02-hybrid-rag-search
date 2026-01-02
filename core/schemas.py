from dataclasses import dataclass
from typing import Dict

@dataclass
class DocumentChunk:
    source_id: str
    source_type: str
    title: str
    content: str
    metadata: Dict

@dataclass
class WebSearchResult:
    title: str
    content: str
    url: str

@dataclass
class AnswerSource:
    source_type: str   # "doc" or "web"
    reference: str
