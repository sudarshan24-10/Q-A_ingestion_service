from fastapi import FastAPI, APIRouter
from service.object_storage_service import objectStorageService
from service.ingestion_service import IngestionService
from common.logger.logger import AppLogger
from fastapi import Depends
from database.postgres import get_db


logger = AppLogger().get_logger()

router = APIRouter(
    prefix="/object_storage",tags=["Object Storage"])


@router.get("/file/{file_path}")
def get_file(file_path: str, session=Depends(get_db)):
    object_service = objectStorageService()
    logger.info(f"Fetching file from object storage: {file_path}")
    object_service.fetch_file(file_path)
    ingestion_service = IngestionService(session)
    ingestion_service.execute_flow(file_path)
    return {"file_id": file_path, "status": "fetched"}


  