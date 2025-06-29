from collections import Counter


path = "USE\\ПолноценноеРешениеВариантов\\Основная10Июня2025\\9_23193.txt"

data = []
with open(path, 'r') as f:
    for line in f:
        data.append(list(map(int, line.strip().split(';'))))

i = 1
prev = None
for line in data:
    ctr = dict(Counter(line))
    if len(ctr.keys()) == 4 and sorted(ctr.values()) == [1, 1, 1, 3]:
        nepov = sorted(ctr.keys(), key=lambda x: ctr[x])[-1]
        if nepov > sum(ctr.keys() - {nepov}) / 3:
            prev = i
    i += 1
print(prev)
