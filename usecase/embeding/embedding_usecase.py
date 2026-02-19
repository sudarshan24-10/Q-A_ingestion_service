from infrastructure.embeddings.model.base_embedding_model import BaseEmbeddingModel
from infrastructure.embeddings.model.local_embedding_model import LocalEmbeddingModel
from usecase.chunking.content_chunk_usecase.chunck_builder_usecase.chunk import Chunk
class EmbeddingUsecase:
    def __init__(self) -> None:
        self.embedding_model: BaseEmbeddingModel = LocalEmbeddingModel()


    def execute_user_query(self, text: str, is_query: bool = False) -> list[float]:
        vector_data = self.embedding_model.embed_text(text, is_query=is_query)
        return vector_data
    
    def excecute_documents(self, chunks: list[Chunk]) -> list[Chunk]:
        texts = [chunk.text for chunk in chunks]
        vector_data = self.embedding_model.batched_embeded_text(texts)
        i=0
        for chunk, vector in zip(chunks, vector_data):
            chunk.embedding = vector
        return chunks