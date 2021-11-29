"""
Here we define the node and directed graph 
that serves as the basic fundations of our
ford-fulkerson algorithm.
"""


class Graph:
    """
    Here we implement the famous data structure--graph.
    It's a data structure made up by nodes and edges.
    Generally tehre's no limitation on number of nodes, and number of edges.
    Edges can also be weighted or non-weighted.
    """
    def __init__(self, iterable={}, directional=True):
        """
        For here iterable only takes in vertices and weighted edges.
        Right now it only support format as:
        Graph({
            'A': {'B': 10},
            'B': {'A': 5, 'D': 15, 'C': 20},
            })
        """
        self.graph = {}
        self._size = 0
        self.directional = directional
        if isinstance(iterable, dict):
            for v1 in iterable.keys():
                self.add_vertex(v1)
                for v2, weight in iterable[v1].items():
                    self.add_edge(v1, v2, weight)

    def add_vertex(self, val):
        if not self.has_vertex(val):
            self.graph[val] = {}
            self._size += 1
        return self

    def add_edge(self, v1, v2, weight=1):
        """
        adding edge from v1 to v2 with given weight.
        if no weight is imported, it's set to default value 1.
        """
        if not self.has_vertex(v1):
            self.add_vertex(v1)
        if not self.has_vertex(v2):
            self.add_vertex(v2)

        self.graph[v1][v2] = weight

        # if bi-directional, then we also need to add the second direction
        if not self.directional:
            self.graph[v2][v1] = weight
        return self

    def __repr__(self):
        if self._size == 0:
            print("This is an empty graph.")
        print(self.graph)

    def __str__(self):
        if self._size == 0:
            return "This is an empty graph."
        return str(self.graph)

    def __len__(self):
        return self._size

    def has_vertex(self, val):
        """
        checks for a key in the graph
        input: self of graph class, and a value to check
        output: a boolean value
        """
        return val in self.graph

    def get_vertexs(self):
        return sorted(list(self.graph.keys()))

    def get_weight(self, fromNode, toNode):
        return self.graph.get(fromNode, {}).get(toNode, 0)

    def get_neighbors(self, val):
        """
        Given a val (key), return all adjacent verts
        """
        if not self.has_vertex(val):
            print(f'Input value {val} is not in this graph.')
            return {}
        return self.graph[val]


## test:
# Here we construct a flow graph that we will use to test our FF algorithm.
# g = Graph({
#     "A": {
#         "B": 16,
#         "C": 13
#     },
#     "B": {
#         "C": 10,
#         "D": 12
#     },
#     "C": {
#         "B": 4,
#         "E": 14
#     },
#     "D": {
#         "C": 9,
#         "F": 20
#     },
#     "E": {
#         "D": 7,
#         "F": 4
#     }
# })
# print(g)
