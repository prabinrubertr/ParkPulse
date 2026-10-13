"""Simple confirmation-based parking availability estimate.

This educational module does not infer parking occupancy from motion sensors.
It aggregates explicit observations and returns a transparent confidence score.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Iterable, Literal


Status = Literal["available", "occupied"]


@dataclass(frozen=True)
class ParkingObservation:
    space_id: str
    status: Status
    observed_at: datetime
    source: str = "community"


@dataclass(frozen=True)
class ParkingEstimate:
    space_id: str
    status: str
    confidence: float
    observation_count: int
    last_observed_at: datetime | None


def estimate_space(
    space_id: str,
    observations: Iterable[ParkingObservation],
    now: datetime | None = None,
    freshness_seconds: int = 900,
) -> ParkingEstimate:
    """Estimate status using recent observations, weighting newer reports more.

    Reports older than freshness_seconds are ignored. This is a starter rule,
    not a guarantee that the space is still available or occupied.
    """
    if freshness_seconds <= 0:
        raise ValueError("freshness_seconds must be positive")

    current = now or datetime.now(timezone.utc)
    if current.tzinfo is None:
        raise ValueError("now must be timezone-aware")

    recent: list[ParkingObservation] = []
    for obs in observations:
        if obs.space_id != space_id:
            continue
        if obs.observed_at.tzinfo is None:
            raise ValueError("observation timestamps must be timezone-aware")
        age = (current - obs.observed_at).total_seconds()
        if 0 <= age <= freshness_seconds:
            recent.append(obs)

    if not recent:
        return ParkingEstimate(space_id, "unknown", 0.0, 0, None)

    # Each report contributes more when it is newer. Use a small floor so
    # observations near expiry still contribute but do not dominate.
    weights = [
        max(0.05, 1.0 - (current - obs.observed_at).total_seconds() / freshness_seconds)
        for obs in recent
    ]
    available_weight = sum(
        weight for obs, weight in zip(recent, weights) if obs.status == "available"
    )
    occupied_weight = sum(
        weight for obs, weight in zip(recent, weights) if obs.status == "occupied"
    )
    total_weight = available_weight + occupied_weight
    if available_weight == occupied_weight:
        status = "conflicting"
        confidence = 0.0
    else:
        status = "available" if available_weight > occupied_weight else "occupied"
        confidence = abs(available_weight - occupied_weight) / total_weight

    return ParkingEstimate(
        space_id=space_id,
        status=status,
        confidence=round(confidence, 3),
        observation_count=len(recent),
        last_observed_at=max(obs.observed_at for obs in recent),
    )


def _demo() -> None:
    now = datetime.now(timezone.utc)
    reports = [
        ParkingObservation("A-12", "available", now, "community"),
        ParkingObservation("A-12", "available", now, "community"),
        ParkingObservation("A-12", "occupied", now, "community"),
    ]
    print(estimate_space("A-12", reports, now=now))


if __name__ == "__main__":
    _demo()
