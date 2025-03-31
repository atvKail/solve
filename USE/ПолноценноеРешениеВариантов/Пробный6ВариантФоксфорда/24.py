symbols = "ABCDE"
g, s = "AE", "BCD"

with open("USE\\ПолноценноеРешениеВариантов\\Пробный6ВариантФоксфорда\\24.txt") as f:
    inps = f.read().strip()

prev = inps[:2]
idx, n = 2, len(inps)
maxcnt = -1
cnt = 0
while idx <= n - 1:
    if prev[0] in g and prev[1] in s:
        prev = inps[idx] + inps[idx + 1]
        idx += 2
        cnt += 1
    else:
        prev = prev[1] + inps[idx]
        idx += 1
        maxcnt = max(maxcnt, cnt)
        cnt = 0
print(maxcnt)
