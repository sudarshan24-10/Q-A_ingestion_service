from abc import ABC, abstractmethod
from typing import List, Optional
from usecase.chunking.content_chunk_usecase.chunck_builder_usecase.chunk import Chunk

class VectorBaseRepository(ABC):
    @abstractmethod
    def insert_chunks(self, chunks: List[Chunk]) -> None:
        pass

    @abstractmethod
    def similarity_search(self, query_vector: List[float], top_k: int, document_id: Optional[str] = None) -> List[Chunk]:
        pass