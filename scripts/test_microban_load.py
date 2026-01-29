import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from sokoban.env.microban_parser import load_microban

puzzles = load_microban("data/microban/microban.txt")

print(f"Loaded {len(puzzles)} puzzles")

for p in puzzles[:3]:
    print(f"\nPuzzle {p.id}")
    for line in p.raw_lines:
        print(line)
