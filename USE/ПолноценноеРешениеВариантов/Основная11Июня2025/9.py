from collections import Counter


data = []
with open("USE\\ПолноценноеРешениеВариантов\\Основная11Июня2025\\9_23268.csv", 'r') as f:
    while (line:=f.readline()) != '':
        data.append(list(map(int, line.strip().split('|'))))

i = 1
for x in data:
    ctr = Counter(x).most_common()
    pov, nepov = [], []
    flg = False
    cnt = 0
    for ch, ln in ctr:
        if ln == 2 and cnt < 3:
            pov.append(ch)
            cnt += 1
        else:
            if cnt > 3 or ln > 2:
                flg = True
                break
            else:
                nepov.append(ch)
    if not flg and len(pov) == 2 and len(nepov) == 3:
        if sum(pov) / 2 < max(nepov):
            print(i)
            break
    i += 1