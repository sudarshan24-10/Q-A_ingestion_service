from fastapi import FastAPI
import uvicorn
from routes.object_storage_routes import router as object_storage_router
from common.logger.logger import AppLogger

def create_app() -> FastAPI:
    app = FastAPI(
        title="Data Ingestion Service",
        description="A service for ingesting and processing data.",
        version="0.0.1",
        docs_url="/docs",
        redoc_url="/redoc"
    )

    @app.get("/health", tags=["Health"])
    async def health_check():
        return {"status": "Ok"}
    app.include_router(object_storage_router)
    logger = AppLogger().get_logger()
    logger.info("Application has started successfully.")
    return app


app = create_app()


if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host="localhost",
        port=8000,
        reload=True
    )
