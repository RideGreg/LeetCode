# Time:  O(n^2)
# Space: O(n)

# 1216 biweekly contest 10 10/5/2019

# Given a string s and an integer k, find out if the given string is a K-Palindrome or not.
# A string is K-Palindrome if it can be transformed into a palindrome by removing at most k characters from it.

# 1 <= s.length <= 1000
# s has only lowercase English letters.
# 1 <= k <= s.length

class Solution(object):
    def isValidPalindrome(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        if s == s[::-1]:  # optional, to optimize special case
            return True

        N = len(s)
        dp = [1] * N
        for i in range(N-2, -1, -1):
            ndp = [1] * N
            for j in range(i+1, N):
                if s[i] == s[j]:
                    ndp[j] = 2 + dp[j-1] if j > i + 1 else 2
                else:
                    ndp[j] = max(ndp[j-1], dp[j])
            dp = ndp
        return N - dp[-1] <= k

        '''
        dp = [[1] * len(s) for _ in xrange(2)]
        for i in reversed(xrange(len(s))):
            for j in xrange(i+1, len(s)):
                if s[i] == s[j]:
                    dp[i%2][j] = 2 + dp[(i+1)%2][j-1] if i+1 < j else 2
                else:
                    dp[i%2][j] = max(dp[(i+1)%2][j], dp[i%2][j-1])
        return len(s) - dp[0][-1] <= k'''

print(Solution().isValidPalindrome("abcdeca", 2)) # True
