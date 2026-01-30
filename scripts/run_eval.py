from pathlib import Path
from sokoban.env.microban_parser import load_microban
from sokoban.env.environment import SokobanEnv
from sokoban.llm.llm_predictor import LLMPredictor
from sokoban.search.astar import astar, reconstruct_path
from sokoban.search.astar_llm import astar_llm

MICROBAN_PATH = Path("data/microban/microban.txt")


def main():
    puzzles = load_microban(MICROBAN_PATH)[:10]

    # Create LLM predictor once
    predictor = LLMPredictor()

    for i, p in enumerate(puzzles):
        env = SokobanEnv(p.raw_lines)

        res_astar = astar(env)
        print(
            f"[A*] Puzzle {i}:",
            "Solved" if res_astar else "Fail",
            f"steps={len(reconstruct_path(res_astar)) if res_astar else '-'}",
        )

        res_llm = astar_llm(env, predictor)
        print(
            f"[A*+LLM] Puzzle {i}:",
            "Solved" if res_llm else "Fail",
            f"steps={len(reconstruct_path(res_llm)) if res_llm else '-'}",
        )


if __name__ == "__main__":
    main()
