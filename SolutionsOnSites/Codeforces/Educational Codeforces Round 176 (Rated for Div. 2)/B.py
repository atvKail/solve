import sys

input = sys.stdin.readline


results = []
t = int(input().strip())
for _ in range(t):
    n, k = map(int, input().strip().split())
    a = list(map(int, input().strip().split()))
    if k == 1:
        if n == 1:
            results.append(str(a[0]))
        else:
            c1 = a[0] + max(a[1:])
            c2 = a[-1] + max(a[:-1])
            results.append(str(max(c1, c2)))
    else:
        m = k + 1

        sorta = sorted(a, reverse=True)
        results.append(str(sum(sorta[:m])))
print("\n".join(results))
