import heapq

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def best_first_search(grid, start, treasure):
    rows, cols = len(grid), len(grid[0])

    pq = []
    heapq.heappush(pq, (manhattan(start, treasure), start))

    visited = set()
    parent = {start: None}

    while pq:
        heuristic, current = heapq.heappop(pq)
        
        if current == treasure:
            return reconstruct_path(parent, treasure)

        visited.add(current)
        x, y = current

        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols:
                if grid[nx][ny] == 0 and (nx, ny) not in visited:
                    parent[(nx, ny)] = current
                    h = manhattan((nx, ny), treasure)
                    heapq.heappush(pq, (h, (nx, ny)))

    return None 

def reconstruct_path(parent, goal):
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = parent[current]
    return path[::-1]

grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],          
    [0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
treasure = (4, 4)

path = best_first_search(grid, start, treasure)

print("Path to Treasure:", path)