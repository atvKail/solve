from sympy import symbols, Eq, solve, pi  # noqa: E402


a, b, c, d = symbols('a b c d')
x = symbols('x')

equations = [
    Eq(24*(2 - 100)**3 - (a*2**3 + b*2**2 + c*2 + d), 3*pi),
    Eq(24*(3 - 100)**3 - (a*3**3 + b*3**2 + c*3 + d), 3*pi),
    Eq(24*(4 - 100)**3 - (a*4**3 + b*4**2 + c*4 + d), 3*pi),
    Eq(24*(5 - 100)**3 - (a*5**3 + b*5**2 + c*5 + d), 3*pi)
]

solution = solve(equations, [a, b, c, d])
print(solution)
