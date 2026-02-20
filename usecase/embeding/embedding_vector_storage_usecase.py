from repository.abstract.vector_base_repository import VectorBaseRepository
from usecase.chunking.content_chunk_usecase.chunck_builder_usecase.chunk import Chunk
from typing import List
class EmneddingVectorStorageUsecase():
    def __init__(self, vector_repository: VectorBaseRepository) -> None:
        self.vector_repository = vector_repository

    def execute(self,chunks: List[Chunk]) -> None:
        self.vector_repository.insert_chunks(chunks)
        return None