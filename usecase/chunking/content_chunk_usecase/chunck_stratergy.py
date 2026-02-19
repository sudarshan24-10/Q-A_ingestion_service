from abc import ABC, abstractmethod
from llama_index.core.schema import BaseNode
from typing import Optional, List, Dict, Sequence
from usecase.chunking.content_chunk_usecase.chunck_builder_usecase.chunk import Chunk
class ChunckStratergy(ABC):
    @abstractmethod
    def parse(self, text:str, metadata:Optional[Dict] = None)-> List[Chunk]:
        pass
    

