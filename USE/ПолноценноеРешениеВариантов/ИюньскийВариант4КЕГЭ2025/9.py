from collections import Counter


data = []
with open(
    "USE\\ПолноценноеРешениеВариантов\\ИюньскийВариант4КЕГЭ2025\\9_22550.csv"
) as f:
    while (line := f.readline()) != "":
        data.append(list(map(int, line.strip().split("."))))

for i in range(len(data)):
    curr = data[i]
    ctr = dict(Counter(curr))

    if sorted(ctr.values()) == [1, 1, 3, 3]:
        pov, unpov = [], []
        for x in ctr.keys():
            if ctr[x] > 1:
                pov.append(x)
            else:
                unpov.append(x)
        if (sum(unpov)) ** 3 > 3 * sum([x**2 for x in pov]):
            print(i + 1)
            break
