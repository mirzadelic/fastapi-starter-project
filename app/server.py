import uvicorn
from core.settings import settings


def main() -> None:
    """Entrypoint of the application."""
    uvicorn.run(
        "core.app:get_app",
        workers=settings.WORKERS_COUNT,
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.RELOAD,
        factory=True,
    )


if __name__ == "__main__":
    main()
