def f(n: int) -> str:
    alpha = ["A", "B", "E", "H", "C"]
    result = []
    n -= 1

    for _ in range(5):
        result.append(alpha[n % 5])
        n //= 5

    return "".join(reversed(result))


cnt = 0
for i in range(1876, 2501):
    nf = f(i)
    snf = set(list(nf))
    if nf.count("B") == 2 and len(snf) == 4:
        cnt += 1
print(cnt)
