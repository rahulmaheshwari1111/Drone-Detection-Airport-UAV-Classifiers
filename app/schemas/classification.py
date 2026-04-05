from datetime import datetime
from pydantic import BaseModel


class ClassificationRequest(BaseModel):
    track_id: str
    mean_speed: float
    heading_variability: float
    jerk: float
    thermal_signature: float
    rcs_mean: float


class ClassificationResponse(BaseModel):
    track_id: str
    inferred_at: datetime
    predicted_label: str
    confidence: float | None = None
    p_drone: float | None = None
    p_bird: float | None = None
    p_decoy: float | None = None
    p_unknown: float | None = None
    ood_score: float | None = None
