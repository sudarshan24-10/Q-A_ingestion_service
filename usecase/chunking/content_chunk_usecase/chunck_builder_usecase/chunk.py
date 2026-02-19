from dataclasses import dataclass
from typing import Dict

@dataclass
class Chunk:
    text: str
    metadata: Dict
    embedding: list[float]
