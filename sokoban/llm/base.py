from abc import ABC, abstractmethod
from sokoban.env.state import SokobanState
from typing import Literal

class ActionPredictor(ABC):
    @abstractmethod
    def predict(self, state_text: str, state: SokobanState) -> Literal["up","down","left","right"]:
        pass
