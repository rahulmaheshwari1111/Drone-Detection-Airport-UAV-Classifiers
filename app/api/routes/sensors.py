from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.schemas.detection import DetectionIn, DetectionOut
from app.repositories.sensors import get_sensor_by_code
from app.repositories.detections import create_detection
from app.services.tracking import associate_or_create_track

router = APIRouter(prefix="/detections", tags=["detections"])


@router.post("", response_model=DetectionOut)
def ingest_detection(payload: DetectionIn, db: Session = Depends(get_db)) -> DetectionOut:
    sensor = get_sensor_by_code(db, payload.sensor_code)
    if sensor is None:
        raise HTTPException(status_code=404, detail=f"Sensor not found: {payload.sensor_code}")

    track = associate_or_create_track(db=db, detection=payload)
    detection = create_detection(db=db, sensor_id=sensor.id, track_id=track.id, payload=payload)

    return DetectionOut(id=str(detection.id), track_id=str(track.id), status="accepted")
