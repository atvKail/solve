n = int(input())
a = list(map(int, input().split()))

negative = 0
zero = 0
posit = 0
pos = 0
neg = 0

lastZeroIdx = -1

for i in range(n):
    if a[i] == 0:
        zero += (i - lastZeroIdx) * (n - i)
        pos = 0
        neg = 0
        lastZeroIdx = i
    elif a[i] > 0:
        pos += 1
        posit += pos
        negative += neg
    else:  # a[i] < 0
        pos, neg = neg, pos + 1
        posit += pos
        negative += neg

print(negative, zero, posit)
