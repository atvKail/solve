path = "USE\\ПолноценноеРешениеВариантов\\Основная10Июня2025\\26_23208.txt"
data = []

with open(path, 'r') as f:
    n = int(f.readline().strip())
    for i in range(n):
        grinding, coloring = map(int, f.readline().strip().split())
        dg, dc = [i + 1, grinding, 0], [i + 1, coloring, 1] # [номер, время, шлифовка-0/окраска-1]
        data.append(dc)
        data.append(dg)
        
prev = 0
shl = []
visited = set()
i, j = 0, 2 * n - 1
tape = [float('infinity')] * 2 * n
data.sort(key=lambda x: x[1])
for d in data:
    ni, time, typed = d
    if typed == 0 and ni not in visited:
        tape[i] = time
        visited.add(ni)
        i += 1
        prev = ni
        shl.append(time)
    elif typed == 1 and ni not in visited:
        tape[j] = time
        visited.add(ni)
        j -= 1
        prev = ni
        
cnt, i = 0, 0
while i < len(shl) and shl[i] <= tape[j + 1]:
    cnt += 1
    i += 1
print(prev, cnt)
