import time
from dataclasses import dataclass

@dataclass
class EvalResult:
    puzzle_id: int
    solved: bool
    steps: int | None
    expansions: int
    time_sec: float
    llm_calls: int

def evaluate(env, solver_fn, puzzle_id: int, **kwargs):
    start = time.time()
    result = solver_fn(env, **kwargs)
    elapsed = time.time() - start

    if result is None:
        return EvalResult(
            puzzle_id=puzzle_id,
            solved=False,
            steps=None,
            expansions=getattr(env, "expansions", 0),
            time_sec=elapsed,
            llm_calls=getattr(env, "llm_calls", 0),
        )

    return EvalResult(
        puzzle_id=puzzle_id,
        solved=True,
        steps=len(result.actions),
        expansions=result.expansions,
        time_sec=elapsed,
        llm_calls=getattr(result, "llm_calls", 0),
    )
