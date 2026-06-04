from tools.search import web_search
from config.llm import llm


def research_worker(state):

    question = state["question"]
    results = web_search(question)
    research_text = ""
    sources = []
    raw_content = ""

    for item in results["results"]:
        title = item.get("title", "")
        content = item.get("content", "")[:500]
        url = item.get("url", "")

        raw_content += f"""
        Title: {title}

        Content:
        {content}
        """

        sources.append(
            {
                "title": title,
                "url": url
            }
        )

    summary = llm.invoke(
        f"""
        You are a professional research assistant.

        Summarize the research below.

        Focus on:
        - Key facts
        - Important statistics
        - Major trends
        - Notable opportunities
        - Important risks

        Keep the summary concise (150-200 words).

        RESEARCH:

        {raw_content}
        """
    )

    return {
        "research_results": [
            {
                "research": summary.content,
                "sources": sources
            }
        ]
    }