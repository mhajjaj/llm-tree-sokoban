from sokoban.env.state import SokobanState, Position
from typing import Set

def manhattan(a: Position, b: Position) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def heuristic(state: SokobanState, goals: Set[Position]) -> int:
    cost = 0
    for box in state.boxes:
        cost += min(manhattan(box, g) for g in goals)
    return cost

