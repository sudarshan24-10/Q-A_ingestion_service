from abc import ABC, abstractmethod


class BaseEmbeddingModel(ABC):
    @abstractmethod
    def embed_text(self, text: str, is_query: bool = False) -> list[float]:
        pass

    @abstractmethod
    def batched_embeded_text(self, texts: list[str]) -> list[list[float]]:
        pass

    @abstractmethod
    def get_embedding_dimension(self) -> int:
        pass