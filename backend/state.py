from typing import TypedDict
from typing import Annotated
import operator


class AgentState(TypedDict):
    query: str
    plan: str
    research_questions: list[str]
    research_results: Annotated[list, operator.add]
    research: str
    sources: Annotated[list, operator.add]
    analysis: str
    report: str

class ResearchState(TypedDict):
    question: str
    research_results: list