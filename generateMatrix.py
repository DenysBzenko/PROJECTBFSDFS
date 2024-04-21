import numpy as np
import random

def generate_random_weighted_graph(n, density, is_undirected=True):

    max_edges_undirected = n * (n - 1) // 2

    if density <= 0:
        m = 0
    elif density >= 1:
        m = max_edges_undirected if max_edges_undirected > 0 else 0
    else:
        m = int(density * max_edges_undirected)

    adjacency_matrix = np.zeros((n, n), dtype=int)
    adjacency_lists = [[] for _ in range(n)]

    edges_generated = 0
    while edges_generated < m:
        u, v = random.randint(0, n-1), random.randint(0, n-1)
        if u != v and adjacency_matrix[u, v] == 0:
            weight = random.randint(1, 50)
            adjacency_matrix[u, v] = weight
            adjacency_lists[u].append((v, weight))

            if is_undirected:
                adjacency_matrix[v, u] = weight
                adjacency_lists[v].append((u, weight))

            edges_generated += 1

    return adjacency_matrix, adjacency_lists

n = 10

density = 0.3
adj_matrix, adj_lists = generate_random_weighted_graph(n, density, is_undirected=True)

print("Adjacency Matrix:")
print(adj_matrix)

print("\nAdjacency Lists:")
for i in range(n):
    print(f"{i}: {adj_lists[i]}")
