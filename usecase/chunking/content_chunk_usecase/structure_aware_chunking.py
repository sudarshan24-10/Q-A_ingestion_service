from typing import List
from usecase.chunking.content_chunk_usecase.chunck_stratergy import ChunckStratergy
from usecase.chunking.content_chunk_usecase.chunck_builder_usecase.chunk import Chunk
from usecase.chunking.content_chunk_usecase.atomic_extract_usecase.atomic_unit_extractor import AtomicUnitExtractor
from usecase.chunking.content_chunk_usecase.chunck_builder_usecase.chunk_builder import ChunkBuilder
from typing import Optional, Dict
from usecase.chunking.content_chunk_usecase.chunck_builder_usecase.text_normalizer import normalize_text

class StructureAwareChunkingStrategy(ChunckStratergy):
    def __init__(self):
        self.extractor = AtomicUnitExtractor()
        self.builder = ChunkBuilder()

    def parse(self, text: str, metadata: Optional[Dict] = None) -> List[Chunk]:
        text = normalize_text(text)
        atomic_units = self.extractor.extract(text)
        return self.builder.build(atomic_units)
