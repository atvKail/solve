mi = 100000 + 1
path = "USE\\ПолноценноеРешениеВариантов\\Основная10Июня2025\\17_23201.txt"

data = []
with open(path, 'r') as f:
    para = []
    for line in f:
        x = int(line.strip())
        if x < mi and x % 10 == 7 and 1 <= x // 100 <= 9:
            mi = x
        if len(para) < 2:
            para.append(x)
        else:
            data.append(para)
            para = para[1:] + [x]
    data.append(para)
print(mi)

mis = 100000 * 2 + 1
cnt = 0
for p in data:
    if 1 <= p[0] // 100 <= 9 and not (1 <= p[1] // 100 <= 9) or not 1 <= p[0] // 100 <= 9 and (1 <= p[1] // 100 <= 9):
        if sum(p) % mi == 0:
            cnt += 1
            mis = min(mis, sum(p))
print(cnt, mis)
