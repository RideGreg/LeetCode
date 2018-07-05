# Time:  O(n^2)
# Space: O(n^2)
#
# Given a string s, partition s such that every substring of the partition is a palindrome.
#
# Return the minimum cuts needed for a palindrome partitioning of s.
#
# For example, given s = "aab",
# Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
#

class Solution:
    # @param s, a string
    # @return an integer
    def minCut_backward(self, s):
        lookup = [[False for j in xrange(len(s))] for i in xrange(len(s))]
        mincut = [len(s) - 1 - i for i in xrange(len(s) + 1)]

        for i in reversed(xrange(len(s))):
            for j in xrange(i, len(s)):
                if s[i] == s[j]  and (j - i < 2 or lookup[i + 1][j - 1]):
                    lookup[i][j] = True
                    mincut[i] = min(mincut[i], mincut[j + 1] + 1)

        return mincut[0]

    def minCut(self, s): # USE THIS: forward DP easy to follow
        n = len(s)
        lookup = [[False] * n for _ in xrange(n)]
        for i in reversed(xrange(n)):
            for j in xrange(i, n):
                lookup[i][j] = (s[i] == s[j] and (j - i < 2 or lookup[i + 1][j - 1]))

        dp = [i - 1 for i in xrange(n + 1)]
        for j in xrange(2, n + 1):
            for i in xrange(1, j + 1):
                if lookup[i - 1][j - 1]:    # substring s[i,j] is palindrome
                    dp[j] = min(dp[j], dp[i - 1] + 1)
        return dp[n]

if __name__ == "__main__":
    print Solution().minCut("aab")