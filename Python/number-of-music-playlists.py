# Time:  O(n * l)
# Space: O(l)

# Another better solution (generating function), you could refer to 
# https://leetcode.com/problems/number-of-music-playlists/solution/

# Your music player contains N different songs and she wants to listen to
# L (not necessarily different) songs during your trip.
# You create a playlist so that:
#
# Every song is played at least once
# A song can only be played again only if K other songs have been played
# Return the number of possible playlists.
# As the answer can be very large, return it modulo 10^9 + 7.
#
# Example 1:
#
# Input: N = 3, L = 3, K = 1
# Output: 6
# Explanation: There are 6 possible playlists.
#              [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1].
# Example 2:
#
# Input: N = 2, L = 3, K = 0
# Output: 6
# Explanation: There are 6 possible playlists.
#              [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2, 1], [2, 1, 2], [1, 2, 2]
# Example 3:
#
# Input: N = 2, L = 3, K = 1
# Output: 2
# Explanation: There are 2 possible playlists. [1, 2, 1], [2, 1, 2]
#
# Note:
# 0 <= K < N <= L <= 100

# Dynamic programming
# Let dp[n][l] be the number of playlists of length l that have exactly n unique songs. Want dp[N][L].
# For dp[n][l]: the song at position l can be either a new song or a played song. If a new song, last state is # of
# playlists of length l-1 with n-1 unique songs, then we had dp[n-1][l-1] * n ways to choose it. If a played song,
# then we repeated a previous song in dp[n][l-1] * max(n-K, 0) ways (total n songs, except the last K ones played are banned.)

class Solution(object):
    def numMusicPlaylists(self, N, L, K):
        """
        :type N: int
        :type L: int
        :type K: int
        :rtype: int
        """
        M = 10**9+7
        dp = [[0] * (1+L) for _ in xrange(2)]
        dp[0][0] = dp[1][1] = 1
        for n in xrange(1, N+1):
            dp[n % 2][n] = (dp[(n-1) % 2][n-1] * n) % M         # for n==l: factorial n!
            for l in xrange(n+1, L+1):                          # ignore lower triangle since N<=L
                dp[n % 2][l] = (dp[n % 2][l-1] * max(n-K, 0) +  # repeat one of previous n-K songs
                                dp[(n-1) % 2][l-1] * n)         # new song: have 1 more song compared to dp[i-1][j-1], the new song can be any of n songs
                dp[n % 2][l] %= M
        return dp[N % 2][L]

    from functools import lru_cache # in Python 3
    def numMusicPlaylists_LeetCodeOfficial(self, N, L, K):
        @lru_cache(None)
        def dp(i, j):
            if i == 0:
                return +(j == 0)
            ans = dp(i-1, j-1) * (N-j+1)
            ans += dp(i-1, j) * max(j-K, 0)
            return ans % (10**9+7)

        return dp(L, N)
print(Solution().numMusicPlaylists(3,3,1)) # 6: dp=[[1 0 0 0], [0 1 0 0], [0 0 2 2], [0 0 0 6]]
print(Solution().numMusicPlaylists(2,3,0)) # 6: dp=[[1 0 0 0], [0 1 1 1], [0 0 2 6]]
print(Solution().numMusicPlaylists(2,3,1)) # 2: dp=[[1 0 0 0], [0 1 0 0], [0 0 2 2]]