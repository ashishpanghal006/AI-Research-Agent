from tools.search import web_search

def researcher_agent(state):
    query = state["query"]
    results = web_search(query)
    research_data = ""

    for item in results["results"]:
        title = item["title"]
        content = item["content"]
        url = item["url"]

        research_data += f"""

        Title: {title}

        Content:
        {content}

        Source:
        {url}

        --------------------------------

        """

    return {"research": research_data}