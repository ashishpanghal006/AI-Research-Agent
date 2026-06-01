from langchain_groq import ChatGroq

llm = ChatGroq(model="llama-3.3-70b-versatile")

def planner_agent(state):
    query = state["query"]
    prompt = f"""
    You are a planning agent.

    Create a research plan for:
    
    {query}

    Keep it concise.
    """

    response = llm.invoke(prompt)

    return {
        "plan": response.content
    }