data, mx = [], -100_001
with open("USE\\ПолноценноеРешениеВариантов\\Основная11Июня2025\\17_23276.txt") as f:
    triple = []
    for ch in f:
        num = int(ch.strip())
        if len(triple) < 3:
            triple.append(num)
        else:
            data.append(triple)
            triple = triple[1:] + [num]
        mx = max(mx, num if abs(num) % 100 == 25 else -100_001)
    data.append(triple)

cnt, mxsum = 0, -100_101 * 3
for triple in data:
    cnt_f = 0
    for t in triple:
        if len(str(abs(t))) == 4:
            cnt_f += 1
    if cnt_f <= 2 and sum(triple) <= mx:
        mxsum = max(mxsum, sum(triple))
        cnt += 1
print(cnt, mxsum)
