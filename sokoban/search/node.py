from dataclasses import dataclass
from sokoban.env.state import SokobanState

@dataclass
class SearchNode:
    state: SokobanState
    parent: "SearchNode | None"
    action: str | None
    g: int  # cost so far
    h: int  # heuristic
    expansions: int = 0
