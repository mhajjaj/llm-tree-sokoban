from dataclasses import dataclass
from typing import FrozenSet, Tuple

Position = Tuple[int, int]

@dataclass(frozen=True)
class SokobanState:
    player: Position
    boxes: FrozenSet[Position]
