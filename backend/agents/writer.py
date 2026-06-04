from config.llm import llm

def writer_agent(state):
    query = state["query"]
    plan = state["plan"]
    analysis = state["analysis"]
    sources = state["sources"]

    unique_urls = list(
        {
            source["url"]
            for source in sources
        }
    )

    reference_text = "\n".join(
        [
            f"- {url}"
            for url in unique_urls[:20]
        ]
    )

    prompt = f"""
    Create a professional research report.

    TOPIC:
    {query}

    RESEARCH PLAN:
    {plan}

    ANALYSIS:
    {analysis}

    REFERENCES:
    {reference_text}

    Format:

    # Executive Summary

    # Key Findings

    # Market Insights

    # Opportunities

    # Risks

    # References

    # Conclusion
    """

    response = llm.invoke(prompt)

    return {"report": response.content}