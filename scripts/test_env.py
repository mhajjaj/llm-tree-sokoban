from sokoban.env.microban_parser import load_microban
from sokoban.env.environment import SokobanEnv

puzzles = load_microban("data/microban/microban.txt")

env = SokobanEnv(puzzles[0].raw_lines)
state = env.initial_state

print("Initial state:")
print("\n".join(env.render(state)))

for action in ["right", "down", "left", "up"]:
    next_state, ok = env.step(state, action)
    print(f"\nAction: {action}, valid: {ok}")
    if ok:
        print("\n".join(env.render(next_state)))
