import sys

input = sys.stdin.readline


def linear_dp(w_arr):
    m = len(w_arr) - 1
    if m == 0:
        return 0
    if m == 1:
        return w_arr[1]
    if m == 2:
        return max(w_arr[1], w_arr[2])
    dp = [0] * (m + 1)
    dp[1] = w_arr[1]
    dp[2] = max(w_arr[1], w_arr[2])
    for i in range(3, m + 1):
        dp[i] = max(dp[i - 1], dp[i - 3] + w_arr[i])
    return dp[m]


def solve_circular(w):
    n = len(w) - 1
    if n == 1:
        return w[1]
    if n == 2:
        return max(w[1], w[2])
    if n == 3:
        return max(w[1], w[2], w[3])

    w_skipA = [0] + w[2:]
    ansA = linear_dp(w_skipA)

    base = w[1]
    if n <= 3:
        ansB = base
    else:
        if n - 2 < 3:
            ansB = base
        else:
            w_skipB = [0] + w[3 : (n - 1)]
            ansB = base + linear_dp(w_skipB)

    return max(ansA, ansB)


out = []
t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    a = list(map(int, input().strip().split()))

    if n < 3:
        out.append("0")
        continue
    top3 = sorted(a, reverse=True)[:3]
    best_single = top3[0] * top3[1] * top3[2]

    w_blocks = [0] * (n + 1)
    for i in range(1, n + 1):
        i2 = (i + 1) if (i + 1) <= n else (i + 1 - n)
        i3 = (i + 2) if (i + 2) <= n else (i + 2 - n)
        w_blocks[i] = a[i - 1] * a[i2 - 1] * a[i3 - 1]

    if n == 3:
        best_consecutive = w_blocks[1]
    else:
        best_consecutive = solve_circular(w_blocks)

    ans = max(best_single, best_consecutive)
    out.append(str(ans))

print("\n".join(out))

# Первый тест неверно
"""
Мой вывод:
6
24
6
30
772
648
Правильный:
6
24
5
30
732
696
"""
