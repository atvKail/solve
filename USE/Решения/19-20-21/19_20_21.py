# operations = [
#     lambda a, b: [a + 1, b],
#     lambda a, b: [a * 2, b],
#     lambda a, b: [a, b + 1],
#     lambda a, b: [a, b * 2]
# ]


# def f(heaps: list[int], m: int) -> bool:
#     if sum(heaps) >= 81:
#         return not m & 1
#     if m == 0:
#         return 0
#     variants = [f(op(*heaps), m - 1) for op in operations]
#     return all(variants) if not m & 1 else any(variants)


# print([x for x in range(24, 471) if f(x, 2)])
# print([x for x in range(24, 471) if not f(x, 1) and f(x, 3)])
# print([x for x in range(24, 471) if not f(x, 2) and f(x, 4)])


# operations = [
#     lambda x: x + 3,
#     lambda x: x + 6,
#     lambda x: x * 3
# ]


# def f(h: int, m: int) -> bool:
#     if h >= 132:
#         return not m & 1
#     if m == 0:
#         return 0
#     variants = [f(op(h), m - 1) for op in operations]
#     return all(variants) if not m & 1 else any(variants)


# print(19, [i for i in range(1, 132) if f(i, 2)])
# print(20, [i for i in range(1, 132) if not f(i, 1) and f(i, 3)])
# print(21, [i for i in range(1, 132) if not f(i, 2) and f(i, 4)])


# operations = [
#     lambda x: x + 1,
#     lambda x: x + 6,
#     lambda x: x * 2
# ]


# def f(h: int, m: int) -> bool:
#     if h >= 103:
#         return not m & 1
#     if m == 0: 
#         return 0
#     var = [f(op(h), m - 1) for op in operations]
#     return all(var) if not m & 1 else any(var)


# print(19, [i for i in range(1, 103) if f(i, 2)])
# print(20, [i for i in range(1, 103) if not f(i, 1) and f(i, 3)])
# print(21, [i for i in range(1, 103) if not f(i, 2) and f(i, 4)])


# operations = [
#     lambda a, b: [a - 3, b],
#     lambda a, b: [a // 2 + a % 2, b],
#     lambda a, b: [b - 3, a][::-1],
#     lambda a, b: [b // 2 + b % 2, a][::-1]
# ]


# def f(h: list[int], m: int) -> bool:
#     if sum(h) <= 72:
#         return not m & 1
#     if m == 0:
#         return 0
#     var = [f(op(*h), m - 1) for op in operations]
#     return all(var) if not m & 1 else any(var)


# def g(h: list[int], m: int) -> bool:
#     if sum(h) <= 72:
#         return not m & 1
#     if m == 0:
#         return 0
#     var = [f(op(*h), m - 1) for op in operations]
#     return any(var) if not m & 1 else any(var)


# print(19, [i for i in range(23, 150) if g([50, i], 2)])
# print(20, [i for i in range(23, 150) if not f([50, i], 1) and f([50, i], 3)])
# print(21, [i for i in range(23, 150) if not f([50, i], 2) and f([50, i], 4)])


