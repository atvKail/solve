gl = "AE"
sg = "BCD"

with open("USE/24/24.txt", 'r') as f:
    s = f.read() + "00"

cnt = 0
max_cnt = -1

for i in range(1, len(s) - 2, 2):
    c1 = s[i] in gl
    c2 = s[i + 1] in sg
    if c1 and c2:
        cnt += 1
    else:
        max_cnt = max(max_cnt, cnt)
        cnt = 0
max_cnt = max(max_cnt, cnt)
cnt = 0

for i in range(0, len(s) - 2, 2):
    c1 = s[i] in gl
    c2 = s[i + 1] in sg
    if c1 and c2:
        cnt += 1
    else:
        max_cnt = max(max_cnt, cnt)
        cnt = 0
max_cnt = max(max_cnt, cnt)

print(max_cnt)