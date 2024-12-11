g = int(input())
c = int(input())

exc = {}
for _ in range(c):
    g1, g2, r = map(int, input().split())
    exc[(g1, g2)] = r
    exc[(g2, g1)] = r

n = int(input())
pcgs = list(map(int, input().split()))

stck = []

for purchase in pcgs:
    stck.append(purchase)

    while True:
        if len(stck) >= 2:
            top1 = stck[-1]
            top2 = stck[-2]
            if top1 == top2:
                stck.pop()
            elif (top1, top2) in exc:
                stck.pop()
                stck.pop()
                stck.append(exc[(top1, top2)])
            else:
                break
        else:
            break

print(len(stck))
print(*stck)
