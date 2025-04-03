import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    p = list(map(int, input().split()))

    d_list = [int(x) - 1 for x in input().split()]

    cycid = [-1] * n
    cycLen = []
    curr_cycle = 0
    for i in range(n):
        if cycid[i] == -1:
            cur = i
            cnt = 0
            while cycid[cur] == -1:
                cycid[cur] = curr_cycle
                cnt += 1
                cur = p[cur] - 1
            cycLen.append(cnt)
            curr_cycle += 1

    dmged = [False] * curr_cycle
    ttlOps = 0
    ress = []

    for d in d_list:
        cid = cycid[d]
        if not dmged[cid]:
            dmged[cid] = True
            ttlOps += cycLen[cid]
        ress.append(str(ttlOps))
    sys.stdout.write(" ".join(ress) + "\n")

# Solved
