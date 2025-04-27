import sys
import heapq

input = sys.stdin.readline


N, M, A, B = map(int, input().split())
D = int(input())
adj = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, t = map(int, input().split())
    adj[u].append((v, t))
    adj[v].append((u, t))

visited = [False] * (N + 1)
visited[A] = True

front = [A]
days = 0

f = True
while front:
    days += 1

    dist = [10**30] * (N + 1)
    pq = []
    for u in front:
        dist[u] = 0
        heapq.heappush(pq, (0, u))

    rable = [False] * (N + 1)
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u] or d > D:
            continue
        rable[u] = True
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v] and nd <= D:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))

    if rable[B]:
        print(days)
        f = False
        break

    nfront = []
    for u in range(1, N + 1):
        if rable[u] and not visited[u]:
            visited[u] = True
            nfront.append(u)
    front = nfront
if f:
    print(-1)
