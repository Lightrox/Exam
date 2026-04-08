from collections import deque

def water_jug_bfs(c1, c2, target):
    visited = set()
    q = deque([((0, 0), [])])

    while q:
        (x, y), path = q.popleft()

        if (x, y) in visited:
            continue
        visited.add((x, y))

        if x == target or y == target:
            return path + [(x, y)]

        next_states = [
            (c1, y), (x, c2),   # fill
            (0, y), (x, 0),     # empty
            (0, x+y) if x+y <= c2 else (x-(c2-y), c2),   # pour 1->2
            (x+y, 0) if x+y <= c1 else (c1, y-(c1-x))    # pour 2->1
        ]

        for ns in next_states:
            if ns not in visited:
                q.append((ns, path + [(x, y)]))

    return None


# Example usage
jug1 = 4
jug2 = 3
target = 2

solution = water_jug_bfs(jug1, jug2, target)

if solution:
    print(f"✅ Solution found in {len(solution)-1} steps:")
    for step in solution:
        print(f"Jug1: {step[0]}L, Jug2: {step[1]}L")
else:
    print("❌ No solution found.")