import time
from algorithmbfsdfs import bfs_matrix, bfs_list, dfs_matrix, dfs_list
from generateMatrix import generate_random_weighted_graph, n, density

adj_matrix, adj_list = generate_random_weighted_graph(n, density)

def run_search(func, data, method_name):
    start_time = time.time()
    path = func(data, 0)
    end_time = time.time()
    print_path(method_name, path, end_time - start_time)

def print_path(method_name, path, execution_time):
    if not path:
        print(f"No path found using {method_name}.")
    else:
        print(f"Shortest path using {method_name}: {path}")
        print(f"Path length: {len(path) - 1}")
        print(f"Execution time: {execution_time:.9f} seconds")

run_search(bfs_matrix, adj_matrix, "BFS using Adjacency Matrix")
run_search(dfs_matrix, adj_matrix, "DFS using Adjacency Matrix")
run_search(bfs_list, adj_list, "BFS using Adjacency List")
run_search(dfs_list, adj_list, "DFS using Adjacency List")
