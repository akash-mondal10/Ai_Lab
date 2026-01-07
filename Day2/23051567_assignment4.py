import heapq
from collections import deque
def uniform_cost_search(graph, start, goal):
    pq = [(0, start)]         
    visited = set()
    parent = {start: None}
    cost = {start: 0}

    while pq:
        curr_cost, node = heapq.heappop(pq)

        if node in visited:
            continue
        visited.add(node)

        if node == goal:     
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            return path[::-1], curr_cost

        for neigh, w in graph.get(node, []):
            new_cost = curr_cost + w
            if neigh not in cost or new_cost < cost[neigh]:
                cost[neigh] = new_cost
                parent[neigh] = node
                heapq.heappush(pq, (new_cost, neigh))

    return None, None
def bfs_unweighted(graph, start, goal):
    q = deque([start])
    parent = {start: None}
    visited = {start}
    uw = {u: [v for v, _ in graph[u]] for u in graph}

    while q:
        node = q.popleft()
        if node == goal:
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            return path[::-1]

        for neigh in uw.get(node, []):
            if neigh not in visited:
                visited.add(neigh)
                parent[neigh] = node
                q.append(neigh)

    return None


# -------- Example Graph --------
graph = {
    "A": [("B", 2), ("C", 5)],
    "B": [("C", 1), ("D", 4)],
    "C": [("D", 1)],
    "D": [("E", 3)],
    "E": []
}
ucs_path, ucs_cost = uniform_cost_search(graph, "A", "E")
bfs_path = bfs_unweighted(graph, "A", "E")

print("UCS optimal path :", ucs_path, " Cost:", ucs_cost)
print("BFS path         :", bfs_path)