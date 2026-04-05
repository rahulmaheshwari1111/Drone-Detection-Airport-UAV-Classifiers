from datetime import UTC, datetime
from sqlalchemy.orm import Session
from app.models.track import Track


def create_track(db: Session, *, x: float, y: float, z: float | None, vx: float | None, vy: float | None, vz: float | None) -> Track:
    now = datetime.now(UTC)
    track = Track(
        status="tentative",
        first_seen_at=now,
        last_seen_at=now,
        current_x=x,
        current_y=y,
        current_z=z,
        current_vx=vx,
        current_vy=vy,
        current_vz=vz,
        track_quality=1.0,
        source_sensors=[],
    )
    db.add(track)
    db.commit()
    db.refresh(track)
    return track


def get_track_by_id(db: Session, track_id: str) -> Track | None:
    return db.query(Track).filter(Track.id == track_id).first()


def list_active_tracks(db: Session) -> list[Track]:
    return (
        db.query(Track)
        .filter(Track.status.in_(["tentative", "confirmed", "stale"]))
        .order_by(Track.last_seen_at.desc())
        .all()
    )


def update_track_position(db: Session, track: Track, *, x: float, y: float, z: float | None, vx: float | None, vy: float | None, vz: float | None) -> Track:
    track.current_x = x
    track.current_y = y
    track.current_z = z
    track.current_vx = vx
    track.current_vy = vy
    track.current_vz = vz
    track.last_seen_at = datetime.now(UTC)
    if track.status == "tentative":
        track.status = "confirmed"
    db.add(track)
    db.commit()
    db.refresh(track)
    return track
