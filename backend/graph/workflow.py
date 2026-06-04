from langgraph.graph import StateGraph
from langgraph.graph import END

from state import AgentState

from agents.planner import planner_agent
from agents.dispatcher import dispatch_research
from agents.research_worker import research_worker
from agents.merge import merge_research
from agents.analyst import analyst_agent
from agents.writer import writer_agent


workflow = StateGraph(AgentState)

workflow.add_node("planner", planner_agent)
workflow.add_node("research_worker", research_worker)
workflow.add_node("merge", merge_research)
workflow.add_node("analyst", analyst_agent)
workflow.add_node("writer", writer_agent)

workflow.set_entry_point("planner")

workflow.add_conditional_edges("planner", dispatch_research, ["research_worker"])

workflow.add_edge("research_worker", "merge")
workflow.add_edge("merge", "analyst")
workflow.add_edge("analyst", "writer")
workflow.add_edge("writer", END)

graph = workflow.compile()