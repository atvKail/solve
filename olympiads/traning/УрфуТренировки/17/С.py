results = []
for _ in range(int(input())):
    n, c = input().split()
    s = input()

    n = int(n)
    
    if all(ch == c for ch in s):
        results.append("0")
        continue

    op = -1
    for x in range(2, n + 1):
        valid = True
        for j in range(x, n + 1, x):
            if s[j - 1] != c:
                valid = False
                break
        if valid:
            op = x
            break

    if op != -1:
        results.append("1")
        results.append(str(op))
    else:
        results.append("2")
        results.append(f"{n} {n - 1}")

print("\n".join(results))
