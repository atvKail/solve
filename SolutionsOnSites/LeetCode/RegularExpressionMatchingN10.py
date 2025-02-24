class Solution:
    def __init__(self):
        self.memo = {}

    def isMatch(self, s: str, p: str) -> bool:
        self.memo = {}
        return self._dp(s, p, 0, 0)

    def _dp(self, s: str, p: str, i: int, j: int) -> bool:
        if (i, j) in self.memo:
            return self.memo[(i, j)]

        if j == len(p):
            ans = i == len(s)
        else:
            first_match = i < len(s) and (p[j] == s[i] or p[j] == ".")
            if (j + 1) < len(p) and p[j + 1] == "*":
                ans = self._dp(s, p, i, j + 2) or (
                    first_match and self._dp(s, p, i + 1, j)
                )
            else:
                ans = first_match and self._dp(s, p, i + 1, j + 1)

        self.memo[(i, j)] = ans
        return ans


if __name__ == "__main__":
    matcher = Solution()

    print(matcher.isMatch("aa", "a"))  # False
    print(matcher.isMatch("aa", "a*"))  # True
    print(matcher.isMatch("ab", ".*"))  # True
    