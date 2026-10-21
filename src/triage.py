from src.schemas import Incident


def recommend_action(incident: Incident) -> str:
    error = (incident.error_message or "").lower()

    if "cannot resolve column" in error:
        return (
            "Compare the source dataset columns with the pipeline's "
            "expected schema. Check whether 'net_sales' was renamed, "
            "removed, or omitted in an earlier transformation."
        )

    if "source file missing" in error:
        return (
            "Check whether the expected source file arrived. "
            "If absent, contact the source team. "
            "Once available, validate the file before rerunning the pipeline."
        )

    return "Review the pipeline logs to identify the failure."