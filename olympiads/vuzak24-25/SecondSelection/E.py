import sys


sys.setrecursionlimit(10**6)


def in_subtree(u, x):
    return tin[x] <= tin[u] < tout[x]


def same_component(u, v, child):
    return in_subtree(u, child) == in_subtree(v, child)


def dfs(v, p):
    global timer
    tin[v] = timer
    timer += 1
    par[v] = p
    for nv, w in graph[v]:
        if nv == p:
            continue
        dist_s[nv] = dist_s[v] + w
        dfs(nv, v)
    tout[v] = timer


n, s, t = map(int, input().split())
s -= 1
t -= 1

graph = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    u, v = u - 1, v - 1
    graph[u].append((v, w))
    graph[v].append((u, w))

dist_s, tin, tout, par, timer = [0] * n, [0] * n, [0] * n, [-1] * n, 0

dfs(s, -1) # вход/выход время, родаки, расстояния

# от t 
dist_t = [None] * n
dist_t[t] = 0
stack = [t]
while stack:
    cur = stack.pop()
    for nv, w in graph[cur]:
        if dist_t[nv] is None:
            dist_t[nv] = dist_t[cur] + w
            stack.append(nv)

results = []
q = int(input())
for _ in range(q):
    a1, b1, a2, b2, c = map(int, input().split())
    a1, b1, a2, b2 = a1 - 1, b1 - 1, a2 - 1, b2 - 1

    if par[a1] == b1:
        child = a1
    elif par[b1] == a1:
        child = b1
    else:
        child = a1

    ans = float('infinity')

    # s-t
    if same_component(s, t, child):
        ans = min(ans, dist_s[t])

    # s-a2, b2-t, +a2->b2
    if same_component(s, a2, child) and same_component(b2, t, child):
        candidate = dist_s[a2] + c + dist_t[b2]
        ans = min(ans, candidate)

    # s->b2, b2->a2, a2->t
    if same_component(s, b2, child) and same_component(a2, t, child):
        candidate = dist_s[b2] + c + dist_t[a2]
        ans = min(ans, candidate)

    results.append(str(ans if ans < float('infinity') else -1))

print("\n".join(results))
