for i in range(int(input())):
    n, k = map(int, input().split())
    nk = k
    st = input()
    sp = [0] * n
    ans = ""
    for i in range(n):
        if k == 0:
            break
        if nk % 2 == 1 and st[i] == '1':
            sp[i] = sp[i] + 1
            k = k - 1
        elif nk % 2 == 0 and st[i] == '0':
            sp[i] = sp[i] + 1
            k = k - 1
    sp[n - 1] = sp[n - 1] + k
    for i in range(n):
        flip = nk - sp[i]
        if flip % 2 == 0:
            ans = ans + st[i]
        else:
            if st[i] == '1':
                ans = ans + '0'
            else:
                ans = ans + '1'
    print(ans)
    for i in range(n):
        print(sp[i], end =' ')
    print()

# F of JifX96