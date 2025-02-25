from math import sqrt
import sys


input = sys.stdin.readline

results = []
t = int(input())
for _ in range(t):
    k = int(input())
    if k == 0:
        print(1)
        print("0 0")
    else:
        groups = []
        rem = k

        while rem > 0:
            m = int((1 + sqrt(1 + 8 * rem)) / 2)
            if m < 2:
                m = 2
            while m * (m - 1) // 2 > rem:
                m -= 1
            groups.append(m)
            rem -= m * (m - 1) // 2

        n = sum(groups)
        results.append(str(n))

        cgroup = 0
        for m in groups:
            x = cgroup
            base_y = cgroup * 10000
            for j in range(m):
                results.append(f"{x} {base_y + j}")
            cgroup += 1
print("\n".join(results))
