from sqlalchemy.orm import Session
from app.models.sensor import Sensor


def get_sensor_by_code(db: Session, sensor_code: str) -> Sensor | None:
    return db.query(Sensor).filter(Sensor.sensor_code == sensor_code).first()
