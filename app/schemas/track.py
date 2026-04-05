from pydantic import BaseModel


class TrackSummary(BaseModel):
    track_id: str
    status: str
    current_position: dict
    track_quality: float | None = None
