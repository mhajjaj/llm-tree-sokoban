import heapq
from logging import root
from typing import Dict, List, Optional, Tuple
from sokoban.search.node import SearchNode
from sokoban.utils.heuristics import heuristic
from sokoban.env.environment import ACTIONS

def reconstruct_path(node: SearchNode) -> List[str]:
    actions = []
    while node.parent is not None:
        actions.append(node.action)
        node = node.parent
    return list(reversed(actions))


def astar(env, max_nodes: int = 100_000) -> Optional[SearchNode]:
    start = env.initial_state
    start_h = heuristic(start, env.goals)

    root = SearchNode(
        state=start,
        parent=None,
        action=None,
        g=0,
        h=start_h
    )

    open_heap = []
    counter = 0
    heapq.heappush(open_heap, (root.g + root.h, counter, root))

    closed: Dict = {}
    expansions = 0

    while open_heap and expansions < max_nodes:
        _, _, node = heapq.heappop(open_heap)

        if env.is_goal(node.state):
            node.expansions = expansions
            return node

        if node.state in closed and closed[node.state] <= node.g:
            continue

        closed[node.state] = node.g
        expansions += 1

        for action in ACTIONS:
            next_state, ok = env.step(node.state, action)
            if not ok:
                continue

            if env.is_deadlock(next_state):
                continue

            g = node.g + 1
            h = heuristic(next_state, env.goals)

            child = SearchNode(
                state=next_state,
                parent=node,
                action=action,
                g=g,
                h=h
            )

            counter += 1
            heapq.heappush(open_heap, (g + h, counter, child))

    return None
