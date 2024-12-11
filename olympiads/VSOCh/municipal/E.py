def chk(dlta):
    miv = [rgs[i][0] for i in range(n)]
    mav = [rgs[i][1] for i in range(n)]

    for i in range(1, n):
        miv[i] = max(miv[i], miv[i-1] - dlta)
        mav[i] = min(mav[i], mav[i-1] + dlta)

    for i in range(n - 2, -1, -1):
        miv[i] = max(miv[i], miv[i+1] - dlta)
        mav[i] = min(mav[i], mav[i+1] + dlta)

    for i in range(n):
        if miv[i] > mav[i]:
            return False
    return True


n = int(input())
rgs = [tuple(list(map(int, input().split()))) for _ in range(n)]

l, r = 0, 2 * 10**9
bst_dlta = -1
bst_vl = []

while l <= r:
    mid = (l + r) // 2
    if chk(mid):
        bst_dlta = mid
        r = mid - 1
    else:
        l = mid + 1

miv = [rgs[i][0] for i in range(n)]
mav = [rgs[i][1] for i in range(n)]

for i in range(1, n):
    miv[i] = max(miv[i], miv[i-1] - bst_dlta)
    mav[i] = min(mav[i], mav[i-1] + bst_dlta)

for i in range(n - 2, -1, -1):
    miv[i] = max(miv[i], miv[i+1] - bst_dlta)
    mav[i] = min(mav[i], mav[i+1] + bst_dlta)

bst_vl = [miv[i] for i in range(n)]

print(bst_dlta)
print(*bst_vl)
