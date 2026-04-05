import uuid
from datetime import datetime
from sqlalchemy import DateTime, Float, Integer, ForeignKey, func, JSON, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base


class TrackFeature(Base):
    __tablename__ = "track_features"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    track_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("tracks.id"), nullable=False)
    computed_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    window_size: Mapped[int] = mapped_column(Integer, nullable=False)
    mean_speed: Mapped[float | None] = mapped_column(Float)
    heading_variability: Mapped[float | None] = mapped_column(Float)
    jerk: Mapped[float | None] = mapped_column(Float)
    thermal_signature: Mapped[float | None] = mapped_column(Float)
    rcs_mean: Mapped[float | None] = mapped_column(Float)
    acceleration_std: Mapped[float | None] = mapped_column(Float)
    hover_ratio: Mapped[float | None] = mapped_column(Float)
    path_curvature: Mapped[float | None] = mapped_column(Float)
    rcs_variance: Mapped[float | None] = mapped_column(Float)
    micro_doppler_entropy: Mapped[float | None] = mapped_column(Float)
    rf_presence: Mapped[bool | None] = mapped_column(Boolean)
    feature_json: Mapped[dict] = mapped_column(JSON, default=dict, nullable=False)
