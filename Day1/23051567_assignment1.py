# Assignment-1: Maze Solver using BFS and DFS
# Objective: Implement BFS and DFS to solve a maze.
# Problem Statement: Given a grid-based maze where 0 represents walls and 1
# represents walkable paths, find the shortest path from a start cell to an end cell.
# Tasks:
# 1.Use BFS to find the shortest path.
# 2.Use DFS to explore all possible paths and report one valid path (not necessarily
# the shortest).
# 3.Compare the number of nodes explored by BFS and DFS.

from collections import deque

def reconstruct_path(came_from, start, end):
    path=[]
    current = end
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path

def bfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    queue = deque([start])
    visited = set()
    visited.add(start)
    came_from = {}
    nodes_explored = 0

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    while queue:
        current = queue.popleft()
        nodes_explored +=1
        if current == end:
            path = reconstruct_path(came_from, start, end)
            return path, nodes_explored
        for direction in directions:
            neighbour = (current[0] + direction[0], current[1] + direction[1])
            if (0 <= neighbour[0] < rows and 0 <= neighbour[1] < cols and maze [neighbour[0]][neighbour[1]] == 1 and neighbour not in visited):
                visited.add(neighbour)
                came_from[neighbour] = current
                queue.append(neighbour)
    return None, nodes_explored  # No path found

def dfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    stack = [start]
    visited = set()
    visited.add(start)
    came_from = {}
    nodes_explored = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    while stack:
        current = stack.pop()
        nodes_explored +=1
        if current == end:
            path = reconstruct_path(came_from, start, end)
            return path, nodes_explored
        for direction in directions:
            neighbour = current[0] + direction[0], current[1] + direction[1]
            if (0 <= neighbour[0] <rows and 0 <= neighbour[1] < cols and maze[neighbour[0]][neighbour[1]] == 1 and neighbour not in visited):
                visited.add(neighbour)
                came_from[neighbour] = current
                stack.append(neighbour)
    return None, nodes_explored  # No path found

# Example maze
maze = [
    [1, 0, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 1, 1, 1],
    [1, 1, 0, 0, 1]
]
start = (0, 0)
end = (4, 4)
bfs_path, bfs_explored = bfs(maze, start, end)
print("BFS Shortest Path:", bfs_path)
print("BFS Nodes Explored:", bfs_explored)

# Run DFS
dfs_path, dfs_explored = dfs(maze, start, end)
print("DFS Path (not always shortest):", dfs_path)
print("DFS Nodes Explored:", dfs_explored)

# Comparison
print("\n--- Comparison ---")
print("BFS explored:", bfs_explored, "nodes")
print("DFS explored:", dfs_explored, "nodes")

