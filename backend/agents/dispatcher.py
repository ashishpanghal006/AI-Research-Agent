from langgraph.constants import Send


def dispatch_research(state):
    questions = state["research_questions"]

    return [
        Send(
            "research_worker",
            {
                "question": question
            }
        )
        for question in questions
    ]