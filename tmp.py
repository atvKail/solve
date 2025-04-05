def solve(N, K, A, M, T):
    if T < M:
        return "No"

    L = T // M
    ttlp = N * K

    if (T - M) // A >= N:
        return "Yes"

    l, r = 0, min(L, ttlp)
    while l <= r:
        mid = (l + r) // 2
        badcnt = 0
        for i in range(1, N + 1):
            if T - i * A <= 0:
                bpos = mid
            else:
                fbk = (T - i * A) // M + 1
                bpos = max(0, mid - fbk + 1)
            badcnt += min(K, bpos)
            if badcnt > mid:
                break

        if badcnt >= mid:
            l = mid + 1
        else:
            r = mid - 1

    mid = r
    if mid < min(L, ttlp):
        return "Yes"
    else:
        return "No"


N = int(input())
K = int(input())
A = int(input())
M = int(input())
T = int(input())

print(solve(N, K, A, M, T))
