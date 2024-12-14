res = ""
for _ in range(int(input())):
    n = int(input())
    row = list(input().strip())
    stack = []

    for ch in row:
        while stack and abs(ord(stack[-1]) - ord(ch)) == 1:
            if stack[-1] < ch:
                ch = stack.pop()
            else:
                stack.pop()
        stack.append(ch)

    res += "".join(stack) + '\n'

print(res[:-1])
