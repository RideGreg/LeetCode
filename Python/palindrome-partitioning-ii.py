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
    def minCut(self, s): # USE THIS: only one double loop
        n = len(s)
        lookup = [[False] * n for _ in range(n)]  # lookup[i][j] if s[i][j] is palindrome
        dp = [n - 1 - i for i in range(n + 1)]  # dp[i] is minCut needed for substring s[i:]

        for i in reversed(range(n)):
            for j in range(i, n):
                if s[i] == s[j]  and (j - i < 2 or lookup[i + 1][j - 1]):
                    lookup[i][j] = True
                    dp[i] = min(dp[i], dp[j + 1] + 1)

        return dp[0]

    def minCut_forward(self, s):
        n = len(s)
        lookup = [[False] * n for _ in range(n)]
        for i in reversed(range(n)):
            for j in range(i, n):
                lookup[i][j] = (s[i] == s[j] and (j - i < 2 or lookup[i + 1][j - 1]))

        dp = [i - 1 for i in range(n + 1)]
        for j in range(2, n + 1):         # j = length of substring under consideration, map to char s[j-1]
            for i in range(j):            # i = start position of postfix substring
                if lookup[i][j - 1]:      # substring s[i,j-1] is palindrome
                    dp[j] = min(dp[j], dp[i] + 1)
        return dp[n]

    # TLE O(n^3). Calculate minCut for every substring s[i][j].
    # isPalindrome and minCut are not saved in separate tables.
    def minCut_ming(self, s):
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in reversed(range(n - 1)):
            for j in range(i + 1, n):

                if s[i] != s[j] or (j > i + 1 and dp[i + 1][j - 1]):
                    dp[i][j] = min(dp[i][k] + dp[k + 1][j] + 1 for k in range(i, j))
        return dp[0][-1]

if __name__ == "__main__":
    print(Solution().minCut("aab"))