def main():
    import sys

    input = sys.stdin.readline

    results = []
    t = int(input().strip())
    for _ in range(t):
        b, c, h = map(int, input().strip().split())
        k = min(b - 1, c + h)
        results.append(str(2 * k + 1))

    print("\n".join(results))


if __name__ == "__main__":
    main()
