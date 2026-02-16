from abc import ABC, abstractmethod
from llama_index.core.schema import BaseNode
from typing import Optional, List, Dict
class ChunckStratergy(ABC):
    @abstractmethod
    def parse(self, text:str, metadata:Optional[Dict] = None)-> List[BaseNode]:
        pass
    

