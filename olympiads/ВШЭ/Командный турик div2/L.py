import itertools, sys

input = sys.stdin.readline

def solve():
    w = [input().strip() for _ in range(4)]
    for p in itertools.permutations(w):
        a, b, c, d = p
        for x in range(1, 10):
            if len(a) < x + 1 or len(b) < x + 1:
                continue
            for y in range(1, 10):
                if len(c) < y + 1 or len(d) < y + 1:
                    continue
                for i in range(1, len(a) - x + 1):
                    for j in range(1, len(b) - x + 1):
                        for k in range(1, len(c) - y + 1):
                            for l in range(1, len(d) - y + 1):
                                if (
                                    a[i - 1] == c[k - 1]
                                    and a[i + x - 1] == d[l - 1]
                                    and b[j - 1] == c[k + y - 1]
                                    and b[j + x - 1] == d[l + y - 1]
                                ):
                                    s1, s2, t1, t2 = 1, 1 + y, 1, 1 + x
                                    u1 = t1 - (i - 1)
                                    u2 = t1 - (j - 1)
                                    v1 = s1 - (k - 1)
                                    v2 = s1 - (l - 1)
                                    rs = set([s1, s2])
                                    for x in range(len(c)):
                                        rs.add(v1 + x)
                                    for x in range(len(d)):
                                        rs.add(v2 + x)
                                    cs = set([t1, t2])
                                    for x in range(len(a)):
                                        cs.add(u1 + x)
                                    for x in range(len(b)):
                                        cs.add(u2 + x)
                                    mr, xr = min(rs), max(rs)
                                    mc, xc = min(cs), max(cs)
                                    if xr - mr + 1 > 18 or xc - mc + 1 > 18:
                                        continue
                                    orr, oc = 1 - mr, 1 - mc
                                    s1 += orr
                                    s2 += orr
                                    v1 += orr
                                    v2 += orr
                                    u1 += oc
                                    u2 += oc
                                    t1 += oc
                                    t2 += oc
                                    g = [["." for _ in range(18)] for _ in range(18)]
                                    for x in range(len(a)):
                                        g[s1 - 1][u1 + x - 1] = a[x]
                                    for x in range(len(b)):
                                        g[s2 - 1][u2 + x - 1] = b[x]
                                    for x in range(len(c)):
                                        g[v1 + x - 1][t1 - 1] = c[x]
                                    for x in range(len(d)):
                                        g[v2 + x - 1][t2 - 1] = d[x]
                                    print("YES")
                                    for row in g:
                                        print("".join(row))
                                    return
    print("NO")


solve()
