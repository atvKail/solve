def f(n):
    bn = bin(n)[2:]
    if (n & 1) == 0:
        bn = "10" + bn
    else:
        bn = "1" + bn + "01"
    return bn


minn = 1000001
for n in range(200):
    R = int(f(n), 2)
    if R > 177:
        minn = min(minn, n)
print(minn)
