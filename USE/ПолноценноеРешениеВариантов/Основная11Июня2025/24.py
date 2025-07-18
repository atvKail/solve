# with open("USE\\ПолноценноеРешениеВариантов\\Основная11Июня2025\\24_23281.txt", 'r') as f:
#     s = f.readline().strip()

# prefix2025 = [0] * len(s)
# prefixY = [0] * len(s)

# prefixY[0] = 1 if s[0] == 'Y' else 0

# posY = [i for i, ch in enumerate(s) if ch == 'Y']

# pref2025 = [0] * (len(s) + 1)
# for i in range(len(s)):
#     pref2025[i + 1] = pref2025[i]
#     if i >= 3 and s[i - 3:i + 1] == "2025":
#         pref2025[i + 1] += 1

# ans = -1
# for p in range(len(posY) - 80 + 1):
#     l = posY[p - 1] + 1 if p > 0 else 0
#     r = posY[p + 80] - 1 if (p + 80) < len(posY) else (len(s) - 1)

#     if r - l + 1 < 4:
#         continue

#     cnt2025 = pref2025[r - 3 + 1] - pref2025[l]
#     if cnt2025 >= 90:
#         ans = max(ans, r - l + 1)
# print(ans)


with open("USE\\ПолноценноеРешениеВариантов\\Основная11Июня2025\\24_23281.txt", 'r') as f:
    s = f.readline().strip()
n = len(s)
ys  = []
occ = []
best = 0
l = 0

for r in range(n):
    if r >= 3 and s[r-3:r+1] == "2025":
        occ.append(r-3)

    if s[r] == 'Y':
        ys.append(r)

    while len(ys) > 80:
        new_l = ys[0] + 1
        while ys and ys[0] < new_l:
            ys.pop(0)
        while occ and occ[0] < new_l:
            occ.pop(0)
        l = new_l

    if len(ys) == 80 and len(occ) >= 90:
        best = max(best, r - l + 1)
print(best)
