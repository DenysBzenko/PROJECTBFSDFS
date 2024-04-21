import numpy as np
from collections import deque

def bfs_matrix(adj_matrix, start):
    visited = [False] * len(adj_matrix)
    queue = deque([start])
    path = []
    visited[start] = True

    while queue:
        vertex = queue.popleft()
        path.append(vertex)
        for i, is_adjacent in enumerate(adj_matrix[vertex]):
            if is_adjacent and not visited[i]:
                visited[i] = True
                queue.append(i)
    return path

def dfs_matrix(adj_matrix, start):
    visited = [False] * len(adj_matrix)
    path = []
    stack = [start]

    while stack:
        vertex = stack.pop()
        if not visited[vertex]:
            visited[vertex] = True
            path.append(vertex)
            for i, is_adjacent in enumerate(adj_matrix[vertex]):
                if is_adjacent and not visited[i]:
                    stack.append(i)
    return path

def bfs_list(adj_list, start):
    visited = [False] * len(adj_list)
    queue = deque([start])
    path = []
    visited[start] = True

    while queue:
        vertex = queue.popleft()
        path.append(vertex)
        for neighbor, _ in adj_list[vertex]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    return path

def dfs_list(adj_list, start):
    visited = [False] * len(adj_list)
    path = []
    stack = [start]

    while stack:
        vertex = stack.pop()
        if not visited[vertex]:
            visited[vertex] = True
            path.append(vertex)
            for neighbor, _ in reversed(adj_list[vertex]):
                if not visited[neighbor]:
                    stack.append(neighbor)
    return path
