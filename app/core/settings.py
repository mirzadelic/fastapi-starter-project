from pathlib import Path

from pydantic import BaseSettings

BASE_DIR = Path(__file__).parent.resolve()


class Settings(BaseSettings):
    """Application settings."""

    host: str = "127.0.0.1"
    port: int = 8000
    base_url_: str = f"https://{host}:{port}"
    # quantity of workers for uvicorn
    workers_count: int = 1
    # Enable uvicorn reloading
    reload: bool = False
    # Database settings
    db_host: str = "localhost"
    db_port: int = 5432
    db_user: str = ""
    db_pass: str = ""
    db_base: str = ""
    db_echo: bool = False

    @property
    def base_url(self) -> str:
        return self.base_url_ if self.base_url_.endswith("/") else f"{self.base_url_}/"

    @property
    def db_url(self) -> str:
        """
        Assemble Database URL from settings.

        :return: Database URL.
        """

        return f"postgresql+asyncpg://{self.db_user}:{self.db_pass}@{self.db_host}:{self.db_port}/{self.db_base}"

    class Config:
        env_file = f"{BASE_DIR}/.env"
        env_file_encoding = "utf-8"
        fields = {
            'base_url_': {
                'env': 'BASE_URL',
            }
        }


settings = Settings()
