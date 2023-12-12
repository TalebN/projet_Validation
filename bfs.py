from collections import deque

class Graph:
    def __init__(self, root):
        self.graph = dict()
        self.root_node = root

    def add_new_one(self, u, v):
        self.graph.setdefault(u, []).append(v)

    def neighbors(self, node):
        return self.graph.get(node, [])

    def root(self):
        return self.root_node

def add_all(graph, edges):
    for edge in edges:
        graph.add_new_one(*edge)

def bfs_search(graph, query):
    visited = set()
    queue = deque([graph.root()])
    visited.add(graph.root())

    while queue:
        current_node = queue.popleft()

        if query(current_node):
            return visited
        for neighbor in graph.neighbors(current_node):
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

    return visited

#exemple dutilisation
# g = Graph(root=0)
# edges_to_add = [(0, 1), (0, 2), (0, 3), (1, 4), (2, 5), (3, 6)]
# add_all(g, edges_to_add)
#
# result = bfs_search(g, lambda n: n > 3)
#
# print(result)
