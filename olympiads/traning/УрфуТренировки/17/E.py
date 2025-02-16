from itertools import*
for i in range(int(input())):
    n = int(input())
    for i in product("abcdefghijklmnopqrstuvwxyz", repeat=3):
        ans = 0
        for j in i:
            ans += ord(j) - 96
        if ans == n:
            print(*i, sep='')
            break

# solution of Daniil15