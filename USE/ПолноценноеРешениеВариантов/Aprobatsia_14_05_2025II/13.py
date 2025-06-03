ip = (196, 154, 199, 107)
mask = (255, 248, 0, 0)

print(["{:08b}".format(i) for i in ip])
print(["{:08b}".format(i) for i in mask])

nip = ['11000100', '10011111', '11111111', '11111110']
print(''.join([str(int(i, 2)) for i in nip]))