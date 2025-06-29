with open("USE\\ПолноценноеРешениеВариантов\\Основная10Июня2025\\24_23206.txt", 'r') as f:
    s = f.readline().strip()

n = len(s)
mxlen = 0
i = 0
while i < n:
    if s[i] not in "02468":
        i += 1
        continue

    j = i + 1
    cnts = 0
    while j < n and s[j] not in "02468":
        if s[j] == "S":
            cnts += 1
        j += 1

    cnts = 0
    k = i
    for k in range(i, j):
        if s[k] == "S":
            cnts += 1
        if cnts == 35:
            mxlen = max(mxlen, k - i + 1)
        if cnts > 35:
            break
    i += 1
print(mxlen)