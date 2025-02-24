def solve():
    import sys

    input = sys.stdin.readline

    t = int(input().strip())
    results = []
    for _ in range(t):
        n = int(input().strip())
        reports = list(map(int, input().strip().split()))

        freq = [0] * 101
        for r in reports:
            freq[r] += 1

        valid = True

        if freq[0] == 0:
            valid = False
        else:
            for i in range(100):
                if freq[i] < freq[i + 1]:
                    valid = False
                    break

        results.append("YES" if valid else "NO")

    print("\n".join(results))


if __name__ == "__main__":
    solve()
