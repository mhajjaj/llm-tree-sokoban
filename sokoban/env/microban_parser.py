from typing import List
from sokoban.env.puzzle import SokobanPuzzle

def load_microban(path: str) -> List[SokobanPuzzle]:
    puzzles = []
    current = []
    puzzle_id = 0

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")

            if line.strip() == "":
                if current:
                    puzzles.append(
                        SokobanPuzzle(
                            id=puzzle_id,
                            raw_lines=current
                        )
                    )
                    puzzle_id += 1
                    current = []
            else:
                current.append(line)

        # last puzzle
        if current:
            puzzles.append(
                SokobanPuzzle(
                    id=puzzle_id,
                    raw_lines=current
                )
            )

    return puzzles
