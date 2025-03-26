import math

MOD = 998244353


def solve():
    t = int(input().strip())
    for _ in range(t):
        n, m, d = map(int, input().split())
        grid = [input().rstrip() for _ in range(n)]

        levels = []
        for row in grid:
            levels.append([1 if ch == "X" else 0 for ch in row])

        def compute_initial(level_arr):
            dp = [0] * m

            for j in range(m):
                if level_arr[j]:
                    dp[j] = 1

            prefix = [0] * (m + 1)
            for j in range(m):
                prefix[j + 1] = prefix[j] + level_arr[j]
            for j in range(m):
                if level_arr[j]:
                    low = max(0, j - d)
                    high = min(m - 1, j + d)
                    count = prefix[high + 1] - prefix[low]

                    dp[j] = (dp[j] + count - 1) % MOD
            return dp

        dp = compute_initial(levels[n - 1])

        L_val = int(math.sqrt(d * d - 1)) if d * d - 1 >= 0 else 0

        for level_idx in range(n - 2, -1, -1):
            level_arr = levels[level_idx]
            new_dp = [0] * m

            prefix_dp = [0] * (m + 1)
            for j in range(m):
                prefix_dp[j + 1] = (prefix_dp[j] + dp[j]) % MOD

            for j in range(m):
                if level_arr[j]:
                    low = max(0, j - L_val)
                    high = min(m - 1, j + L_val)
                    one_touch = (prefix_dp[high + 1] - prefix_dp[low]) % MOD
                    new_dp[j] = (new_dp[j] + one_touch) % MOD

            H = [0] * m
            for j in range(m):
                if level_arr[j]:
                    low = max(0, j - L_val)
                    high = min(m - 1, j + L_val)
                    H[j] = (prefix_dp[high + 1] - prefix_dp[low]) % MOD

            prefix_H = [0] * (m + 1)
            for j in range(m):
                prefix_H[j + 1] = (prefix_H[j] + H[j]) % MOD
            conv = [0] * m
            for j in range(m):
                low = max(0, j - d)
                high = min(m - 1, j + d)
                conv[j] = (prefix_H[high + 1] - prefix_H[low]) % MOD

            for j in range(m):
                if level_arr[j]:
                    two_touch = (conv[j] - H[j]) % MOD
                    new_dp[j] = (new_dp[j] + two_touch) % MOD

            dp = new_dp

        result = sum(dp) % MOD
        print(result)


if __name__ == "__main__":
    solve()
