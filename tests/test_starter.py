import sys
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from pothole_detection import AccelerationSample, acceleration_magnitude, detect_candidate_events
from parking_estimation import ParkingObservation, estimate_space


class PotholeDetectionTests(unittest.TestCase):
    def test_acceleration_magnitude(self):
        sample = AccelerationSample(1.0, 3.0, 4.0, 0.0)
        self.assertAlmostEqual(acceleration_magnitude(sample), 5.0)

    def test_candidate_event_threshold(self):
        samples = [
            AccelerationSample(1.0, 0.0, 0.0, 9.81),
            AccelerationSample(2.0, 0.0, 0.0, 22.0, 13.0, 80.0),
        ]
        events = detect_candidate_events(samples, threshold_m_s2=19.6)
        self.assertEqual(len(events), 1)
        self.assertEqual(events[0].label, "candidate_needs_confirmation")


class ParkingEstimationTests(unittest.TestCase):
    def test_available_majority(self):
        now = datetime.now(timezone.utc)
        observations = [
            ParkingObservation("P1", "available", now),
            ParkingObservation("P1", "available", now),
            ParkingObservation("P1", "occupied", now),
        ]
        result = estimate_space("P1", observations, now=now)
        self.assertEqual(result.status, "available")
        self.assertGreater(result.confidence, 0)

    def test_stale_reports_return_unknown(self):
        now = datetime.now(timezone.utc)
        old = now - timedelta(hours=1)
        result = estimate_space(
            "P1",
            [ParkingObservation("P1", "available", old)],
            now=now,
            freshness_seconds=900,
        )
        self.assertEqual(result.status, "unknown")


if __name__ == "__main__":
    unittest.main()
