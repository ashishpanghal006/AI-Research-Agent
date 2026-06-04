import os

from tavily import TavilyClient


api_key = os.getenv("TAVILY_API_KEY")

if not api_key:
    raise ValueError("TAVILY_API_KEY not found")

client = TavilyClient(api_key=api_key)

def web_search(query: str):
    
    return client.search(query=query, search_depth="advanced", max_results=3)