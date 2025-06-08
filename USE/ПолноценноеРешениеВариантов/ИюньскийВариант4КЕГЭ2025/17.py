MAX = int(1e5 + 1)

data = []
dataT = []
with open(
    "USE\\ПолноценноеРешениеВариантов\\ИюньскийВариант4КЕГЭ2025\\17_22471.txt"
) as f:
    triple = []
    while (line := f.readline()) != "":
        data.append(int(line.strip()))
        if len(triple) >= 3:
            dataT.append(triple)
            triple = triple[1:] + [int(line.strip())]
        else:
            triple.append(int(line.strip()))
    if len(triple) == 3:
        dataT.append(triple)
mx, cnt = -1, 0
miel = min(data, key=lambda x: x if x > 0 and len(str(x)) == 3 else MAX)
for triple in dataT:
    striple = sorted(triple)
    if striple[1] >= 0 and striple[0] + striple[2] > miel:
        mx = max(sum(striple), mx)
        cnt += 1
print(cnt, mx)
