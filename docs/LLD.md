# Low-Level Design

## Core services

### Sensor Gateway
- receives sensor payloads over HTTP, gRPC, or queue
- normalizes timestamps and coordinates
- validates schema
- publishes normalized detections

### Track Association Service
- matches detections to active tracks
- uses distance and recency gates
- can evolve into Hungarian assignment

### Track Engine
- maintains tentative, confirmed, stale, dropped track lifecycle
- updates position and velocity
- persists current state

### Feature Service
Baseline features:
- mean_speed
- heading_variability
- jerk
- thermal_signature
- rcs_mean

Extended features:
- acceleration_std
- hover_ratio
- path_curvature
- rcs_variance
- micro_doppler_entropy
- rf_presence

### Classification Service
- loads active model
- classifies bird, drone, decoy, unknown
- returns confidence and probabilities

### Threat Scoring Service
- transforms class outputs into operational severity
- can trigger alert creation

## Database entities

- sensors
- detections
- tracks
- track_features
- model_versions
- classifications
- alerts
- incidents

## Starter limitations

- nearest-distance association instead of Kalman plus assignment
- manual classification endpoint instead of automatic feature-to-class pipeline
- no Redis cache yet
- no streaming consumer yet
- no auth yet
