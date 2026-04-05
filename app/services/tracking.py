from __future__ import annotations
from sqlalchemy.orm import Session
from app.repositories.tracks import create_track, list_active_tracks, update_track_position
from app.schemas.detection import DetectionIn


ASSOCIATION_DISTANCE_THRESHOLD = 50.0


def _distance(a_x: float, a_y: float, b_x: float, b_y: float) -> float:
    return ((a_x - b_x) ** 2 + (a_y - b_y) ** 2) ** 0.5


def associate_or_create_track(db: Session, detection: DetectionIn):
    candidates = list_active_tracks(db)
    best_track = None
    best_distance = None

    for track in candidates:
        if track.current_x is None or track.current_y is None:
            continue
        dist = _distance(track.current_x, track.current_y, detection.x, detection.y)
        if dist <= ASSOCIATION_DISTANCE_THRESHOLD and (best_distance is None or dist < best_distance):
            best_distance = dist
            best_track = track

    if best_track is None:
        return create_track(
            db,
            x=detection.x,
            y=detection.y,
            z=detection.z,
            vx=detection.vx,
            vy=detection.vy,
            vz=detection.vz,
        )

    return update_track_position(
        db,
        best_track,
        x=detection.x,
        y=detection.y,
        z=detection.z,
        vx=detection.vx,
        vy=detection.vy,
        vz=detection.vz,
    )
