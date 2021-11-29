import math
from Graph import Graph

DEBUG = True

g = Graph({
    "A": {
        "B": 16,
        "C": 13
    },
    "B": {
        "C": 10,
        "D": 12
    },
    "C": {
        "B": 4,
        "E": 14
    },
    "D": {
        "C": 9,
        "F": 20
    },
    "E": {
        "D": 7,
        "F": 4
    }
})
print(g)


def fordBFS(cur_graph: Graph, source: str, sink: str) -> (bool, dict):
    """
    Two duties: 
    1. find a path from source to sink, and save that path info
    by constructing a parent dictionary.
    2. return a boolean flag indicating whether it is possible to
    reach sink from the source
    """

    parentTracker = {}
    queue = [source]
    visited = set()

    while queue:
        cur = queue.pop(0)
        for neighbor in cur_graph.get_neighbors(cur):
            if neighbor not in visited and cur_graph.get_weight(
                    fromNode=cur, toNode=neighbor) > 0:
                queue.append(neighbor)
                visited.add(neighbor)
                parentTracker[neighbor] = cur
    flag = sink in parentTracker
    return flag, parentTracker


# test ford fulkerson
def fordFulkerson(graph: Graph, source: str, sink: str) -> [int, float]:
    # part 1, init and pre-construction
    flag = True
    cur_graph = graph
    maxFlow = 0

    # keep search for new pathes from source to the sink
    while flag:
        flag, parentTracker = fordBFS(cur_graph, source, sink)
        if DEBUG:
            print(
                f"1. Search for new pathes: flag={flag}, parentTracker={parentTracker}."
            )
        local_maxFlow = math.inf
        cur = sink

        # based on the current parentTracker, we find the local flow
        while cur != source:
            parent = parentTracker.get(cur, source)
            local_maxFlow = min(
                local_maxFlow, cur_graph.get_weight(fromNode=parent,
                                                    toNode=cur))
            cur = parent
        if DEBUG:
            print(
                f"2. Based on the found parentTracker, calculate local_maxFlow = {local_maxFlow}."
            )
        maxFlow += local_maxFlow

        # update the graph for the next iteration
        cur = sink
        while cur != source:
            parent = parentTracker.get(cur, source)
            old_weight = cur_graph.get_weight(fromNode=parent, toNode=cur)
            cur_graph.add_edge(parent, cur, old_weight - local_maxFlow)
            cur = parent
    return maxFlow


## test ff
test1 = fordFulkerson(g, "A", "F")
print(test1)