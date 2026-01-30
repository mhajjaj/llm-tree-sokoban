from typing import Set, Tuple
from sokoban.env.state import SokobanState, Position

def is_corner(pos: Position, walls: Set[Position]) -> bool:
    x, y = pos
    wall_pairs = [
        ((x-1, y), (x, y-1)),
        ((x+1, y), (x, y-1)),
        ((x-1, y), (x, y+1)),
        ((x+1, y), (x, y+1)),
    ]
    return any(a in walls and b in walls for a, b in wall_pairs)


def has_deadlock(
    state: SokobanState,
    walls: Set[Position],
    goals: Set[Position],
) -> bool:
    for box in state.boxes:
        if box not in goals and is_corner(box, walls):
            return True
    return False
