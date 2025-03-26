import sys

input = sys.stdin.readline


def max_in_row(m, L):
    if L >= m:
        return m
    B0 = (m + 1) // (L + 1)
    best = 0
    for B in [B0, B0 + 1]:
        if B < 1 or B > m + 1:
            continue
        cand = min(B * L, m - B + 1)
        best = max(best, cand)
    return best


t = int(input().strip())
results = []
for _ in range(t):
    n, m, k = map(int, input().split())

    low, high = 1, m
    ans = m
    while low <= high:
        mid = (low + high) // 2
        if n * max_in_row(m, mid) >= k:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    results.append(str(ans))
print("\n".join(results))
