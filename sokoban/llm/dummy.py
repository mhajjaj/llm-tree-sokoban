import random
from sokoban.llm.predictor import ActionPredictor

class RandomPredictor(ActionPredictor):
    def predict(self, state_text: str) -> str:
        return random.choice(["up", "down", "left", "right"])
