with open(
    "USE\\ПолноценноеРешениеВариантов\\ИюньскийВариантN1ШастинБахтиеваКЕГЭ\\24_22446.txt",
    "r",
) as f:
    raw = "".join(ch for ch in f.read() if ch in "LND")
n = len(raw)
if n < 1:
    print(0)
else:
    A = [0] * n
    for i in range(n - 2):
        if raw[i] == "L" and raw[i + 1] == "N" and raw[i + 2] == "D":
            A[i] = 1

    P = [0] * n
    P[0] = A[0]
    for i in range(1, n):
        P[i] = P[i - 1] + A[i]

    def cnt(i, j):
        if j - i + 1 < 3:
            return 0
        r = j - 2
        return P[r] - (P[i - 1] if i > 0 else 0)

    pos = {"L": [], "N": [], "D": []}
    for i, ch in enumerate(raw):
        pos[ch].append(i)

    K = 10000
    best = 0

    for ch in "LND":
        lst = pos[ch]
        r = 0
        for l in range(len(lst)):
            if r < l:
                r = l
            while r + 1 < len(lst) and cnt(lst[l], lst[r + 1]) <= K:
                r += 1
            length = lst[r] - lst[l] + 1
            if length > best:
                best = length

    print(best)
