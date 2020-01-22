# Time:  O(k * n^2)
# Space: O(n^2)

# 1278 weekly contest 165 11/30/2019

# You are given a string s containing lowercase letters and an integer k. You need to :
#
#     First, change some characters of s to other lowercase English letters.
#     Then divide s into k non-empty disjoint substrings such that each substring is palindrome.
# Return the minimal number of characters that you need to change to divide the string.

# 1 <= k <= s.length <= 100

class Solution(object):
    def palindromePartition(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # dp1[i][j]: minimum number of changes to make s[i, j] palindrome
        dp1 = [[0]*len(s) for _ in xrange(len(s))]
        for l in xrange(1, len(s)+1):
            for i in xrange(len(s)-l+1):
                j = i+l-1
                if i == j-1:
                    dp1[i][j] = 0 if s[i] == s[j] else 1
                elif i != j:
                    dp1[i][j] = dp1[i+1][j-1] if s[i] == s[j] else dp1[i+1][j-1]+1

        # dp2[d][i]: minimum number of changes to divide s[0, i] into d palindromes
        dp2 = [[float("inf")]*len(s) for _ in xrange(2)]
        dp2[1] = dp1[0][:]
        for d in xrange(2, k+1):
            dp2[d%2] = [float("inf")]*len(s)
            for i in xrange(d-1, len(s)):  
                for j in xrange(d-2, i):
                    dp2[d%2][i] = min(dp2[d%2][i], dp2[(d-1)%2][j]+dp1[j+1][i])
        return dp2[k%2][len(s)-1]


    def palindromePartition_ming(self, s: str, k: int) -> int:
        if k == len(s): return 0
        n = len(s)
        lookup = [[False] * n for _ in range(n)]  # lookup[i][j] if s[i][j] is palindrome
        dp = [[float('inf')]*n for _ in range(k+1)]
        for i in range(n):
            dp[1][i] = 0
            b, e = i, n-1
            while b<e:
                if s[b] != s[e]:
                    dp[1][i] += 1
                b+=1
                e-=1
        for kk in range(2, k+1):
            dp[kk][n-1] = 0
            for i in reversed(range(n-1)):
                for j in range(i, n):
                    if s[i] == s[j]  and (j - i < 2 or lookup[i + 1][j - 1]):
                        lookup[i][j] = True
                        dp[kk][i] = min(dp[kk][i], dp[kk-1][j + 1] if j<n-1 else 0)
        return dp[k-1][0]

print(Solution().palindromePartition('abc', 2)) # 1
print(Solution().palindromePartition('aabbc', 3)) # 0
