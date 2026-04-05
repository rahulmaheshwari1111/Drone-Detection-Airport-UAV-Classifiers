from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "airport-uav-classifier"
    app_env: str = "dev"
    debug: bool = True
    database_url: str = "postgresql+psycopg://postgres:postgres@localhost:5432/airport_uav"
    model_artifact_path: str = "artifacts/svm_uav_model.joblib"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
