from sokoban.env.microban_parser import load_microban
from sokoban.env.environment import SokobanEnv

puzzles = load_microban("data/microban/microban.txt")
env = SokobanEnv(puzzles[0].raw_lines)

state = env.initial_state
print("Deadlock at start:", env.is_deadlock(state))

# Try pushing box into corner manually if possible
