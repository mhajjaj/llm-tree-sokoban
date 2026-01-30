from sokoban.env.microban_parser import load_microban
from sokoban.env.environment import SokobanEnv
from sokoban.search.astar_llm import astar_llm
from sokoban.llm.dummy import RandomPredictor
from sokoban.search.astar import reconstruct_path

puzzles = load_microban("data/microban/microban.txt")
predictor = RandomPredictor()

env = SokobanEnv(puzzles[0].raw_lines)
goal_node = astar_llm(env, predictor)

if goal_node:
    path = reconstruct_path(goal_node)
    print("Solved in", len(path))
    print(path)
else:
    print("No solution")
