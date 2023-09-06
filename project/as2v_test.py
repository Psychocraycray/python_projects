def can_escape(n, m, k, vx, vy, friends):
    graph = {}
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            neighbors = []
            if i > 1:
                neighbors.append((i - 1, j))
            if i < n:
                neighbors.append((i + 1, j))
            if j > 1:
                neighbors.append((i, j - 1))
            if j < m:
                neighbors.append((i, j + 1))
            graph[(i, j)] = neighbors

    visited = set()
    q = [(vx, vy, 0)]
    visited.add((vx, vy))
    while q:
        x, y, steps = q.pop(0)
        if steps == 101:  # Vika can move at most n*m times
            return "YES"
        for nx, ny in graph[(x, y)]:
            if (nx, ny) in visited:
                continue
            if (nx, ny) in friends:
                if abs(nx - vx) + abs(ny - vy) == 1:
                    continue
                else:
                    return "NO"
            visited.add((nx, ny))
            q.append((nx, ny, steps + 1))
    return "YES"


t = int(input())

for i in range(t):
    n, m, k = map(int, input().split())
    vx, vy = map(int, input().split())
    friends = set()
    for j in range(k):
        x, y = map(int, input().split())
        friends.add((x, y))
    result = can_escape(n, m, k, vx, vy, friends)
    print(result)
