import os
import requests
from sokoban.llm.base import ActionPredictor
from sokoban.env.state import SokobanState
from typing import Literal
from dotenv import load_dotenv

ALLOWED = {"up", "down", "left", "right"}

load_dotenv()
OPENROUTER_KEY = os.environ["OPENROUTER_API_KEY"]

class LLMPredictor(ActionPredictor):
    def __init__(self, model: str = "mistral-7b-chat"):
        self.model = model
        self.api_url = "https://openrouter.ai/api/v1/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {OPENROUTER_KEY}",
            "Content-Type": "application/json"
        }

    def predict(self, state_text: str, state: SokobanState) -> Literal["up","down","left","right"]:
        prompt = f"""
You are solving Sokoban.
Choose ONE best action from: up, down, left, right.

State:
{state_text}

Action:
""".strip()

        data = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0
        }

        resp = requests.post(self.api_url, headers=self.headers, json=data).json()

        # OpenRouter returns a list of messages under "completion"
        try:
            action = resp["completion"][0]["content"].strip().lower()
        except Exception:
            # fallback in case of unexpected response
            action = "up"

        if action not in ALLOWED:
            return "up"  # safe fallback

        return action
