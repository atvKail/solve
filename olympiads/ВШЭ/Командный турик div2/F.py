import sys

input = sys.stdin.readline
INF = 10**30


n, K = map(int, input().split())
a = list(map(int, input().split()))

fmin, mmin = 0, 0
smin, m2 = INF, -1

res = 0
pref = 0
for x in a:
    pref += x
    r = pref % K

    if r != mmin:
        bprev = fmin
    else:
        bprev = smin

    if bprev != INF:
        res = max(res, pref - bprev)

    if r == mmin:
        if pref < fmin:
            fmin = pref

    elif r == m2:
        if pref < smin:
            smin = pref

    else:
        if pref < fmin:
            smin, m2, fmin, mmin = fmin, mmin, pref, r
        elif pref < smin:
            smin, m2 = pref, r

    if smin < fmin:
        fmin, smin, mmin, m2 = smin, fmin, m2, mmin
print(res)
