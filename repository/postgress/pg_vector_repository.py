import uuid
from repository.abstract.vector_base_repository import VectorBaseRepository
from typing import List, Optional
from usecase.chunking.content_chunk_usecase.chunck_builder_usecase.chunk import Chunk
from repository.model.embedding_vector_model import DocumentChunkModel
class PGVectorRepository(VectorBaseRepository):
    def __init__(self, session) -> None:
        self.session = session

    def insert_chunks(self, chunks: List[Chunk], document_id: Optional[str] = None) -> None:
        try:
            i = 1
            for chunk in chunks:
                db_chunk = DocumentChunkModel(
                    id = uuid.uuid4(),
                    document_id=uuid.uuid4(),
                    chunk_index=i,
                    chunk_text=chunk.text,
                    embedding=chunk.embedding,
                    metadata_json=chunk.metadata
                )
                self.session.add(db_chunk)
                i+=1
            self.session.commit()
                
        except Exception as e:
            self.session.rollback()
            raise e

        

    def similarity_search(self, query_vector: List[float], top_k: int, document_id: Optional[str] = None) -> List[Chunk]:
        return []
        