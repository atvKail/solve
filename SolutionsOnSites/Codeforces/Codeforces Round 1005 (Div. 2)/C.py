# def build(seg, a, idx, l, r):
#     if l == r:
#         seg[idx] = a[idx]
#         return seg
#     mid = (l + r) // 2
#     build(seg, a, idx * 2, l, mid)
#     build(seg, a, idx * 2 + 1, mid + 1, r)
#     seg[idx] = max(seg[idx * 2], seg[idx * 2 + 1])


# def query(seg, idx, l, r, ql, qr):
#     if ql > r or qr < l:
#         return (-float("inf"), -1)
#     if ql <= l and r <= qr:
#         return seg[idx]
#     mid = (l + r) // 2
#     left_part = query(seg, idx * 2, l, mid, ql, qr)
#     right_part = query(seg, idx * 2 + 1, mid + 1, r, ql, qr)
#     return max(left_part, right_part)


def solve(m: int, a: list):
    idxpref = [0] * (m + 1)
    for i in range(1, m + 1):
        idxpref[i] = idxpref[i - 1] + (a[i - 1] if a[i - 1] > 0 else 0)

    negsuffix = [0] * (m + 2)
    for i in range(m - 1, -1, -1):
        negsuffix[i + 1] = negsuffix[i + 2] + (-a[i] if a[i] < 0 else 0)

    allPos = idxpref[m]
    allNeg = negsuffix[1]

    ans = max(allPos, allNeg)
    for x in range(0, m + 1):
        cur = idxpref[x] + negsuffix[x + 1]
        if cur > ans:
            ans = cur
    return str(ans)


results = []
for _ in range(int(input())):
    m = int(input())
    a = list(map(int, input().split()))
    results.append(solve(m, a))
print("\n".join(results))
