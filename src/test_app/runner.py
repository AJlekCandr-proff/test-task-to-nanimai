import uvicorn

from src.test_app.application.config import settings


if __name__ == "__main__":
    uvicorn.run(
        app=settings.APP.APP_DIRECTORY,
        host=settings.APP.HOST,
        port=settings.APP.PORT,
        reload=bool(settings.APP.RELOADED),
    )
