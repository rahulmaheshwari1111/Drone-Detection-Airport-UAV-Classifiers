import uuid
from datetime import datetime
from sqlalchemy import String, DateTime, Float, func, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base


class Track(Base):
    __tablename__ = "tracks"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    external_track_ref: Mapped[str | None] = mapped_column(String)
    status: Mapped[str] = mapped_column(String, nullable=False)
    first_seen_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    last_seen_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    current_x: Mapped[float | None] = mapped_column(Float)
    current_y: Mapped[float | None] = mapped_column(Float)
    current_z: Mapped[float | None] = mapped_column(Float)
    current_vx: Mapped[float | None] = mapped_column(Float)
    current_vy: Mapped[float | None] = mapped_column(Float)
    current_vz: Mapped[float | None] = mapped_column(Float)
    track_quality: Mapped[float | None] = mapped_column(Float)
    source_sensors: Mapped[list] = mapped_column(JSON, default=list, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
