import sys


input = sys.stdin.readline

results = []
t = int(input())
for _ in range(t):
    n, x, k = map(int, input().split())
    s = input()

    p = [0] * (n + 1)
    first_occ = {}
    for i in range(1, n + 1):
        move = 1 if s[i - 1] == "R" else -1
        p[i] = p[i - 1] + move
        if p[i] not in first_occ:
            first_occ[p[i]] = i

    ttlzero = 0
    usetime = 0

    if -x in first_occ:
        m_first = first_occ[-x]
        if m_first > k:
            results.append("0")
            continue
        ttlzero += 1
        usetime += m_first
    else:
        results.append("0")
        continue

    if 0 not in first_occ:
        results.append(str(ttlzero))
        continue

    m0 = first_occ[0]
    remtime = k - usetime
    addcycls = remtime // m0
    ttlzero += addcycls

    results.append(str(ttlzero))

print("\n".join(results))
