ip = [205, 99, 68, 249]
mask = [255, 255, 248, 0]

ip = ["{:08b}".format(i) for i in ip]
mask = ["{:08b}".format(i) for i in mask]

print(ip, mask, sep="\n")

ans = int(ip[0], 2), int(ip[1], 2), int("01000111", 2), int("11111111", 2) - 1
print(*ans, sep='.')
print(*ans, sep="")

# Ответ: 2059971254