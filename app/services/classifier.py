from __future__ import annotations
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
import joblib
import numpy as np
from app.core.config import settings


@dataclass
class PredictionResult:
    predicted_label: str
    confidence: float | None
    p_drone: float | None
    p_bird: float | None
    p_decoy: float | None
    p_unknown: float | None
    ood_score: float | None
    inferred_at: datetime


class BaselineClassifier:
    def __init__(self, artifact_path: str | None = None):
        path = Path(artifact_path or settings.model_artifact_path)
        self.model = joblib.load(path) if path.exists() else None

    def predict(
        self,
        *,
        mean_speed: float,
        heading_variability: float,
        jerk: float,
        thermal_signature: float,
        rcs_mean: float,
    ) -> PredictionResult:
        now = datetime.now(UTC)

        if self.model is None:
            drone_score = 0.0
            drone_score += 0.35 if thermal_signature > 0.65 else 0.0
            drone_score += 0.20 if heading_variability < 0.25 else 0.0
            drone_score += 0.20 if jerk < 0.8 else 0.0
            drone_score += 0.15 if rcs_mean > 0.08 else 0.0
            drone_score += 0.10 if mean_speed > 4.0 else 0.0
            predicted = "drone" if drone_score >= 0.5 else "bird"
            bird_score = max(0.0, 1.0 - drone_score)
            return PredictionResult(
                predicted_label=predicted,
                confidence=round(max(drone_score, bird_score), 4),
                p_drone=round(drone_score, 4),
                p_bird=round(bird_score, 4),
                p_decoy=0.05,
                p_unknown=0.05,
                ood_score=0.10,
                inferred_at=now,
            )

        x = np.array([[mean_speed, heading_variability, jerk, thermal_signature, rcs_mean]], dtype=float)
        pred = self.model.predict(x)[0]
        probs = self.model.predict_proba(x)[0] if hasattr(self.model, "predict_proba") else None
        classes = list(self.model.classes_) if hasattr(self.model, "classes_") else []
        prob_map = {cls: float(prob) for cls, prob in zip(classes, probs)} if probs is not None else {}

        return PredictionResult(
            predicted_label=str(pred),
            confidence=max(prob_map.values()) if prob_map else None,
            p_drone=prob_map.get("drone"),
            p_bird=prob_map.get("bird"),
            p_decoy=prob_map.get("decoy"),
            p_unknown=prob_map.get("unknown"),
            ood_score=0.05,
            inferred_at=now,
        )
