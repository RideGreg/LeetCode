# Time:  O(n^2)
# Space: O(n)

# 877
# Alex and Lee play a game with piles of stones.
# There are an even number of piles arranged in a row,
# and each pile has a positive integer number of stones piles[i].
#
# The objective of the game is to end with the most stones.
# The total number of stones is odd, so there are no ties.
#
# Alex and Lee take turns, with Alex starting first.
# Each turn, a player takes the entire pile of stones from
# either the beginning or the end of the row.
# This continues until there are no more piles left,
# at which point the person with the most stones wins.
#
# Assuming Alex and Lee play optimally,
# return True if and only if Alex wins the game.
#
# Example 1:
#
# Input: [5,3,4,5]
# Output: true
# Explanation: 
# Alex starts first, and can only take the first 5 or the last 5.
# Say he takes the first 5, so that the row becomes [3, 4, 5].
# If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.
# If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.
# This demonstrated that taking the first 5 was a winning move for Alex, so we return true.
#
# Note:
# - 2 <= piles.length <= 500
# - piles.length is even.
# - 1 <= piles[i] <= 500
# - sum(piles) is odd.

# The solution is the same as https://leetcode.com/problems/predict-the-winner/description/
class Solution(object):
    def stoneGame(self, piles): # USE THIS, easy to understand
        """
        :type piles: List[int]
        :rtype: bool
        """
        if len(piles) % 2 == 0 or len(piles) == 1:
            return True

        prefixsum = [0]
        for p in piles:
            prefixsum.append(prefixsum[-1] + p)

        n = len(piles)
        dp = [0] * n
        for i in reversed(xrange(n)):
            for j in xrange(i, n):
                if i == j:
                    dp[j] = piles[j]
                else:
                    dp[j] = prefixsum[j + 1] - prefixsum[i] - min(dp[j], dp[j - 1])
        return dp[-1] * 2 > prefixsum[-1]

    def stoneGame_kamyu(self, piles):
        if len(piles) % 2 == 0 or len(piles) == 1:
            return True

        dp = [0] * len(piles)
        for i in reversed(xrange(len(piles))):
            dp[i] = piles[i]
            for j in xrange(i+1, len(piles)):
                dp[j] = max(piles[i] - dp[j], piles[j] - dp[j - 1])
        return dp[-1] >= 0
