import os

from tavily import TavilyClient

client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)

def websearch(query: str):
    result = client.search(query=query, search_depth="advanced", max_results=5)
    return result