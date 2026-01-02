import os
from langchain_tavily import TavilySearch
from config.settings import settings
from core.schemas import WebSearchResult

class TavilySearchTool:
    def __init__(self):
        os.environ["TAVILY_API_KEY"] = settings.TAVILY_API_KEY
        self.tool = TavilySearch(max_results=3)

    def search(self, query: str):
        result = self.tool.invoke(query)
        results = []

        if isinstance(result, dict) and "results" in result:
            for r in result["results"]:
                results.append(
                    WebSearchResult(
                        title=r.get("title", ""),
                        content=r.get("content", ""),
                        url=r.get("url", "")
                    )
                )
        return results
