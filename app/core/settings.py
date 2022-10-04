from pathlib import Path
from sys import modules

from pydantic import BaseSettings

BASE_DIR = Path(__file__).parent.resolve()


class Settings(BaseSettings):
    """Application settings."""

    ENV: str = "dev"
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    BASE_URL_: str = f"https://{HOST}:{PORT}"
    # quantity of workers for uvicorn
    WORKERS_COUNT: int = 1
    # Enable uvicorn reloading
    RELOAD: bool = False
    # Database settings
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_USER: str = "postgres"
    DB_PASS: str = "postgres"
    DB_BASE: str = "db"
    DB_ECHO: bool = False

    @property
    def BASE_URL(self) -> str:
        return self.BASE_URL_ if self.BASE_URL_.endswith("/") else f"{self.BASE_URL_}/"

    @property
    def DB_URL(self) -> str:
        """
        Assemble Database URL from settings.

        :return: Database URL.
        """

        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_BASE}"

    class Config:
        env_file = f"{BASE_DIR}/.env"
        env_file_encoding = "utf-8"
        fields = {
            "BASE_URL_": {
                "env": "BASE_URL",
            },
        }


class TestSettings(Settings):
    @property
    def DB_BASE(self):
        return f"{self.DB_BASE}_test"


if "pytest" in modules:
    settings = TestSettings()
else:
    settings = Settings()
