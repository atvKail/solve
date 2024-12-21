for _ in range(int(input())):
    s, k = map(int, input().split())

    l, r = (
        1,
        int((2 * s) ** 0.5) + 1,
    )  # Sn = n / 2 * (a + (n - 1) * k) => n ~ sqrt(2 * s)

    while l < r:
        mid = l + (r - l) // 2 + 1
        mbs = mid * (2 + (mid - 1) * k) // 2  # a1 = 2

        if mbs <= s:
            l = mid
        else:
            r = mid - 1

    print(l)
