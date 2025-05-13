with open("USE\\ПолноценноеРешениеВариантов\\Открытый майский вариант 2025\\17_21903.txt", "r") as f:
    data = [int(line.strip()) for line in f.readlines()]

cnt = 0
mind = 100001**2
minn = min(data, key=lambda x: x if len(str(abs(x))) == 3 and abs(x) % 100 == 15 else 100001)
for i in range(2, len(data)):
    triple = data[i - 2], data[i - 1], data[i]
    if all([bool(d < 0) for d in triple]) or all([(d > 0) for d in triple]):
        minmaxd = min(triple) * max(triple)
        if minmaxd > minn * minn:
            cnt += 1
            mind = min(mind, minmaxd)
print(cnt, mind)
