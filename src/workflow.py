from typing import TypedDict

from langgraph.graph import END, START, StateGraph

from .schemas import Incident


class TriageState(TypedDict):
    incident: Incident
    category: str
    hypothesis: str
    investigation_steps: list[str]


def assess_incident(state: TriageState) -> dict:
    error = (state["incident"].error_message or "").lower()

    if "cannot resolve column" in error:
        return {
            "category": "Schema or column mismatch",
            "hypothesis": (
                "A referenced column may be missing, renamed, "
                "or unavailable at this transformation step. "
                "The root cause is not yet confirmed."
            ),
        }

    return {
        "category": "Needs further investigation",
        "hypothesis": (
            "The available error does not match a known rule. "
            "Review logs and dependencies before drawing conclusions."
        ),
    }


def recommend_steps(state: TriageState) -> dict:
    if state["category"] == "Schema or column mismatch":
        steps = [
            "Inspect the failing task's full error and query.",
            "Compare source columns with the transformation's expectations.",
            "Check recent schema, code, and deployment changes.",
            "Confirm downstream impact and communicate the data delay.",
            "Validate the fix before an authorized rerun.",
        ]
    else:
        steps = [
            "Collect the failing task's logs and execution details.",
            "Check upstream data availability and dependencies.",
            "Review recent code and configuration changes.",
            "Confirm business impact and assign an investigation owner.",
        ]

    return {"investigation_steps": steps}


def build_workflow():
    graph = StateGraph(TriageState)

    graph.add_node("assess_incident", assess_incident)
    graph.add_node("recommend_steps", recommend_steps)

    graph.add_edge(START, "assess_incident")
    graph.add_edge("assess_incident", "recommend_steps")
    graph.add_edge("recommend_steps", END)

    return graph.compile()
