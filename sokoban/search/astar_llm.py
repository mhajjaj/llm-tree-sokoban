import heapq
from sokoban.search.node import SearchNode
from sokoban.utils.heuristics import heuristic
from sokoban.env.environment import ACTIONS

def astar_llm(env, predictor, max_nodes=100_000):
    start = env.initial_state
    root = SearchNode(start, None, None, 0, heuristic(start, env.goals))

    open_heap = []
    counter = 0
    heapq.heappush(open_heap, (root.g + root.h, counter, root))

    closed = {}

    while open_heap:
        _, _, node = heapq.heappop(open_heap)

        if env.is_goal(node.state):
            return node

        if node.state in closed and closed[node.state] <= node.g:
            continue

        closed[node.state] = node.g

        # ---- LLM action prediction ----
        state_text = env.to_text(node.state)
        preferred = predictor.predict(state_text)

        ordered_actions = [preferred] + [a for a in ACTIONS if a != preferred]

        for action in ordered_actions:
            next_state, ok = env.step(node.state, action)
            if not ok:
                continue

            if env.is_deadlock(next_state):
                continue

            g = node.g + 1
            h = heuristic(next_state, env.goals)

            counter += 1
            heapq.heappush(
                open_heap,
                (g + h, counter,
                 SearchNode(next_state, node, action, g, h))
            )

    return None
