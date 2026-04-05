import uuid
from datetime import datetime
from sqlalchemy import String, DateTime, Float, ForeignKey, JSON, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base


class Classification(Base):
    __tablename__ = "classifications"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    track_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("tracks.id"), nullable=False)
    feature_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey("track_features.id"))
    model_version_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey("model_versions.id"))
    inferred_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    predicted_label: Mapped[str] = mapped_column(String, nullable=False)
    confidence: Mapped[float | None] = mapped_column(Float)
    p_drone: Mapped[float | None] = mapped_column(Float)
    p_bird: Mapped[float | None] = mapped_column(Float)
    p_decoy: Mapped[float | None] = mapped_column(Float)
    p_unknown: Mapped[float | None] = mapped_column(Float)
    ood_score: Mapped[float | None] = mapped_column(Float)
    explanation_json: Mapped[dict] = mapped_column(JSON, default=dict, nullable=False)
