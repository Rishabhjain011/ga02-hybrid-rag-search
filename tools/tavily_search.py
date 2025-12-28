import os
from langchain_tavily import TavilySearch
from config.settings import settings


class TavilySearchTool:
    def __init__(self, k: int = 3):
        os.environ["TAVILY_API_KEY"] = settings.TAVILY_API_KEY
        self.tool = TavilySearch(max_results=k)

    def search(self, query: str) -> str:
        """
        Returns clean web context as STRING.
        Handles all Tavily return formats safely.
        """
        result = self.tool.invoke(query)

        # Case 1: Already a string
        if isinstance(result, str):
            return f"[Web]\n{result}"

        # Case 2: Dict with results list
        if isinstance(result, dict) and "results" in result:
            snippets = []
            for r in result["results"]:
                title = r.get("title", "")
                content = r.get("content", "")
                url = r.get("url", "")
                snippets.append(
                    f"[Web] {title}\n{content}\nSource: {url}"
                )
            return "\n\n".join(snippets)

        # Fallback (safe)
        return f"[Web]\n{str(result)}"
