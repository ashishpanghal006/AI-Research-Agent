from config.llm import llm

def analyst_agent(state):
    research = state["research"]
    prompt = f"""
    You are a senior research analyst.

    Based on the research summaries below, provide:

    1. Key Findings
    2. Important Trends
    3. Opportunities
    4. Risks
    5. Strategic Insights

    Keep the response concise and actionable.

    RESEARCH SUMMARIES:

    {research}
    """

    response = llm.invoke(prompt)

    return {"analysis": response.content}