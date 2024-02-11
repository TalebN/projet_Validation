from collections import deque

#implémentation de la recherche en largeur (BFS) dans un graphe.
def bfs_search(graph, query):
    visited = set()
    queue = deque()
    i = True

    while queue or i:
        if i:
            neighbours = graph.getRoots()
            i = False
        else:
            neighbours = graph.getNeighbors(queue.popleft())

        for neighbour in neighbours:
            if neighbour not in visited:
                if query(neighbour):
                    return neighbour, visited
                visited.add(neighbour)
                queue.append(neighbour)
    return None, visited

