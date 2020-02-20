# Time:  O(n*(logn)^2)
# Space: O(nlogn)

# 1140 weekly contest 147 7/27/2019

# Alex and Lee continue their games with piles of stones.  There are a number of piles arranged in a row,
# and each pile has a positive integer number of stones piles[i].  The objective of the game is
# to end with the most stones.
#
# Alex and Lee take turns, with Alex starting first.  Initially, M = 1.
# On each player's turn, that player can take all the stones in the first X remaining piles,
# where 1 <= X <= 2M.  Then, we set M = max(M, X).
#
# The game continues until all the stones have been taken.
# Assuming Alex and Lee play optimally, return the maximum number of stones Alex can get.

# Input: piles = [2,7,9,4,4]
# Output: 10
# Explanation:  If Alex takes one pile at the beginning, Lee takes two piles, then Alex takes 2 piles
# again. Alex can get 2 + 4 + 4 = 10 piles in total. If Alex takes two piles at the beginning,
# then Lee can take all three piles left. In this case, Alex get 2 + 7 = 9 piles in total.
# So we return 10 since it's larger.

# dp[i, m] = maximum stones the current player can get from piles[i:] with M=m
# A[i]= total stones of piles[i:]
# when current player pick stones from i to i+x-1
# -> the other player's stones: dp[i+x, max(m, x)]
# -> total stones of current player: A[i] - dp[i+x, max(m, x)]
# we want the current player gets maximum means the other player gets minimum

class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        from functools import lru_cache
        @lru_cache(None)
        def dp(i, m):
            if i + 2 * m >= N: return piles[i]
            return piles[i] - min(dp(i + x, max(m, x)) for x in range(1, 2 * m + 1))

        N = len(piles)
        for i in range(N - 2, -1, -1):
            piles[i] += piles[i + 1]
        return dp(0, 1)

    def stoneGameII_useLookup(self, piles):
        def dp(i, m):
            if (i, m) not in lookup:
                if i + 2 * m >= len(piles):
                    lookup[i, m] = piles[i]
                else:
                    lookup[i, m] = piles[i] - \
                                   min(dp(i+x, max(m, x))
                                       for x in range(1, 2*m+1))
            return lookup[i, m]

        for i in reversed(range(len(piles)-1)):
            piles[i] += piles[i+1]
        lookup = {}
        return dp(0, 1)

print(Solution().stoneGameII([2,7,9,4,4])) # 10
# Alex: (0, 1)->26-16=10
# Lee: (1, 1)->24-8=16; (2, 2)->17
# Alex: (2, 1)->17-4=13, (3,2)->8;
# Lee: (3, 1)->8, (4,2)->4;