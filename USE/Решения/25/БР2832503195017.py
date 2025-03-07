cnt = 0
for x in range(650000 + 1, 10, -1):
    d = x // 2
    for j in range(19, d + 1):
        if x % j == 0 and j % 10 == 9:
            print(x, j)
            cnt += 1
            break
    if cnt == 10:
        break

# print(chr(sum(range(ord(min(str(not())))))))
