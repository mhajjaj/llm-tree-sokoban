from sokoban.llm.predictor import ActionPredictor
from sokoban.env.environment import ACTIONS
from sokoban.utils.heuristics import heuristic


class HeuristicPredictor(ActionPredictor):
    def __init__(self, env):
        self.env = env

    def predict(self, state_text: str, state):
        best_action = None
        best_h = float("inf")

        for action in ACTIONS:
            next_state, ok = self.env.step(state, action)
            if not ok:
                continue

            h = heuristic(next_state, self.env.goals)

            if h < best_h:
                best_h = h
                best_action = action

        return best_action if best_action is not None else "up"
