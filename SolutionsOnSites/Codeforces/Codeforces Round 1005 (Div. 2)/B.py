def solve(n, a):
    freq = {}
    for x in a:
        freq[x] = freq.get(x, 0) + 1

    bstl, bstr = 0, 0
    bstlen = 0

    currl = None
    currlen = 0
    for i in range(n):
        if freq[a[i]] == 1:
            if currl is None:
                currl = i
                currlen = 1
            else:
                currlen += 1
        else:
            if currl is not None:
                if currlen > bstlen:
                    bstlen = currlen
                    bstl, bstr = currl, i - 1
                currl = None
                currlen = 0
    if currl is not None:
        if currlen > bstlen:
            bstlen = currlen
            bstl, bstr = currl, n - 1

    if bstlen == 0:
        return "0"
    else:
        return f"{bstl + 1} {bstr + 1}"


results = []
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    results.append(solve(n, a))
print("\n".join(results))
