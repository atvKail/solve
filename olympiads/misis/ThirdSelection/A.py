for _ in range(int(input())):
    n = int(input())
    x = (1000 - n) // 7 if -(1000 - n) // 7 * -1 == (1000 - n) // 7 and (1000 - n) // 7 != 0  else -1
    print(x)