from dataclasses import dataclass
from typing import Literal

AtomicType = Literal[
    "heading", "paragraph", "list", "key_value", "line", "sentence"
]

@dataclass
class AtomicUnit:
    type: AtomicType
    text: str
