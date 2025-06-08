with open(
    "USE\\ПолноценноеРешениеВариантов\\ИюньскийВариант4КЕГЭ2025\\26_22606.txt"
) as f:
    data = f.read().split()
N, T, M = map(int, data[:3])
cargoes = list(map(int, data[3 : 3 + N]))
cargoes.sort()

holds: list[tuple[int, int, int]] = []

for w in cargoes:
    placed = False
    for i, (mn, sm, cnt) in enumerate(holds):
        if w - mn <= T and sm + w <= M:
            holds[i] = (mn, sm + w, cnt + 1)
            placed = True
            break
    if not placed:
        holds.append((w, w, 1))
ttlholds = len(holds)

cfrst = holds[0][2]
print(ttlholds, cfrst)
