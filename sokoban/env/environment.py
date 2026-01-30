from typing import List, Set, Tuple
from sokoban.env import state
from sokoban.env.state import SokobanState, Position
from sokoban.utils.deadlock import has_deadlock


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
                pos = (y, x)

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
        pr, pc = state.player
        dr, dc = ACTIONS[action]
        next_pos = (pr + dr, pc + dc)

        # Wall in front
        if next_pos in self.walls:
            return None, False

        boxes = set(state.boxes)

        # Moving into box
        if next_pos in boxes:
            box_next = (next_pos[0] + dr, next_pos[1] + dc)

            # Box blocked
            if box_next in self.walls or box_next in boxes:
                return None, False

            # Push box
            boxes.remove(next_pos)
            boxes.add(box_next)

        # Move player
        new_state = SokobanState(player=next_pos, boxes=frozenset(boxes))

        return new_state, True

    def is_goal(self, state: SokobanState) -> bool:
        return state.boxes.issubset(self.goals)

    def render(self, state: SokobanState) -> List[str]:
        grid = [[" " for _ in range(self.width)] for _ in range(self.height)]

        # walls
        for r, c in self.walls:
            grid[r][c] = "#"

        # goals
        for r, c in self.goals:
            grid[r][c] = "."

        # boxes
        for r, c in state.boxes:
            grid[r][c] = "*" if (r, c) in self.goals else "$"

        # player
        pr, pc = state.player
        grid[pr][pc] = "+" if (pr, pc) in self.goals else "@"

        return ["".join(row) for row in grid]

    def is_deadlock(self, state: SokobanState) -> bool:
        return has_deadlock(state, self.walls, self.goals)

    def to_text(self, state):
        grid = [[" " for _ in range(self.width)] for _ in range(self.height)]

        # walls
        for r, c in self.walls:
            grid[r][c] = "#"

        # goals
        for r, c in self.goals:
            grid[r][c] = "."

        # boxes
        for r, c in state.boxes:
            if (r, c) in self.goals:
                grid[r][c] = "*"
            else:
                grid[r][c] = "$"

        # player
        pr, pc = state.player
        if (pr, pc) in self.goals:
            grid[pr][pc] = "+"
        else:
            grid[pr][pc] = "@"

        return "\n".join("".join(row) for row in grid)


ACTIONS = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
