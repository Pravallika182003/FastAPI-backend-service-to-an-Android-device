from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./app.db"
    SECRET_KEY: str = "Myservice123"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    FIREBASE_CREDENTIALS_PATH: str = ""
    DEFAULT_DEVICE_TOKEN: str = ""

    class Config:
        env_file = ".env"
settings=Settings()
