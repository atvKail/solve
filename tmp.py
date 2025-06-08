import sys
import bisect


input = sys.stdin.readline

t = int(input())
horizontals = []
verticals = []
for i in range(1, t + 1):
    x1, y1, x2, y2 = map(int, input().split())
    if y1 == y2:
        xmin, xmax = min(x1, x2), max(x1, x2)
        horizontals.append((xmin, xmax, y1, i))
    else:
        ymin, ymax = min(y1, y2), max(y1, y2)
        verticals.append((x1, ymin, ymax, i))

events = []
for xmin, xmax, y, idH in horizontals:
    events.append((xmin, 0, y, idH))
    events.append((xmax, 2, y, idH))
for x, ymin, ymax, idV in verticals:
    events.append((x, 1, ymin, ymax, idV))

events.sort(key=lambda x: (x[0], x[1]))

active = []
id_to_y = {}
flagH = [False] * (t + 1)
flagV = [False] * (t + 1)

for ev in events:
    if ev[1] == 0:
        _, _, y, idH = ev
        bisect.insort(active, (y, idH))
        id_to_y[idH] = y
    elif ev[1] == 2:
        _, _, y, idH = ev
        pos = bisect.bisect_left(active, (y, idH))
        if pos < len(active) and active[pos] == (y, idH):
            active.pop(pos)
    else:
        _, _, ymin, ymax, idV = ev
        l = bisect.bisect_right(active, (ymin, 10**18))
        r = bisect.bisect_left(active, (ymax, -(10**18)))
        if l < r:   
            flagV[idV] = True
            for y, idH in active[l:r]:
                flagH[idH] = True

ans = 0
for i in range(1, t + 1):
    if flagH[i] or flagV[i]:
        ans += 1
print(ans)
