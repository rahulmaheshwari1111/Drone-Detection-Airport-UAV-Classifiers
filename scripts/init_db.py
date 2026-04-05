from app.core.database import Base, engine
from app.models.sensor import Sensor
from app.models.track import Track
from app.models.detection import Detection
from app.models.feature import TrackFeature
from app.models.model_version import ModelVersion
from app.models.classification import Classification
from app.models.alert import Alert
from app.models.incident import Incident


def main() -> None:
    Base.metadata.create_all(bind=engine)
    print("Database tables created.")


if __name__ == "__main__":
    main()
