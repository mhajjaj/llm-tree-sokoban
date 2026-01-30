from abc import ABC, abstractmethod

class ActionPredictor(ABC):
    @abstractmethod
    def predict(self, state_text: str) -> str:
        """
        Return one of: 'up', 'down', 'left', 'right'
        """
        pass
