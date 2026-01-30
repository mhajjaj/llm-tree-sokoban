from sokoban.env.microban_parser import load_microban
from sokoban.env.environment import SokobanEnv
from sokoban.search.astar import astar

puzzles = load_microban("data/microban/microban.txt")

for idx in range(5):
    env = SokobanEnv(puzzles[idx].raw_lines)
    solution = astar(env)

    print(f"Puzzle {idx}:")
    if solution:
        print("Solved in", len(solution), "steps")
        print(solution)
    else:
        print("No solution found")
