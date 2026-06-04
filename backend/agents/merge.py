def merge_research(state):
    research_parts = state.get("research_results", [])
    all_sources = []
    final_research = ""

    for result in research_parts:
        final_research += result["research"]
        all_sources.extend(result["sources"])

    return {
        "research": final_research,
        "sources": all_sources
    }