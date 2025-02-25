import sys


input = sys.stdin.readline

results = []
t = int(input())
for _ in range(t):
    n = int(input().strip())
    a = list(map(int, input().split()))

    bdelt = 0
    bl, br = 0, 0

    for l in range(n):
        cntLess = 0
        cntGreatr = 0
        for r in range(l + 1, n):
            if a[r] > a[l]:
                cntGreatr += 1
            elif a[r] < a[l]:
                cntLess += 1
            delta = cntGreatr - cntLess
            if delta < bdelt:
                bdelt = delta
                bl = l
                br = r
    results.append(f"{bl + 1} {br + 1}")
print("\n".join(results))
