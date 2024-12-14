import heapq

def f(a, c):
    return [a[i][c] for i in range(len(a))]

def dijkstra(n, graph):
    dist = [float("inf")] * n
    dist[0] = 0
    pq = [(0, 0)]

    while pq:
        d, node = heapq.heappop(pq)
        if d > dist[node]:
            continue

        for neighbor, weight in graph[node]:
            if dist[neighbor] > d + weight:
                dist[neighbor] = d + weight
                heapq.heappush(pq, (dist[neighbor], neighbor))

    return dist


for _ in range(int(input())):
    n, m = map(int, input().split())
    c = list(map(int, input().split()))
    graph = [[] for _ in range(n)]

    for __ in range(m):
        u, v, w = map(int, input().split())
        graph[u - 1].append((v - 1, w))
        graph[v - 1].append((u - 1, w))
    
    for i in range(n):
        for j in range(n):
            if j not in f(graph[i], 0):
                graph[i].append((j, c[i]))

    dist = dijkstra(n, graph)

    print(" ".join(map(str, dist)))


# не отправил, идет все к черту на подспорье! 