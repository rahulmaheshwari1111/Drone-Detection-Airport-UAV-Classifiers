from fastapi import FastAPI
from app.core.config import settings
from app.core.logging import configure_logging
from app.api.routes.health import router as health_router
from app.api.routes.sensors import router as sensors_router
from app.api.routes.tracks import router as tracks_router
from app.api.routes.classify import router as classify_router
from app.api.routes.alerts import router as alerts_router


def create_app() -> FastAPI:
    configure_logging()
    app = FastAPI(title=settings.app_name, debug=settings.debug)
    app.include_router(health_router)
    app.include_router(sensors_router)
    app.include_router(tracks_router)
    app.include_router(classify_router)
    app.include_router(alerts_router)
    return app


app = create_app()
