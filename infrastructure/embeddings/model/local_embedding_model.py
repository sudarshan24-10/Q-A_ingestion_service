from typing import List
import torch
from sentence_transformers import SentenceTransformer

from infrastructure.embeddings.model.base_embedding_model import BaseEmbeddingModel


class LocalEmbeddingModel(BaseEmbeddingModel):


    def __init__(self, model_name: str = "intfloat/e5-large-v2"):
        self.model_name = model_name
        device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"Loading embedding model on {device}...")
        self.model = SentenceTransformer(self.model_name, device=device)


    def embed_text(self, text:str, is_query: bool = False) -> List[float]:
        prefix = "query: " if is_query else "passage: "
        formatted_text = prefix + text
        embedding = self.model.encode(
            formatted_text,
            convert_to_numpy=True,
            normalize_embeddings=True
        )

        return embedding.tolist()
    
    def batched_embeded_text(self, texts: List[str]) -> List[List[float]]:
        formatted_texts = ["passage: " + text for text in texts]

        embeddings = self.model.encode(
            formatted_texts,
            convert_to_numpy=True,
            normalize_embeddings=True,
            batch_size=32,
            show_progress_bar=False,
        )
        return embeddings.tolist()

    
    def get_embedding_dimension(self) -> int:
        sample_embedding = self.model.encode("passage: text", convert_to_numpy=True)
        return len(sample_embedding)