with open(
    file="USE\\ПолноценноеРешениеВариантов\\ИюньскийВариантN1ШастинБахтиеваКЕГЭ\\26_22605.txt",
    mode="r",
) as f:
    input = f.readline
    N_line = int(input().strip())
    N = int(N_line)

    timesbcell = {}
    for _ in range(N):
        line = input().split()
        if len(line) != 3:
            continue
        x = int(line[0])
        y = int(line[1])
        t = int(line[2])
        key = (x, y)
        if key in timesbcell:
            timesbcell[key].append(t)
        else:
            timesbcell[key] = [t]

binterval = 10**9
bx = 10**9
by = 10**9

for (x, y), times in timesbcell.items():
    if len(times) < 2:
        continue
    times.sort()

    cmin = times[1] - times[0]
    for i in range(2, len(times)):
        diff = times[i] - times[i - 1]
        if diff < cmin:
            cmin = diff

            if cmin == 0:
                break

    if cmin < binterval or (cmin == binterval and (x < bx or (x == bx and y < by))):
        binterval = cmin
        bx = x
        by = y

print(bx + by, binterval)
