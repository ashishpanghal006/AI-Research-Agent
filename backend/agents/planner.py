from pydantic import BaseModel
from config.llm import llm

class ResearchPlan(BaseModel):
    plan: str
    questions: list[str]

structured_llm = llm.with_structured_output(ResearchPlan)

def planner_agent(state):
    query = state["query"]
    response = structured_llm.invoke(
        f"""
        Create a research strategy.

        Topic:
        {query}

        Generate:

        1. A concise research plan
        2. Five important research questions
        """
    )

    return {
        "plan": response.plan,
        "research_questions": response.questions
    }