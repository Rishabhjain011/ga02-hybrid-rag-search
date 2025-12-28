from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from config.settings import settings
from tools.tavily_search import TavilySearchTool

PROMPT = ChatPromptTemplate.from_template("""
You are an AI assistant.

Answer the question using the context below.
If the answer is not present, say you don't know.

Context:
{context}

Question:
{question}
""")

class RAGChain:
    def __init__(self, vector_store):
        self.vector_store = vector_store
        self.web_search = TavilySearchTool()
        self.llm = ChatGroq(
            model=settings.LLM_MODEL,
            temperature=settings.LLM_TEMPERATURE,
            api_key=settings.GROQ_API_KEY,
        )

    def run(self, query: str, use_web: bool = False):
        # 1️⃣ Document context
        docs = self.vector_store.search(query)
        doc_context = "\n\n".join(
            f"[Doc] {d.page_content}" for d in docs
        )

        # 2️⃣ Web context (optional)
        web_context = ""
        if use_web:
            web_context = self.web_search.search(query)

        # 3️⃣ Hybrid context
        full_context = doc_context
        if web_context:
            full_context += "\n\n" + web_context

        # 4️⃣ LLM
        chain = PROMPT | self.llm | StrOutputParser()
        return chain.invoke({
            "context": full_context,
            "question": query
        })
