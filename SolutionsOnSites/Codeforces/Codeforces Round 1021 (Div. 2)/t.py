from fractions import Fraction
import sys

input = sys.stdin.readline


t = int(input())
for _ in range(t):
    n, x, y, vx, vy = map(int, input().split())
    x, y = Fraction(x), Fraction(y)
    count = 0
    seen = set()
    
    while True:
        state = (x, y, vx, vy)
        if (x == 0 and y == 0) or (x == 0 and y == n) or (x == n and y == 0):
            print(count)
            break
        if state in seen:
            print(-1)
            break
        seen.add(state)
        
        t_x = Fraction(-y, vy) if vy < 0 else Fraction(10**18)
        t_y = Fraction(-x, vx) if vx < 0 else Fraction(10**18)
        t_h = Fraction(n - x - y, vx + vy) if vx + vy > 0 else Fraction(10**18)
        
        t = min(t_x, t_y, t_h)
        if t <= 0:
            continue

        x_new = x + vx * t
        y_new = y + vy * t

        if (x_new == 0 and y_new == 0) or (x_new == 0 and y_new == n) or (x_new == n and y_new == 0):
            print(count)
            break

        count += 1
        x, y = x_new, y_new
        if t == t_x:
            vy = -vy
        elif t == t_y:
            vx = -vx
        else:
            vx, vy = -vy, -vx
