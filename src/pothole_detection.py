"""Educational starter logic for flagging possible road-impact events.

This is a threshold-based demonstration, not a validated pothole classifier.
Accelerometer values should be calibrated for the sensor, device orientation,
mounting position, and sampling rate before any real-world use.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import sqrt
from typing import Iterable, Optional


@dataclass(frozen=True)
class AccelerationSample:
    """Acceleration sample in m/s^2, with optional GPS coordinates."""

    timestamp: float
    x: float
    y: float
    z: float
    latitude: Optional[float] = None
    longitude: Optional[float] = None


@dataclass(frozen=True)
class CandidateEvent:
    """A possible impact event; this does not prove a pothole exists."""

    timestamp: float
    magnitude: float
    score: float
    latitude: Optional[float]
    longitude: Optional[float]
    label: str = "candidate_needs_confirmation"


def acceleration_magnitude(sample: AccelerationSample) -> float:
    """Return the Euclidean magnitude of a 3-axis acceleration sample."""
    return sqrt(sample.x**2 + sample.y**2 + sample.z**2)


def detect_candidate_events(
    samples: Iterable[AccelerationSample],
    threshold_m_s2: float = 19.6,
) -> list[CandidateEvent]:
    """Flag samples whose raw acceleration magnitude exceeds a threshold.

    The default threshold is illustrative only. Raw magnitude includes gravity
    and is sensitive to phone orientation; production systems should calibrate
    sensors and estimate dynamic acceleration before applying thresholds.
    """
    if threshold_m_s2 <= 0:
        raise ValueError("threshold_m_s2 must be positive")

    events: list[CandidateEvent] = []
    for sample in samples:
        magnitude = acceleration_magnitude(sample)
        if magnitude >= threshold_m_s2:
            score = min(1.0, (magnitude - threshold_m_s2) / threshold_m_s2 + 0.5)
            events.append(
                CandidateEvent(
                    timestamp=sample.timestamp,
                    magnitude=magnitude,
                    score=score,
                    latitude=sample.latitude,
                    longitude=sample.longitude,
                )
            )
    return events


def _demo() -> None:
    samples = [
        AccelerationSample(1.0, 0.0, 0.0, 9.81, 13.0850, 80.2101),
        AccelerationSample(1.1, 3.0, 2.0, 21.0, 13.0851, 80.2102),
        AccelerationSample(1.2, 0.1, 0.2, 9.8, 13.0852, 80.2103),
    ]
    for event in detect_candidate_events(samples):
        print(event)


if __name__ == "__main__":
    _demo()
