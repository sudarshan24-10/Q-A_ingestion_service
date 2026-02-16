
from usecase.content_chunk_usecase.chunck_stratergy import ChunckStratergy
from usecase.content_chunk_usecase.hierarchical_chunking import HierarchicalChunkingStrategy
from usecase.content_chunk_usecase.structure_aware_chunking import StructureAwareChunkingStrategy
class ChunckStratergyFactory:
    def __init__(self):
        self.stratergy:dict[str,ChunckStratergy] ={
            "hierarchical":HierarchicalChunkingStrategy(),
            "structure_aware_chunking": StructureAwareChunkingStrategy()}

    def create(self,chunk_stratergy:str):
        if chunk_stratergy in self.stratergy:
            return self.stratergy[chunk_stratergy]
        else:
            raise ValueError(f"Chunk stratergy {chunk_stratergy} not found")

    