from src.schemas import Incident


def draft_update(incident: Incident, recommendation: str) -> str:
    return (
        f"Subject: Pipeline incident — {incident.pipeline_name}\n\n"
        f"Incident: {incident.incident_id}\n"
        f"Reported priority: {incident.reported_priority or 'Not provided'}\n\n"
        f"Summary: {incident.description}\n\n"
        f"Business impact: "
        f"{incident.business_impact or 'Pending assessment'}\n\n"
        f"Suggested investigation: {recommendation}\n\n"
        "Recovery ETA: To be confirmed.\n"
        "Next update: [Enter an agreed time before sending.]"
    )