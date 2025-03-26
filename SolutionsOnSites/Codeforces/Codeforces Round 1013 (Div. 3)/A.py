import sys

input = sys.stdin.readline


t = int(input().strip())
required = {"0": 3, "1": 1, "2": 2, "3": 1, "5": 1}
for _ in range(t):
    n = int(input().strip())
    digits = input().split()
    freq = {}
    ans = 0

    for i, d in enumerate(digits, start=1):
        freq[d] = freq.get(d, 0) + 1

        if (
            freq.get("0", 0) >= required["0"]
            and freq.get("1", 0) >= required["1"]
            and freq.get("2", 0) >= required["2"]
            and freq.get("3", 0) >= required["3"]
            and freq.get("5", 0) >= required["5"]
        ):
            ans = i
            break
    print(ans)
