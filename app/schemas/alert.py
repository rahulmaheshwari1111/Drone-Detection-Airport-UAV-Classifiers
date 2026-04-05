from pydantic import BaseModel


class AlertSummary(BaseModel):
    alert_id: str
    severity: str
    status: str
    threat_score: float
    title: str
