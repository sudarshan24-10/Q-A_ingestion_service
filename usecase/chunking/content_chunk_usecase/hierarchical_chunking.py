from usecase.chunking.content_chunk_usecase.chunck_stratergy import ChunckStratergy
from llama_index.core import Document
from llama_index.core.node_parser import HierarchicalNodeParser
from typing import Optional, List, Dict
from llama_index.core.schema import BaseNode
class HierarchicalChunkingStrategy(ChunckStratergy):
    def __init__(self, chunck_size: List[int] | None = None, chunk_overlap: int = 10) -> None:
        self.chunck_size = chunck_size or [100,50]
        self.chunk_overlap = chunk_overlap
        self.parser = HierarchicalNodeParser.from_defaults(chunk_sizes=self.chunck_size, chunk_overlap=self.chunk_overlap)
        
    def parse(self, text:str, metadata:Optional[Dict] = None)-> List[BaseNode]:
        document = Document(text = text, metadata=metadata or {})
        nodes = self.parser.get_nodes_from_documents([document])
        return nodes
        