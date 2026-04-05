from sqlalchemy.orm import Session
from app.models.classification import Classification
from app.services.classifier import PredictionResult


def save_classification(db: Session, *, track_id, result: PredictionResult) -> Classification:
    row = Classification(
        track_id=track_id,
        predicted_label=result.predicted_label,
        confidence=result.confidence,
        p_drone=result.p_drone,
        p_bird=result.p_bird,
        p_decoy=result.p_decoy,
        p_unknown=result.p_unknown,
        ood_score=result.ood_score,
        explanation_json={},
    )
    db.add(row)
    db.commit()
    db.refresh(row)
    return row
