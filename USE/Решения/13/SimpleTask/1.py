from itertools import product


ip = (204, 152, 228, 160)
mask = (255, 255, 255, 224)

bip = [bin(i)[2:] for i in ip]
bmask = [bin(i)[2:] for i in mask]

print(bip)
print(bmask)

zeros = [i.count('0') for i in bip]
ones = [i.count('1') for i in bip]

cnt = 0
for p in product((0, 1), repeat=bmask[-1].count('0')):
    onesp = p.count(1)
    zerosp = p.count(0)
    sones = sum(ones) + onesp
    szeros = sum(zeros) - 5 + zerosp

    if sones > szeros:
        cnt += 1
print(cnt)