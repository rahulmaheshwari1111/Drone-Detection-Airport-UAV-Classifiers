from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.schemas.classification import ClassificationRequest, ClassificationResponse
from app.repositories.tracks import get_track_by_id
from app.repositories.classifications import save_classification
from app.services.classifier import BaselineClassifier

router = APIRouter(prefix="/classifications", tags=["classifications"])
classifier = BaselineClassifier()


@router.post("", response_model=ClassificationResponse)
def classify(payload: ClassificationRequest, db: Session = Depends(get_db)) -> ClassificationResponse:
    track = get_track_by_id(db, payload.track_id)
    if track is None:
        raise HTTPException(status_code=404, detail=f"Track not found: {payload.track_id}")

    result = classifier.predict(
        mean_speed=payload.mean_speed,
        heading_variability=payload.heading_variability,
        jerk=payload.jerk,
        thermal_signature=payload.thermal_signature,
        rcs_mean=payload.rcs_mean,
    )

    save_classification(db=db, track_id=track.id, result=result)

    return ClassificationResponse(
        track_id=payload.track_id,
        inferred_at=result.inferred_at,
        predicted_label=result.predicted_label,
        confidence=result.confidence,
        p_drone=result.p_drone,
        p_bird=result.p_bird,
        p_decoy=result.p_decoy,
        p_unknown=result.p_unknown,
        ood_score=result.ood_score,
    )
