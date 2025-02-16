def solve(n: int, s: str):
    blocks = 1
    for i in range(1, n):
        if s[i] != s[i - 1]:
            blocks += 1

    if s[0] == "0":
        ans = blocks - 1
    else:
        ans = blocks
    return ans


results = []
for _ in range(int(input())):
    n = int(input())
    s = input()
    results.append(str(solve(n, s)))
print("\n".join(results))
