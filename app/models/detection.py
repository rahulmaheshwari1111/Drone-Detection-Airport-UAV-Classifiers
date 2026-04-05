import uuid
from datetime import datetime
from sqlalchemy import DateTime, Float, ForeignKey, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base


class Detection(Base):
    __tablename__ = "detections"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    sensor_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("sensors.id"), nullable=False)
    track_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey("tracks.id"))
    event_ts: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    x: Mapped[float] = mapped_column(Float, nullable=False)
    y: Mapped[float] = mapped_column(Float, nullable=False)
    z: Mapped[float | None] = mapped_column(Float)
    vx: Mapped[float | None] = mapped_column(Float)
    vy: Mapped[float | None] = mapped_column(Float)
    vz: Mapped[float | None] = mapped_column(Float)
    snr_db: Mapped[float | None] = mapped_column(Float)
    rcs_estimate: Mapped[float | None] = mapped_column(Float)
    thermal_value: Mapped[float | None] = mapped_column(Float)
    quality_score: Mapped[float | None] = mapped_column(Float)
    raw_payload: Mapped[dict] = mapped_column(JSON, default=dict, nullable=False)
