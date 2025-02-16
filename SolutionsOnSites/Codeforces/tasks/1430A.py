t = int(input())
for _ in range(t):
    n = int(input())
    found = False
    for a in range(n // 3 + 1):
        for b in range((n - 3 * a) // 5 + 1):
            rem = n - 3 * a - 5 * b
            if rem % 7 == 0:
                c = rem // 7
                print(a, b, c)
                found = True
                break
        if found:
            break
    if not found:
        print(-1)
