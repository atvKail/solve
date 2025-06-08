def dto2(n: int) -> str:
    s = ""
    while n:
        s = str(n % 2) + s
        n //= 2
    return s


cnt = 0
for j in range(192, 256):
    for i in range(0, 256):
        # if j == 192 and i == 0:
        #     continue
        # if j == 255 and i == 255:
        #     continue
        if i % 2 == 0:
            continue
        bip = (
            dto2(172).zfill(8)
            + dto2(16).zfill(8)
            + dto2(j).zfill(8)
            + dto2(i).zfill(8)
        )
        if bip.count("1") % 3 == 0:
            cnt += 1
print(cnt)
