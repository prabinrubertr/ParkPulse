# Project Proposal: ParkPulse
## Smart Parking and Pothole Detection System

### 1. Abstract

ParkPulse is a proposed smart-city application that aims to make urban travel safer and more convenient by crowdsourcing information about road potholes and estimating nearby parking availability. The system uses smartphone sensors such as accelerometers, GPS coordinates, and user confirmations to create location-based reports. These reports can be reviewed, merged, and displayed on a map for commuters and authorized municipal teams. The initial implementation is a prototype: its detection rules and parking estimates must be validated with real-world observations before practical deployment.

### 2. Problem statement

Potholes can damage vehicles and create hazards for cyclists and motorcyclists, while drivers often spend time searching for parking. Road-condition reports may be outdated, and parking information can change quickly. A low-cost system using smartphones and community participation could help collect timely observations, but sensor noise, inaccurate location data, duplicate reports, and uncertain parking signals must be addressed.

### 3. Proposed solution

ParkPulse will provide two complementary features:

- **Pothole reporting:** identify candidate impact events from accelerometer samples, associate them with GPS coordinates when available, and submit them for validation.
- **Parking estimation:** combine parking-event observations and community confirmations into an estimate with a confidence score and timestamp.

A map-based interface can display confirmed pothole reports and recent parking estimates. A municipal dashboard may help authorized staff review, prioritize, and update road reports.

### 4. Objectives

1. Design a simple, modular software prototype.
2. Demonstrate basic accelerometer-based event detection.
3. Represent geolocated road reports with timestamps and confidence.
4. Demonstrate a transparent, rule-based parking estimate.
5. Encourage validation, privacy protection, and responsible handling of uncertain data.
6. Define a path toward mobile, backend, and map integration.

### 5. System workflow

1. A user opts in to sensor and location collection.
2. The mobile client samples motion data and, where permitted, GPS.
3. The detector filters or evaluates acceleration magnitude and flags candidate events.
4. The client creates a candidate report with time, location, and sensor-derived score.
5. Duplicate reports are grouped and users or reviewers confirm the location.
6. Parking observations and confirmations are aggregated with freshness and confidence indicators.
7. A map displays reports and clearly labels estimates as confirmed, likely, or uncertain.

### 6. Proposed architecture

- **Mobile client:** sensor sampling, location permission handling, user reporting, and map view.
- **Detection module:** acceleration magnitude calculation, thresholding, and candidate-event generation.
- **Parking module:** event aggregation, confirmation weighting, and confidence estimation.
- **Backend (future work):** authenticated API, database, duplicate merging, moderation, and audit logs.
- **Dashboard (future work):** map layers, report status, filters, and authorized review tools.

### 7. Technology stack

- Python for the initial algorithm prototype.
- Smartphone GPS and accelerometer APIs for future mobile integration.
- A database such as PostgreSQL with PostGIS for a future geospatial backend.
- A map SDK or open mapping library for visualization.
- A REST API for communication between mobile clients and the backend.

These technologies are proposals and are not all implemented in the current starter repository.

### 8. Methodology

**Pothole candidate detection:** compute acceleration magnitude from three axes, subtract the estimated gravity component if calibration permits, and identify short-duration peaks above a configurable threshold. Record a candidate event rather than asserting that a pothole has been proven. Future versions should use filtering, orientation correction, speed/context features, and a trained classifier evaluated against labeled data.

**Parking estimation:** ingest observations such as a user confirming a free space or a vehicle leaving a space. Weight recent observations more strongly than old ones, and expose the evidence count and last-observed time. The current starter module demonstrates simple confirmation-based aggregation; it does not automatically detect occupied curb spaces from a phone's motion.

**Validation:** collect a consent-based, manually labeled test set; compare candidate reports with verified road conditions; measure precision, recall, false positives, and location error; and test parking estimates against ground truth at different times of day.

### 9. Expected outcomes

- A documented Python prototype for candidate pothole events.
- A small parking-estimation module with confidence and freshness metadata.
- A project proposal and reproducible run instructions.
- A foundation for a mobile application, backend, map, and review dashboard.
- A defined testing plan that makes the limitations of crowdsourced data explicit.

### 10. Limitations and risks

- Accelerometer signals vary with phone placement, vehicle suspension, speed, and road surface.
- Speed bumps, potholes, braking, and other impacts can produce similar signals.
- GPS may be inaccurate in dense urban areas.
- Parking status changes quickly; stale reports can mislead drivers.
- Crowd participation can be uneven, and reports may be accidental or malicious.
- Continuous sensor or location collection can expose sensitive movement patterns.

Mitigations include opt-in collection, data minimization, report expiry, duplicate detection, confidence labels, manual review, and testing before deployment.

### 11. Future enhancements

- Native Android/iOS sensor collection.
- Secure API and geospatial database.
- Map-based public view and authorized municipal dashboard.
- Clustering of duplicate pothole reports.
- Machine-learning classification trained on labeled sensor data.
- Parking integration with cameras or parking infrastructure only where legally permitted and privacy-protected.
- Notifications for verified hazards and accessibility-aware routing.

### 12. Conclusion

ParkPulse explores how crowdsourced smartphone data can support safer roads and more efficient parking searches. The proposed modular design separates candidate pothole detection from parking estimation and emphasizes confidence, freshness, and validation. The starter implementation is intended for learning and experimentation; real-world use requires rigorous testing, consent, security, and responsible review.
