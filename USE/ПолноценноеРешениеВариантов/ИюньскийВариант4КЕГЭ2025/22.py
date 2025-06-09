from collections import defaultdict, deque


def analyze(p):
    g, dur, indeg = defaultdict(list), {}, defaultdict(int)
    start, end = {}, {}
    for i, t, deps in p:
        dur[i], start[i] = t, 0
        for j in set(deps):
            if j:
                g[j].append(i)
                indeg[i] += 1
    q = deque(i for i in start if indeg[i] == 0)
    while q:
        u = q.popleft()
        end[u] = start[u] + dur[u]
        for v in g[u]:
            start[v] = max(start[v], end[u])
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    events = sum(([(start[i], 1), (end[i], -1)] for i in start), [])
    events.sort(key=lambda x: (x[0], x[1]))
    cur = maxc = prev = tot = 0
    for t, d in events:
        if prev is not None and cur == maxc:
            tot += t - prev
        cur += d
        if cur > maxc:
            maxc, tot = cur, 0
        prev = t
    print(f"Макс. кол-во процессов={maxc}, Максимальное время={tot}")


s = """
ID процесса B	Время выполнения процесса B (мс)	ID процессов A
1	10	0
2	14	0
3	5	1;2
4	13	1
5	15	3;4
6	10	5
7	11	4;6
8	13	0
9	13	0
10	15	8;9
11	7	8;9
12	5	7;10;11
"""
lines = s.strip().splitlines()[1:]
processes = []
for line in lines:
    id_str, time_str, deps_str = line.split("\t")
    deps = [int(x) for x in deps_str.split(";")] if deps_str != "0" else [0]
    processes.append((int(id_str), int(time_str), deps))

analyze(processes)
