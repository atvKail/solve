from collections import Counter


cnt = 0
with open("USE\\ПолноценноеРешениеВариантов\\НовыйМайскийВарианN6_2025\\09.txt", "r+") as f:
    for line in f.readlines():
        n = 6
        a = list(map(int, line.strip('п»ї').split(';')))
        # print(a)
        ok = 1

        # cond 1
        ok &= (len(set(a)) != 1 and len(set(a)) != len(a))
        
        #cond 2
        repa = []
        unrepa = []
        ctr = Counter(a)
        for x in a:
            if ctr[x] > 1:
                repa += [x]
            else:
                unrepa += [x]
        ok &= (sum(repa) / (len(repa) if len(repa) != 0 else 1) < sum(unrepa) / (len(unrepa) if len(unrepa) != 0 else 1))

        if ok:
            cnt += 1
print(cnt)
