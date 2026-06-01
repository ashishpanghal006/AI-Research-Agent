from langchain_groq import ChatGroq

llm = ChatGroq(model="llama-3.3-70b-versatile")

def analyst_agent(state):
    research = state["research"]
    prompt = f"""
    You are a senior research analyst.

    Analyze the research data below.

    Extract:

    1. Key Findings
    2. Important Trends
    3. Opportunities
    4. Risks
    5. Insights

    RESEARCH:

    {research}
    """

    response = llm.invoke(prompt)

    return {"analysis": response.content}