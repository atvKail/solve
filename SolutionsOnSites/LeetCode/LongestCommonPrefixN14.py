class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = ''
        ps = strs[0]
        for i in range(len(min(strs, key=lambda x : len(x)))):
            for s in strs:
                if s[i] != ps[i]:
                    return prefix
                ps = s
            prefix += ps[i]
        return prefix