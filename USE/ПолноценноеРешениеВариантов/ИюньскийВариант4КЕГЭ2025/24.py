with open(
    "USE\\ПолноценноеРешениеВариантов\\ИюньскийВариант4КЕГЭ2025\\24_22449.txt", "r"
) as f:
    s = f.read().strip()

n = len(s)
k = n if n < 500_000 else 500_000

w = [ord(c) - 64 for c in s]

curr = sum(w[:k])
best = curr
best_i = 0

for i in range(k, n):
    curr += w[i] - w[i - k]
    if curr > best:
        best = curr
        best_i = i - k + 1

print(best_i)
