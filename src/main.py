from pathlib import Path

from src.schemas import Incident


def main():
    project_root = Path(__file__).resolve().parent.parent
    incident_file = project_root / "examples" / "sample_incident.json"

    incident = Incident.model_validate_json(
        incident_file.read_text(encoding="utf-8")
    )

    print("Incident validated successfully")
    print(f"Incident ID: {incident.incident_id}")
    print(f"Pipeline: {incident.pipeline_name}")
    print(f"Priority: {incident.reported_priority}")
    print(f"Business impact: {incident.business_impact}")


if __name__ == "__main__":
    main()
