from fastapi import FastAPI, APIRouter
from service.object_storage_service import objectStorageService
from common.logger.logger import AppLogger

logger = AppLogger().get_logger()

router = APIRouter(
    prefix="/object_storage",tags=["Object Storage"])

object_service = objectStorageService()

@router.get("/file/{file_path}")
def get_file(file_path: str):
    logger.info(f"Fetching file from object storage: {file_path}")
    object_service.fetch_file(file_path)
    return {"file_id": file_path, "status": "fetched"}


  