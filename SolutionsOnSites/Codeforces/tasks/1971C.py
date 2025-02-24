def gr_to_radian(n):
    import math

    return n / 180 * math.pi


def get_point(hour, pi_cond):
    import math

    angle_deg = pi_cond[hour]
    angle_rad = gr_to_radian(angle_deg)
    return (math.cos(angle_rad), math.sin(angle_rad))


def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def main():
    import sys

    input = sys.stdin.readline

    pi_cond = {
        1: 60,
        2: 30,
        3: 0,
        4: -30,
        5: -60,
        6: -90,
        7: -120,
        8: -150,
        9: 180,
        10: 150,
        11: 120,
        12: 90,
    }

    t = int(input().strip())
    results = []
    for _ in range(t):
        a, b, c, d = map(int, input().strip().split())
        A = get_point(a, pi_cond)
        B = get_point(b, pi_cond)
        C = get_point(c, pi_cond)
        D = get_point(d, pi_cond)

        if cross(A, B, C) * cross(A, B, D) < 0 and cross(C, D, A) * cross(C, D, B) < 0:
            results.append("YES")
        else:
            results.append("NO")

    print("\n".join(results))


if __name__ == "__main__":
    main()
