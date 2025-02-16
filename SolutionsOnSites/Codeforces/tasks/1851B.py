for _ in range(int(input())):
    n = int(input().strip())
    a = list(map(int, input().split()))
    
    sorted_a = sorted(a)
    possible = True
    for i in range(n):
        if sorted_a[i] % 2 != a[i] % 2:
            possible = False
            break

    print("YES" if possible else "NO")
