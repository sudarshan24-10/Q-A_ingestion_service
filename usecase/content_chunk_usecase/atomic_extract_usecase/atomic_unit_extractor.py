import re
from typing import List
from usecase.content_chunk_usecase.atomic_extract_usecase.atomic_unit import AtomicUnit


class AtomicUnitExtractor:

    BULLET = re.compile(r"^(\•|\-|\*|\d+\.)\s+")
    KEY_VALUE = re.compile(r"^[A-Za-z ].+:\s+.+")

    def extract(self, text: str) -> List[AtomicUnit]:
        blocks = self._split_blocks_with_internal_headings(text)
        units: List[AtomicUnit] = []

        for block in blocks:
            lines = [l.strip() for l in block.split("\n") if l.strip()]
            if not lines:
                continue
            if self._is_heading(lines):
                units.append(AtomicUnit("heading", lines[0]))
                continue


            if all(self.BULLET.match(l) for l in lines):
                units.append(AtomicUnit("list", "\n".join(lines)))
                continue

  
            if all(self.KEY_VALUE.match(l) for l in lines):
                units.append(AtomicUnit("key_value", "\n".join(lines)))
                continue

            if len(lines) == 1:
                split_units = self._split_heading_and_paragraph(lines[0])
                if split_units:
                    units.extend(split_units)
                    continue
            if len(lines) > 1:
                units.append(AtomicUnit("paragraph", " ".join(lines)))
                continue


            units.append(AtomicUnit("line", lines[0]))

        return units

    def _split_blocks_with_internal_headings(self, text: str) -> List[str]:
        
        final_blocks: List[str] = []

        for block in text.split("\n\n"):
            lines = block.split("\n")
            current: List[str] = []

            for line in lines:
                if self._looks_like_heading(line) and current:
                    final_blocks.append("\n".join(current))
                    current = [line.strip()]
                else:
                    current.append(line.strip())

            if current:
                final_blocks.append("\n".join(current))

        return final_blocks

    def _split_heading_and_paragraph(self, line: str) -> List[AtomicUnit] | None:
    
        tokens = line.split(" ")


        for i in (2, 3):
            if len(tokens) <= i:
                continue

            heading_candidate = " ".join(tokens[:i])
            rest = " ".join(tokens[i:]).strip()

            if self._looks_like_heading(heading_candidate) and rest:
                return [
                    AtomicUnit("heading", heading_candidate),
                    AtomicUnit("paragraph", rest),
                ]

        return None

    def _is_heading(self, lines: List[str]) -> bool:
        if len(lines) != 1:
            return False
        return self._looks_like_heading(lines[0])

    def _looks_like_heading(self, line: str) -> bool:

        line = line.strip()

        if not line:
            return False

        if len(line) > 80:
            return False

        if line.endswith("."):
            return False

        if "http" in line.lower() or "@" in line:
            return False

        if line.islower():
            return False

        if line.startswith(("(", "-", "•")):
            return False

        # Avoid sentence fragments
        if line.count(" ") > 6 and not line.isupper():
            return False

        return True
