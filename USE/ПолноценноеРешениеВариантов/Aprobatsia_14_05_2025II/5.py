def f(n: int) -> int:
    bn = bin(n)[2:]
    sbn = sum(map(int, list(bn)))
    bn += str(sbn % 2)
    bn += str((sbn + int(bn[-1])) % 2)
    return int(bn, 2)
    

minn = [100001, -1]
for n in range(100):
    if (x:=f(n)) > 64:
        minn = min([n, x], minn, key=lambda x: x[0])
print(minn)
