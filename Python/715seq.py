from itertools import *
class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        def exists(a, b):
            """checks if b exists in a as a subsequence"""
            pos = 0
            for ch in a:
                if pos < len(b) and ch == b[pos]:
                    pos += 1
            return pos == len(b)

        min_sum = float("inf")
        total = sum(ord(c) for c in s1) + sum(ord(c) for c in s2)
        if len(s1) > len(s2):
            s1, s2 = s2, s1
        for i in xrange(0, len(s1)+1):
            for ar in list(combinations(s1, i)):
                b = ''.join(ar)
                if exists(s2, b):
                    min_sum = min(min_sum, total - 2 * sum(ord(c) for c in b))
        return min_sum


print Solution().minimumDeleteSum("sea", "eat")
print Solution().minimumDeleteSum("delete", "leet")
print Solution().minimumDeleteSum("kslcclpmfd","guvjxozrjvzhe")
