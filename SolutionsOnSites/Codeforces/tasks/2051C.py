import sys


input = sys.stdin.readline

t = int(input().strip())
results = []
for _ in range(t):
    n, m, k = map(int, input().strip().split())
    a = list(map(int, input().strip().split()))
    q = list(map(int, input().strip().split()))
    unk_cnt = n - k

    if unk_cnt >= 2:
        results.append("0" * m)

    elif unk_cnt == 0:
        results.append("1" * m)
    else:
        unknown = None

        j = 0
        for num in range(1, n + 1):
            if j < k and q[j] == num:
                j += 1
            else:
                unknown = num
                break

        ans = []
        for ai in a:
            if ai == unknown:
                ans.append("1")
            else:
                ans.append("0")
        results.append("".join(ans))
print("\n".join(results))
