from langchain_groq import ChatGroq
from config.settings import settings
from tools.tavily_search import TavilySearchTool

class RAGChain:
    def __init__(self, vector_store):
        self.vs = vector_store
        self.web = TavilySearchTool()
        self.llm = ChatGroq(
            api_key=settings.GROQ_API_KEY,
            model=settings.LLM_MODEL,
            temperature=settings.LLM_TEMPERATURE
        )

    def classify_query(self, query: str):
        q = query.lower()
        if any(k in q for k in ["latest", "current", "today", "news"]):
            return "web"
        if "document" in q or "pdf" in q:
            return "doc"
        return "hybrid"

    def run(self, query: str):
        mode = self.classify_query(query)

        docs = self.vs.search(query)
        doc_context, doc_sources = "", []

        for i, d in enumerate(docs):
            ref = f"{d.metadata.get('source')} – Chunk {i}"
            doc_context += f"[DOC] {ref}\n{d.page_content}\n\n"
            doc_sources.append(ref)

        web_context, web_sources = "", []
        if mode in ["web", "hybrid"]:
            web_results = self.web.search(query)
            for w in web_results:
                web_context += f"[WEB] {w.title}\n{w.content}\n\n"
                web_sources.append(w.url)

        prompt = f"""
Use ONLY the information below to answer.

Document Context:
{doc_context}

Web Context:
{web_context}

Question:
{query}
"""

        answer = self.llm.invoke(prompt).content

        return {
            "answer": answer,
            "mode": mode,
            "doc_sources": doc_sources,
            "web_sources": web_sources
        }
