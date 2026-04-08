from itertools import permutations

def tsp(graph, start):
    n = len(graph)
    nodes = [i for i in range(n) if i != start]

    min_cost = float('inf')
    best_path = []

    for p in permutations(nodes):
        path = [start] + list(p) + [start]

        cost = 0
        for i in range(len(path) - 1):
            cost += graph[path[i]][path[i+1]]

        if cost < min_cost:
            min_cost = cost
            best_path = path

    return best_path, min_cost


# Example
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

route, cost = tsp(graph, 0)
print("Best Route:", route)
print("Minimum Cost:", cost)