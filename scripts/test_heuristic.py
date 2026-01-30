from sokoban.env.microban_parser import load_microban
from sokoban.env.environment import SokobanEnv
from sokoban.utils.heuristics import heuristic

puzzles = load_microban("data/microban/microban.txt")
env = SokobanEnv(puzzles[0].raw_lines)

h = heuristic(env.initial_state, env.goals)
print("Initial heuristic:", h)
