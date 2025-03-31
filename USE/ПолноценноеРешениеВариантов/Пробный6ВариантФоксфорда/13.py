def dto2b8(n: int) -> str:
    d2b8 = ""
    while n != 0:
        d2b8 += str(n % 2)
        n //= 2
    return "0" * (8 - len(d2b8)) + d2b8[::-1]


ip = (dto2b8(105), dto2b8(196), dto2b8(0), dto2b8(0))
ips_valid = set()
ips_valid.add(ip)
print(ips_valid)
for i in range(1, 255):
    for j in range(1, 255):
        nip = ip[0], ip[1], ip[2], dto2b8(i), dto2b8(j)
        ip_str = "".join(list(nip))
        if (ip_str.count("1")) & 1 == 0:
            ips_valid.add(nip)
print(len(ips_valid))
