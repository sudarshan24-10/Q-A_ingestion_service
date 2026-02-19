from repository.abstract.vector_base_repository import VectorBaseRepository
from typing import List, Optional
from usecase.chunking.content_chunk_usecase.chunck_builder_usecase.chunk import Chunk
class PGVectorRepository(VectorBaseRepository):
    def __init__(self, session) -> None:
        self.session = session
        pass

    def insert_chunks(self, chunks: List[Chunk]) -> None:
        pass

    def similarity_search(self, query_vector: List[float], top_k: int, document_id: Optional[str] = None) -> List[Chunk]:
        pass