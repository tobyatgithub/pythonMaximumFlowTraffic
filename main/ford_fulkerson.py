import math
from Graph import Graph
from typing import List, Union

Num = Union[int, float]
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
    },
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
            if (neighbor not in visited and
                    cur_graph.get_weight(fromNode=cur, toNode=neighbor) > 0):
                queue.append(neighbor)
                visited.add(neighbor)
                parentTracker[neighbor] = cur
    flag = sink in parentTracker
    return flag, parentTracker


# test ford fulkerson
def fordFulkerson(in_graph: Graph, source: str,
                  sink: str) -> ([int, float], Graph):
    # part 1, init and pre-construction
    flag = True
    cur_graph, maxFlowGraph = Graph(in_graph.graph), Graph()
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

        # update maxFlow graph after knowing the real local max flow.
        cur = sink
        while cur != source:
            parent = parentTracker.get(cur, source)
            cur_weight = maxFlowGraph.get_weight(parent, cur)
            maxFlowGraph.add_edge(parent, cur, cur_weight + local_maxFlow)
            cur = parent

        # update the graph for the next iteration
        cur = sink
        while cur != source:
            parent = parentTracker.get(cur, source)
            old_weight = cur_graph.get_weight(fromNode=parent, toNode=cur)
            cur_graph.add_edge(parent, cur, old_weight - local_maxFlow)
            cur = parent
    return maxFlow, maxFlowGraph


## double cross verification using google or-tools
"""From Taha 'Introduction to Operations Research', example 6.4-2."""
from ortools.graph import pywrapgraph


def OR_maxFlow(
    source: Num,
    sink: Num,
    start_nodes: List[Num],
    end_nodes: List[Num],
    capacities: List[Num],
):
    """MaxFlow simple interface example."""
    # Instantiate a SimpleMaxFlow solver.
    max_flow = pywrapgraph.SimpleMaxFlow()

    # Add each arc.
    for arc in zip(start_nodes, end_nodes, capacities):
        max_flow.AddArcWithCapacity(arc[0], arc[1], arc[2])

    # Find the maximum flow between node 0 and node 4.
    status = max_flow.Solve(source, sink)

    if status != max_flow.OPTIMAL:
        print("There was an issue with the max flow input.")
        print(f"Status: {status}")
        exit(1)
    print("Max flow:", max_flow.OptimalFlow())
    print("")
    print("  Arc    Flow / Capacity")
    for i in range(max_flow.NumArcs()):
        print("%1s -> %1s   %3s  / %3s" % (
            max_flow.Tail(i),
            max_flow.Head(i),
            max_flow.Flow(i),
            max_flow.Capacity(i),
        ))
    print("Source side min-cut:", max_flow.GetSourceSideMinCut())
    print("Sink side min-cut:", max_flow.GetSinkSideMinCut())
    return max_flow


# # Define three parallel arrays: start_nodes, end_nodes, and the capacities
# # between each pair. For instance, the arc from node 0 to node 1 has a
# # capacity of 20.
# start_nodes = [0, 0, 0, 1, 1, 2, 2, 3, 3]
# end_nodes = [1, 2, 3, 2, 4, 3, 4, 2, 4]
# capacities = [20, 30, 10, 40, 30, 10, 20, 5, 20]

# OR_maxFlow(0, 4, start_nodes, end_nodes, capacities)

## test ff
test1 = fordFulkerson(g, "A", "F")
print(test1)

print("**" * 10)


def turnGraphToNodesLists(graph):
    vertices = graph.get_vertexs()
    s_node, e_node, cap = [], [], []
    mapping = []

    for index, vertex in enumerate(vertices):
        neightbors = graph.get_neighbors(vertex)
        for node in neightbors:
            s_node.append(index)
            e_node.append(vertices.index(node))
            cap.append(graph.get_weight(vertex, node))
        mapping.append(vertex)
    return s_node, e_node, cap, mapping


start_nodes, end_nodes, capacities, mapping = turnGraphToNodesLists(g)
OR_maxFlow(0, 5, start_nodes, end_nodes, capacities)

g = Graph({
    "Waterfront": {
        "South Granville": 26,
        "Mount Pleasant": 34,
        "PNE": 28
    },
    "South Granville": {
        "Waterfront": 38,
        "Mount Pleasant": 29,
        "Marine Gate": 42
    },
    "Mount Pleasant": {
        "Waterfront": 23,
        "South Granville": 25,
        "Brentwood ": 42,
        "Metrotown": 37
    },
    "PNE": {
        "Waterfront": 30,
        "Brentwood ": 38
    },
    "Marine Gate": {
        "South Granville": 41,
        "Airport": 38,
        "Richmood": 22,
        "E-W Connector": 33
    },
    "Brentwood ": {
        "Mount Pleasant": 48,
        "PNE": 38,
        "Metrotown": 44
    },
    "Metrotown": {
        "Mount Pleasant": 34,
        "Brentwood ": 44,
        "E-W Connector": 44,
        "New West": 50
    },
    "Airport": {
        "Marine Gate": 38
    },
    "Richmood": {
        "Marine Gate": 28,
        "E-W Connector": 23
    },
    "E-W Connector": {
        "Marine Gate": 27,
        "Metrotown": 41,
        "Richmood": 26,
        "New West": 61
    },
    "New West": {
        "Metrotown": 47,
        "E-W Connector": 52
    }
})
"""
A = Waterfront, B = South Granville, C = Mount Pleasant, D = PNE, 
E = Marine Gate, F = Brentwood, G = Metrotown, H = Airport, I = Richmood, 
J = Temp, K = New West
"""

# connect multiple sources to one
g.add_edge("source", "Richmond", 500)
g.add_edge("source", "Metrotown", 500)
g.add_edge("source", "Marine Gate", 500)

print("=test2=" * 10)
test2 = fordFulkerson(g, "source", "Waterfront")
print(test2)

print("**" * 10)

start_nodes, end_nodes, capacities, mapping = turnGraphToNodesLists(g)
print("mapping = ", mapping, len(mapping))
OR_maxFlow(12, 11, start_nodes, end_nodes, capacities)