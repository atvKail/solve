from collections import Counter


with open("USE\\Решения\\26\\2653\\26_2653.txt") as f:
    data = f.read().split()
n = int(data[0])
ws = list(map(int, data[1 : 1 + n]))
ttl = sum(ws)

cnt = Counter(ws)
items = []
for w, c in cnt.items():
    k = 1
    while c > k:
        items.append(w * k)
        c -= k
        k <<= 1
    if c:
        items.append(w * c)

rable = 1
mask = (1 << (ttl + 1)) - 1
for w in items:
    rable |= (rable << w) & mask

rlv = ((1 << ttl) - 1) ^ 1
impable = (~rable) & rlv

count = impable.bit_count()
max_un = impable.bit_length() - 1 if impable else 0

print(count, max_un)
