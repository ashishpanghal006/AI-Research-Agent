from langchain_groq import ChatGroq

llm = ChatGroq(model="llama-3.3-70b-versatile")

def writer_agent(state):
    query = state["query"]
    plan = state["plan"]
    analysis = state["analysis"]

    prompt = f"""
    Create a professional research report.

    TOPIC:
    {query}

    RESEARCH PLAN:
    {plan}

    ANALYSIS:
    {analysis}

    Format:

    # Executive Summary

    # Key Findings

    # Market Insights

    # Opportunities

    # Risks

    # Conclusion
    """

    response = llm.invoke(prompt)

    return {"report": response.content}