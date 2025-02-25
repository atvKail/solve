t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    dcnt = s.count("-")
    undcnt = s.count("_")

    if dcnt < 2 or undcnt == 0:
        print(0)
        continue
    
    l = dcnt // 2
    r = (dcnt + 1) // 2

    print(undcnt * l * r)
