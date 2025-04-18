from itertools import product


ip = (125, 175, 0, 0)
mask = (255, 255, 128, 0)

bip = ["{0:08b}".format(i) for i in ip]
bmask = ["{0:08b}".format(i) for i in mask]

maskzeros = sum([i.count('0') for i in bmask])

print(bip)
print(bmask, maskzeros)

nip = [ip[i] & mask[i] for i in range(4)]
bnip = ["{0:08b}".format(i) for i in nip]

print(nip)
print(bnip)

cnt = 0
for p in product((1, 0), repeat=maskzeros):
    pones = p.count(1)
    sones = sum([i.count('1') for i in bnip]) + pones
    if sones % 5 == 0:
        cnt += 1
print(cnt)
