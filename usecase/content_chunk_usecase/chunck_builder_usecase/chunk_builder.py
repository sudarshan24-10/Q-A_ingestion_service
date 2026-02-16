from typing import List
from usecase.content_chunk_usecase.chunck_builder_usecase.chunk import Chunk
from usecase.content_chunk_usecase.atomic_extract_usecase.atomic_unit import AtomicUnit

class ChunkBuilder:
    MAX_CHARS = 500

    def build(self, units: List[AtomicUnit]) -> List[Chunk]:
        chunks: List[Chunk] = []
        buffer: List[str] = []
        current_section = None

        def flush():
            nonlocal buffer
            if buffer:
                chunks.append(
                    Chunk(
                        text="\n".join(buffer),
                        metadata={"section": current_section}
                    )
                )
                buffer = []

        for unit in units:
            if unit.type == "heading":
                flush()
                current_section = unit.text
                buffer.append(unit.text)
                continue

            candidate = "\n".join(buffer + [unit.text])
            if len(candidate) > self.MAX_CHARS:
                flush()

            buffer.append(unit.text)

        flush()
        return chunks
