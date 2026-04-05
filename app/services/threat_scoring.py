from dataclasses import dataclass


@dataclass
class ThreatInputs:
    p_drone: float
    geofence_breach: float
    runway_risk: float
    swarm_score: float
    rf_anomaly: float
    persistence: float


def compute_threat_score(inputs: ThreatInputs) -> float:
    score = (
        0.35 * inputs.p_drone +
        0.20 * inputs.geofence_breach +
        0.15 * inputs.runway_risk +
        0.10 * inputs.swarm_score +
        0.10 * inputs.rf_anomaly +
        0.10 * inputs.persistence
    )
    return round(min(max(score, 0.0), 1.0), 4)


def severity_from_score(score: float) -> str:
    if score >= 0.8:
        return "critical"
    if score >= 0.5:
        return "warning"
    return "info"
