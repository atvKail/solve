# Неудобство, будет inc от inconvenience
n, k = map(int, input().split())
secFlr = input().strip()
FirFlr = input().strip()

tms = []

for i in range(n):
    if secFlr[i] == '1':
        tms.append((2, i + 1))  # 2, t - i+1

for i in range(n):
    if FirFlr[i] == '1':
        tms.append((1, i + 1))  # 1, t - i+1

mimaInc = float('inf')
bestp = None

for prtFlr in [1, 2]:
    for prtTbl in range(1, n + 1):
        maxInc = 0

        for floor, table in tms:
            if floor == prtFlr:
                inc = abs(table - prtTbl)
            else:
                inc = table + k + prtTbl

            maxInc = max(maxInc, inc)
        if maxInc < mimaInc:
            mimaInc = maxInc
            bestp = (prtFlr, prtTbl)

print(mimaInc)
print(*bestp)
