from itertools import product


ip = (136, 34, 24, 16)
mask = (255, 255, 255, 248)

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
    if ''.join([str(i) for i in p]) != "111":
        cnt += 1
print(cnt)
