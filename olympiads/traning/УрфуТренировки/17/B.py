def prefix_function(s):
    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi


def longest_palindrome_prefix(mid):
    temp = mid + "#" + mid[::-1]
    pi = prefix_function(temp)
    length = pi[-1]
    return mid[:length]


def longest_palindrome_suffix(mid):
    rev_mid = mid[::-1]
    temp = rev_mid + "#" + mid
    pi = prefix_function(temp)
    length = pi[-1]
    return mid[len(mid) - length :]


def solve(s):
    n = len(s)
    l, r = 0, n - 1
    while l < r and s[l] == s[r]:
        l += 1
        r -= 1

    if l >= r:
        return s
    else:
        prefix = s[:l]
        suffix = s[r + 1 :]
        mid = s[l : r + 1]
        cand1 = longest_palindrome_prefix(mid)
        cand2 = longest_palindrome_suffix(mid)
        if len(cand1) >= len(cand2):
            midpal = cand1
        else:
            midpal = cand2
        return prefix + midpal + suffix


results = []
for i in range(int(input())):
    results.append(solve(input()))
print("\n".join(results))
