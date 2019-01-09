# Time:  O(m + n)
# Space: O(1)
#
# 161
# Given two strings S and T, determine if they are both one edit distance apart.
#

class Solution(object):
    def isOneEditDistance(self, s, t):
        m, n = len(s), len(t)
        if m > n:
            return self.isOneEditDistance(t, s)

        if n - m > 1: return False
        elif n - m == 0:
            diff = 0
            for i in xrange(m):
                if s[i] != t[i]:
                    diff += 1
                if diff > 1:
                    return False
            return diff == 1
        else:
            i, j = 0, 0
            while i < m and s[i] == t[j]:
                i, j = i + 1, j + 1
            if i == m: return True
            j += 1
            while i < m and s[i] == t[j]:
                i, j = i + 1, j + 1
            return i == m

    def isOneEditDistance_kamyu(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m, n = len(s), len(t)
        if m > n:
            return self.isOneEditDistance(t, s)
        if n - m > 1:
            return False

        i, shift = 0, n - m
        while i < m and s[i] == t[i]:
            i += 1
        if shift == 0:
            i += 1
        while i < m and s[i] == t[i + shift]:
            i += 1

        return i == m


if __name__ == "__main__":
    print Solution().isOneEditDistance("teacher", "acher") # False
    print Solution().isOneEditDistance("acher", "acher") # False
    print Solution().isOneEditDistance("", "") # False
