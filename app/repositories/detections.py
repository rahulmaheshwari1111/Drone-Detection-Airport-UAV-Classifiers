from sqlalchemy.orm import Session
from app.models.detection import Detection
from app.schemas.detection import DetectionIn


def create_detection(db: Session, *, sensor_id, track_id, payload: DetectionIn) -> Detection:
    detection = Detection(
        sensor_id=sensor_id,
        track_id=track_id,
        event_ts=payload.event_ts,
        x=payload.x,
        y=payload.y,
        z=payload.z,
        vx=payload.vx,
        vy=payload.vy,
        vz=payload.vz,
        snr_db=payload.snr_db,
        rcs_estimate=payload.rcs_estimate,
        thermal_value=payload.thermal_value,
        quality_score=payload.quality_score,
        raw_payload=payload.raw_payload,
    )
    db.add(detection)
    db.commit()
    db.refresh(detection)
    return detection
