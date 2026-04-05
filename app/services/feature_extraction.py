from __future__ import annotations
from math import atan2, sqrt
from statistics import mean, pstdev


def compute_mean_speed(points: list[dict]) -> float:
    speeds: list[float] = []
    for i in range(1, len(points)):
        dx = points[i]["x"] - points[i - 1]["x"]
        dy = points[i]["y"] - points[i - 1]["y"]
        dz = (points[i].get("z") or 0.0) - (points[i - 1].get("z") or 0.0)
        speeds.append(sqrt(dx * dx + dy * dy + dz * dz))
    return mean(speeds) if speeds else 0.0


def compute_heading_variability(points: list[dict]) -> float:
    headings: list[float] = []
    for i in range(1, len(points)):
        dx = points[i]["x"] - points[i - 1]["x"]
        dy = points[i]["y"] - points[i - 1]["y"]
        headings.append(atan2(dy, dx))
    return pstdev(headings) if len(headings) > 1 else 0.0


def compute_jerk(points: list[dict]) -> float:
    speeds: list[float] = []
    for i in range(1, len(points)):
        dx = points[i]["x"] - points[i - 1]["x"]
        dy = points[i]["y"] - points[i - 1]["y"]
        dz = (points[i].get("z") or 0.0) - (points[i - 1].get("z") or 0.0)
        speeds.append(sqrt(dx * dx + dy * dy + dz * dz))

    if len(speeds) < 2:
        return 0.0

    deltas = [abs(speeds[i] - speeds[i - 1]) for i in range(1, len(speeds))]
    return mean(deltas) if deltas else 0.0
