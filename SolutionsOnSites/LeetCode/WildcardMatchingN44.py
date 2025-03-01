class Solution:
    def isMatchDynamic(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        dp[0][0] = True

        for j in range(1, n + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 1]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == "?" or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == "*":
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
        return dp[m][n]

    def isMatchGreedy(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        i = j = 0
        star_idx = -1
        match = 0

        while i < m:
            if j < n and (p[j] == "?" or p[j] == s[i]):
                i += 1
                j += 1
            elif j < n and p[j] == "*":
                star_idx = j
                match = i
                j += 1
            elif star_idx != -1:
                j = star_idx + 1
                match += 1
                i = match
            else:
                return False

        while j < n and p[j] == "*":
            j += 1

        return j == n


def main() -> int:
    import sys

    input = sys.stdin.readline

    sol = Solution()
    string = input()
    pattern = input()

    print(sol.isMatchDynamic(string, pattern))
    print(sol.isMatchGreedy(string, pattern))

    return 0


if __name__ == "__main__":
    main()
