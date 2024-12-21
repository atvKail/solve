def dijkstra(matrix, start, end):
    import heapq

    rows, cols = len(matrix), len(matrix[0])
    dist = [[float("inf")] * cols for _ in range(rows)]
    dist[start[0]][start[1]] = matrix[start[0]][start[1]]
    pq = [(matrix[start[0]][start[1]], start[0], start[1])]

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while pq:
        current_dist, x, y = heapq.heappop(pq)

        if (x, y) == end:
            return current_dist

        if current_dist > dist[x][y]:
            continue

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                new_dist = current_dist + matrix[nx][ny]
                if new_dist < dist[nx][ny]:
                    dist[nx][ny] = new_dist
                    heapq.heappush(pq, (new_dist, nx, ny))

    return float("inf")


def merge_matrices(A, B):
    n = len(A)
    merged = [[float('inf')] * (2 * n) for _ in range(2 * n)]

    for i in range(n):
        for j in range(n):
            merged[i][j] = A[i][j]
            merged[i + n][j + n] = B[i][j]

    for i in range(n):
        for j in range(n):
            merged[i + n][j] = B[i][j]
            merged[i][j + n] = A[i][j]

    return merged


n = int(input())
A = []
B = []

for i in range(n):
    A.append(list(map(int, input().split())))

for i in range(n):
    B.append(list(map(int, input().split())))

merged = merge_matrices(A, B)
start = (n, n)
end = (n - 1, n - 1)

print(dijkstra(merged, start, end))
