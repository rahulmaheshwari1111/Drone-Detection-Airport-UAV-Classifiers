from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.repositories.alerts import list_alerts
from app.schemas.alert import AlertSummary

router = APIRouter(prefix="/alerts", tags=["alerts"])


@router.get("", response_model=list[AlertSummary])
def get_alerts(db: Session = Depends(get_db)) -> list[AlertSummary]:
    alerts = list_alerts(db)
    return [
        AlertSummary(
            alert_id=str(alert.id),
            severity=alert.severity,
            status=alert.status,
            threat_score=alert.threat_score,
            title=alert.title,
        )
        for alert in alerts
    ]
