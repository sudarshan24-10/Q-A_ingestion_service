from repository.abstract.object_storage import ObjectStorageReopository
from usecase.object_storage_usecase.file_fetch_usecase import FileFetchUsecase
from repository.minio.object_storage import MinioStorageRepository
from repository.abstract.object_storage import ObjectStorageReopository
from config import Config
from usecase.chunking.content_chunk_usecase.chunck_factory import ChunckStratergyFactory
from usecase.embeding.embedding_usecase import EmbeddingUsecase
from repository.postgress.pg_vector_repository import PGVectorRepository
from repository.abstract.vector_base_repository import VectorBaseRepository
from usecase.embeding.embedding_vector_storage_usecase import EmneddingVectorStorageUsecase

class IngestionService:
    def __init__(self,session) -> None:
        self.bucket = Config.MINIO_BUCKET
        self.endpoint = Config.MINIO_ENDPOINT
        self.access_key = Config.MINIO_ACCESS_KEY
        self.secret_key = Config.MINIO_SECRET_KEY
        self.repo : ObjectStorageReopository = MinioStorageRepository(self.bucket, self.endpoint, self.access_key, self.secret_key, secure=False)
        self.fetch_file_usecase = FileFetchUsecase(self.repo)
        self.embedding_usecase = EmbeddingUsecase()
        self.vector_repository: VectorBaseRepository = PGVectorRepository(session)
        self.embedding_vector_storage_usecase = EmneddingVectorStorageUsecase(self.vector_repository)

    def fetch_file(self, file_path:str)-> str:
        data:str = self.fetch_file_usecase.execute(file_path)
        return data
    
    def execute_flow(self, file_path:str)-> str:
        chunck_stratergy_factory = ChunckStratergyFactory()
        data:str = self.fetch_file(file_path)
        nodes =chunck_stratergy_factory.create("structure_aware_chunking").parse(data)
        processed_chunks = self.embedding_usecase.excecute_documents(nodes)
        self.embedding_vector_storage_usecase.execute(processed_chunks)
        return "success"