from dataclasses import dataclass
from typing import List

@dataclass
class SokobanPuzzle:
    id: int
    raw_lines: List[str]