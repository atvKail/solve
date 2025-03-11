class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        star_index = p.find("*")
        left = p[:star_index]
        right = p[star_index + 1 :]

        n = len(s)
        L = len(left)
        R = len(right)

        can_end = [False] * (n + 1)
        for j in range(R, n + 1):
            if s[j - R : j] == right:
                can_end[j] = True

        suffix_possible = [False] * (n + 2)
        suffix_possible[n] = can_end[n]
        for j in range(n - 1, -1, -1):
            suffix_possible[j] = can_end[j] or suffix_possible[j + 1]

        for i in range(n - L + 1):
            if s[i : i + L] == left:
                j_min = i + L + R
                if j_min <= n and suffix_possible[j_min]:
                    return True
        return False


def main() -> int:
    sol = Solution()
    s = input("Сама строка: ")
    p = input("Паттерн: ")
    verdict = sol.hasMatch(s=s, p=p)
    print(verdict)

    return 0


if __name__ == "__main__":
    import sys

    main()
