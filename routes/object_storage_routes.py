from fastapi import FastAPI, APIRouter
from service.object_storage_service import objectStorageService
from service.ingestion_service import IngestionService
from common.logger.logger import AppLogger
from database.postgres import PostgresDB

logger = AppLogger().get_logger()

router = APIRouter(
    prefix="/object_storage",tags=["Object Storage"])

db = PostgresDB()

@router.get("/file/{file_path}")
def get_file(file_path: str):
    session = db.get_session()
    object_service = objectStorageService()
    logger.info(f"Fetching file from object storage: {file_path}")
    object_service.fetch_file(file_path)
    ingestion_service = IngestionService()
    ingestion_service.execute_flow(file_path)
    return {"file_id": file_path, "status": "fetched"}


  