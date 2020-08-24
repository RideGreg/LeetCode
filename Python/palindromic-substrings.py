# Time:  O(n)
# Space: O(n)

# 647
# Given a string, your task is to count how many palindromic substrings in this string.
#
# The substrings with different start indexes or end indexes are counted as
# different substrings even they consist of same characters.
#
# Example 1:
# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# Example 2:
# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
# Note:
# The input string length won't exceed 1000.

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def manacher(s):
            s = '^#' + '#'.join(s) + '#$'
            P = [0] * len(s)
            C, R = 0, 0
            for i in xrange(1, len(s) - 1):
                i_mirror = 2*C-i
                if R > i:
                    P[i] = min(R-i, P[i_mirror])
                while s[i+1+P[i]] == s[i-1-P[i]]:
                    P[i] += 1
                if i+P[i] > R:
                    C, R = i, i+P[i]
            return P
        return sum((max_len+1)//2 for max_len in manacher(s))

    # expand from center Time O(n^2) Space O(1)
    def countSubstrings2(self, s):
        def countPalindrome(i, j):
            while 0 <= i and j < len(s) and s[i] == s[j]:
                i, j = i - 1, j + 1
            i += 1
            j -= 1
            length = j - i + 1
            return (length + 1) // 2
        
        return sum(countPalindrome(i,i) + countPalindrome(i, i+1) for i in range(len(s)))

    # DP Time O(n^2) Space O(n)
    def countSubstrings_dp(self, s: str) -> int:
        n, ans = len(s), 0
        dp = [False] * n
        for i in reversed(range(n)):
            for j in reversed(range(i, n)):
                dp[j] = False
                if s[j] == s[i]:
                    if j <= i + 1 or dp[j-1] == True:
                        dp[j] = True
                        ans += 1
        
        return ans

print(Solution().countSubstrings('aaa')) # 6