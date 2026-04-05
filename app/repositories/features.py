from sqlalchemy.orm import Session
from app.models.feature import TrackFeature


def create_feature(db: Session, **kwargs) -> TrackFeature:
    feature = TrackFeature(**kwargs)
    db.add(feature)
    db.commit()
    db.refresh(feature)
    return feature
