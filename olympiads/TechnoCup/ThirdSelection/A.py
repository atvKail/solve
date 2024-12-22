n = int(input())
seq = [int(input()) for _ in range(n)]
cones = seq.count(1)
if 0 in seq:
    miv = 0
else:
    miv = 1
mav = cones
print(mav, miv)
