from typing import List, Set, Tuple
from sokoban.env.state import SokobanState, Position

class SokobanEnv:
    def __init__(self, raw_lines: List[str]):
        self.height = len(raw_lines)
        self.width = max(len(line) for line in raw_lines)

        self.walls: Set[Position] = set()
        self.goals: Set[Position] = set()
        self.initial_state = self._parse(raw_lines)

    def _parse(self, lines: List[str]) -> SokobanState:
        boxes = set()
        player = None

        for y, line in enumerate(lines):
            for x, c in enumerate(line):
                pos = (x, y)

                if c == "#":
                    self.walls.add(pos)
                elif c == ".":
                    self.goals.add(pos)
                elif c == "$":
                    boxes.add(pos)
                elif c == "@":
                    player = pos
                elif c == "*":
                    boxes.add(pos)
                    self.goals.add(pos)
                elif c == "+":
                    player = pos
                    self.goals.add(pos)

        if player is None:
            raise ValueError("Invalid puzzle: no player found")

        return SokobanState(player=player, boxes=frozenset(boxes))
    
    def step(self, state: SokobanState, action: str):
        if action not in ACTIONS:
            return None, False

        dx, dy = ACTIONS[action]
        px, py = state.player
        next_pos = (px + dx, py + dy)

        # Wall in front
        if next_pos in self.walls:
            return None, False

        boxes = set(state.boxes)

        # Moving into box
        if next_pos in boxes:
            box_next = (next_pos[0] + dx, next_pos[1] + dy)

            # Box blocked
            if box_next in self.walls or box_next in boxes:
                return None, False

            # Push box
            boxes.remove(next_pos)
            boxes.add(box_next)

        # Move player
        new_state = SokobanState(
            player=next_pos,
            boxes=frozenset(boxes)
        )

        return new_state, True

    def is_goal(self, state: SokobanState) -> bool:
        return state.boxes.issubset(self.goals)

    def render(self, state: SokobanState) -> List[str]:
        grid = [[" " for _ in range(self.width)] for _ in range(self.height)]

        for (x, y) in self.walls:
            grid[y][x] = "#"

        for (x, y) in self.goals:
            grid[y][x] = "."

        for (x, y) in state.boxes:
            grid[y][x] = "*" if (x, y) in self.goals else "$"

        px, py = state.player
        grid[py][px] = "+" if (px, py) in self.goals else "@"

        return ["".join(row) for row in grid]

ACTIONS = {
    "up": (0, -1),
    "down": (0, 1),
    "left": (-1, 0),
    "right": (1, 0),
}
