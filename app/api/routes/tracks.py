from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.repositories.tracks import list_active_tracks
from app.schemas.track import TrackSummary

router = APIRouter(prefix="/tracks", tags=["tracks"])


@router.get("", response_model=list[TrackSummary])
def get_tracks(db: Session = Depends(get_db)) -> list[TrackSummary]:
    tracks = list_active_tracks(db)
    return [
        TrackSummary(
            track_id=str(track.id),
            status=track.status,
            current_position={"x": track.current_x, "y": track.current_y, "z": track.current_z},
            track_quality=track.track_quality,
        )
        for track in tracks
    ]
