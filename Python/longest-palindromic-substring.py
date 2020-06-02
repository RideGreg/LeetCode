# Time:  O(n) Manacher's Algorithm, O(n^2) dynamic programming
# Space: O(n)

# 5
# Given a string S, find the longest palindromic substring in S.
# You may assume that the maximum length of S is 1000,
#  and there exists one unique longest palindromic substring.
#

class Solution(object):
    # 中心扩展算法 Time O(n^2)：长度为1和2的回文中心各有n和n−1个，每个回文中心最多会向外扩展O(n)次，
    # Space O(1)
    # 借鉴动态规划状态方程 P[i,j] = P[i+1,j-1] && Si==Sj，从最短串边界情况开始，可找出所有palindrome substring.
    # 枚举所有的「回文中心」并尝试扩展，直到无法扩展为止，此时的回文串长度即为此「回文中心」下的最长
    # 回文串长度，对所有的长度求出最大值。
    def longestPalindrome(self, s: str) -> str: # USE THIS
        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        start, end = 0, 0
        for i in range(len(s)):
            left1, right1 = expandAroundCenter(i, i)
            left2, right2 = expandAroundCenter(i, i + 1)
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start: end + 1]

    # Dynamic Programming: time O(n^2) space optimized O(n)
    def longestPalindrome_dp(self, s):
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

    # Manacher's Algorithm O(n)
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

