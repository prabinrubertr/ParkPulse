# ParkPulse: Smart Parking & Pothole Detection System

ParkPulse is a smart-city prototype that combines smartphone sensor readings, GPS coordinates, and community reports to help identify road potholes and estimate parking availability.

## Project goals

- Detect road-surface events that may indicate potholes using accelerometer readings.
- Attach GPS coordinates to reports when location data is available.
- Estimate parking availability from observed parking events and community confirmations.
- Provide a foundation for a map-based dashboard for commuters and city teams.

## Important scope note

This repository contains **educational starter code**, not a production-ready detector. Accelerometer thresholds are device- and vehicle-dependent, and a bump is not proof of a pothole. Parking availability cannot be reliably inferred from motion alone. Real deployments need consent, validation, privacy safeguards, and field testing.

## Repository structure

```text
ParkPulse/
├── docs/
│   └── project-proposal.md
├── src/
│   ├── pothole_detection.py
│   └── parking_estimation.py
├── tests/
│   └── test_starter.py
├── requirements.txt
└── .gitignore
```

## Requirements

- Python 3.10 or newer
- No third-party packages are required for the starter scripts or tests

## Run the examples

From the repository root:

```bash
python src/pothole_detection.py
python src/parking_estimation.py
python -m unittest discover -s tests -v
```

## Suggested next steps

1. Build a mobile app to collect accelerometer and GPS samples with explicit user consent.
2. Calibrate the detection logic across devices, speeds, and road conditions.
3. Store validated, privacy-minimized reports in a backend database.
4. Add duplicate-report merging and community confirmation.
5. Build a map and municipal review dashboard.
6. Evaluate precision and recall against manually verified road observations.

## Privacy and safety

Do not upload continuous location histories or personal identifiers unnecessarily. Obtain consent before collecting sensor/location data, minimize retention, secure the backend, and provide a way to correct or remove reports. Do not use unverified reports as the sole basis for road-safety or enforcement decisions.

## License

No license has been selected yet. Add a license file before permitting reuse by others.
