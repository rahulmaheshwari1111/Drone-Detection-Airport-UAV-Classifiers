from datetime import datetime
from pydantic import BaseModel, Field


class DetectionIn(BaseModel):
    sensor_code: str
    event_ts: datetime
    x: float
    y: float
    z: float | None = None
    vx: float | None = None
    vy: float | None = None
    vz: float | None = None
    snr_db: float | None = None
    rcs_estimate: float | None = None
    thermal_value: float | None = None
    quality_score: float | None = Field(default=1.0, ge=0.0, le=1.0)
    raw_payload: dict = Field(default_factory=dict)


class DetectionOut(BaseModel):
    id: str
    track_id: str | None = None
    status: str
