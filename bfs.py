from collections import deque

class Graph:
    def __init__(self):
        self.graph = dict()

    def add_new_one(self, u, v):
        self.graph.setdefault(u, []).append(v)

    def neighbors(self, node):
        return self.graph.get(node, [])

def add_all(graph, edges):
        for edge in edges:
            graph.add_new_one(*edge)

def bfs_search(graph, start, query):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        current_node = queue.popleft()

        if query(current_node):
            return visited
        for neighbor in graph.neighbors(current_node):
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

    return visited


g = Graph()
edges_to_add = [(0, 1), (0, 2), (0, 3), (1, 4), (2, 5), (3, 6)]
add_all(g, edges_to_add)
start_node = 0

result = bfs_search(g, start_node, lambda n: n > 3)

print(result)

