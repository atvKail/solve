def solve(n: int, a: list):
    S = 0
    for i in range(1, n):
        S += abs(a[i] - a[i - 1])

    best = 0
    best = max(best, abs(a[1] - a[0]))
    best = max(best, abs(a[n - 1] - a[n - 2]))

    for i in range(1, n - 1):
        gain = abs(a[i] - a[i - 1]) + abs(a[i + 1] - a[i]) - abs(a[i + 1] - a[i - 1])
        best = max(best, gain)

    return S - best


results = []
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    results.append(solve(n, a))
print(*results, sep="\n")
