from repository.abstract.object_storage import ObjectStorageReopository
from usecase.object_storage_usecase.file_fetch_usecase import FileFetchUsecase
from repository.minio.object_storage import MinioStorageRepository
from repository.abstract.object_storage import ObjectStorageReopository
from config import Config
from usecase.content_chunk_usecase.chunck_factory import ChunckStratergyFactory

class objectStorageService:
    def __init__(self) -> None:
        self.bucket = Config.MINIO_BUCKET
        self.endpoint = Config.MINIO_ENDPOINT
        self.access_key = Config.MINIO_ACCESS_KEY
        self.secret_key = Config.MINIO_SECRET_KEY
        self.repo : ObjectStorageReopository = MinioStorageRepository(self.bucket, self.endpoint, self.access_key, self.secret_key, secure=False)
        self.fetch_file_usecase = FileFetchUsecase(self.repo)
        

    def fetch_file(self, file_path:str)-> str:
        chunck_stratergy_factory = ChunckStratergyFactory()
        data:str = self.fetch_file_usecase.execute(file_path)
        print(data)
        nodes =chunck_stratergy_factory.create("structure_aware_chunking").parse(data)
        for i, node in enumerate(nodes, start=1):
            print(f"\n--- CHUNK {i} ---")
            print(node)
            print("Metadata:", node.metadata)
        return data