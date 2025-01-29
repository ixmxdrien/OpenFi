from pydantic import BaseModel
from functools import lru_cache

class Settings(BaseModel):
    APP_NAME: str = "OpenFi"
    MONGODB_URL: str = "mongodb://localhost:27017"
    JWT_SECRET_KEY: str = "your-secret-key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()