# Airport UAV Threat Classification System

A real-time multimodal aerial object classification starter for airport perimeter surveillance.

## Why this project matters

Airports increasingly face low-altitude airspace intrusions from small UAVs. This project demonstrates how a multimodal surveillance pipeline can classify drones, birds, decoys, and unknown targets in near real time using motion, thermal, and radar-style features.

## What it does

- ingests aerial detections from sensors
- creates or associates tracks
- exposes a baseline classification API
- stores track, detection, classification, and alert data in PostgreSQL
- ships with a Dockerized local setup
- includes architecture and low-level design docs

## Core classification baseline

This starter keeps a lightweight paper-aligned baseline built around:

- mean speed
- heading variability
- jerk
- thermal signature
- radar cross-section (RCS)

That makes it useful as a research-inspired engineering starter before you layer in production-grade tracking, fusion, and model management.

## Tech stack

- FastAPI
- PostgreSQL
- SQLAlchemy
- scikit-learn
- Docker

## Repository structure

```text
airport-uav-classifier/
├── app/
├── artifacts/
├── docs/
├── scripts/
├── tests/
├── .env.example
├── .gitignore
├── CONTRIBUTING.md
├── docker-compose.yml
├── Dockerfile
├── LICENSE
├── README.md
├── requirements.txt
└── ROADMAP.md
```

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python scripts/init_db.py
uvicorn app.main:app --reload
```

## Run with Docker

```bash
cp .env.example .env
docker compose up --build
```

## Seed one sensor

```sql
INSERT INTO sensors (sensor_code, sensor_type, location_name, config_json)
VALUES (
  'radar-north-01',
  'radar',
  'North Perimeter',
  '{}'::jsonb
);
```

## Health endpoints

- `GET /health/live`
- `GET /health/ready`

## Main endpoints

- `POST /detections`
- `GET /tracks`
- `POST /classifications`
- `GET /alerts`

## Example classification request

```json
{
  "track_id": "trk-0001842",
  "mean_speed": 11.8,
  "heading_variability": 0.18,
  "jerk": 0.32,
  "thermal_signature": 0.77,
  "rcs_mean": 0.12
}
```

## Example curl

```bash
curl -X POST http://127.0.0.1:8000/classifications \
  -H "Content-Type: application/json" \
  -d '{
    "track_id":"trk-0001842",
    "mean_speed":11.8,
    "heading_variability":0.18,
    "jerk":0.32,
    "thermal_signature":0.77,
    "rcs_mean":0.12
  }'
```

## Docs

- `docs/ARCHITECTURE.md`
- `docs/LLD.md`

## Next improvements

- Kalman-based tracking
- feature extraction from live track windows
- automatic alert creation
- Redis live state
- Kafka or NATS ingestion
- WebSocket live updates
- real trained model artifact

## Disclaimer

This is a research-inspired engineering starter and not a validated operational aviation safety system.
