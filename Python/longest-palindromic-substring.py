# Time:  O(n)
# Space: O(n)

# 5
# Given a string S, find the longest palindromic substring in S.
# You may assume that the maximum length of S is 1000,
#  and there exists one unique longest palindromic substring.
#

class Solution(object):
    def longestPalindrome(self, s): # USE THIS: space optimized
        if s == s[::-1]: # optimized from O(n^2)->O(n)
            return s

        n, ri, rj = len(s), 0, 0
        dp = [[False] * n for _ in range(2)]
        for i in reversed(range(n)):
            dp[i % 2][i] = True
            for j in range(i + 1, n):
                if s[i] == s[j] and (j == i + 1 or dp[(i + 1) % 2][j - 1] is True):
                    dp[i % 2][j] = True
                    if j - i > rj - ri:
                        ri, rj = i, j
                else:
                    # overwrite to False since we reuse the row. If a nxn matrix w/o
                    # space optimization, no need to set to False
                    dp[i % 2][j] = False

        return s[ri:rj + 1]

    # Manacher's Algorithm
    # http://leetcode.com/2011/11/longest-palindromic-substring-part-ii.html
    def longestPalindrome_manacher(self, s):
        """
        :type s: str
        :rtype: str
        """
        def preProcess(s):
            if not s:
                return ['^', '$']
            T = ['^']
            for c in s:
                T +=  ['#', c]
            T += ['#', '$']
            return T

        T = preProcess(s)
        P = [0] * len(T)
        center, right = 0, 0
        for i in xrange(1, len(T) - 1):
            i_mirror = 2 * center - i
            if right > i:
                P[i] = min(right - i, P[i_mirror])
            else:
                P[i] = 0

            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1

            if i + P[i] > right:
                center, right = i, i + P[i]

        max_i = 0
        for i in xrange(1, len(T) - 1):
            if P[i] > P[max_i]:
                max_i = i
        start = (max_i - 1 - P[max_i]) / 2
        return s[start : start + P[max_i]]



print(Solution().longestPalindrome("abb")) # bb
print(Solution().longestPalindrome("babad")) # aba

