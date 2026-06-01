from langgraph.graph import StateGraph
from langgraph.graph import END

from state import AgentState

from agents.planner import planner_agent
from agents.researcher import researcher_agent


workflow = StateGraph(AgentState)

workflow.add_node("planner", planner_agent)
workflow.add_node("researcher", researcher_agent)

workflow.set_entry_point("planner")

workflow.add_edge("planner", "researcher")
workflow.add_edge("researcher", END)

graph = workflow.compile()