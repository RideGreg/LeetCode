# Time:  O(n * p * g)
# Space: O(p * g)

# There are G people in a gang, and a list of various crimes they could commit.
#
# The i-th crime generates a profit[i] and requires group[i] gang members to participate.
#
# If a gang member participates in one crime,
# that member can't participate in another crime.
#
# Let's call a profitable scheme any subset of these crimes that
# generates at least P profit,
# and the total number of gang members participating in that subset of crimes is at most G.
#
# How many schemes can be chosen?  Since the answer may be very large, return it modulo 10^9 + 7.
#
# Example 1:
#
# Input: G = 5, P = 3, group = [2,2], profit = [2,3]
# Output: 2
# Explanation: 
# To make a profit of at least 3, the gang could either commit crimes 0 and 1, or just crime 1.
# In total, there are 2 schemes.
# Example 2:
#
# Input: G = 10, P = 5, group = [2,3,5], profit = [6,7,8]
# Output: 7
# Explanation: 
# To make a profit of at least 5, the gang could commit any crimes, as long as they commit one.
# There are 7 possible schemes: (0), (1), (2), (0,1), (0,2), (1,2), and (0,1,2).
#
# Note:
# - 1 <= G <= 100
# - 0 <= P <= 100
# - 1 <= group[i] <= 100
# - 0 <= profit[i] <= 100
# - 1 <= group.length = profit.length <= 100

# Solution: Dynamic Programming
# We don't care if the profit of the schemes > P and the number of people required > G, so the bounds are small enough to use DP.
# Keep track of cur[p][g] (the # of schemes with profitability p and requiring g gang members, except the last row when p==P,
# it is all schemes profit at least P instead of exactly P). For each new scheme (p, g), we update the DP table.

import itertools


class Solution(object):
    def profitableSchemes(self, G, P, group, profit):
        """
        :type G: int
        :type P: int
        :type group: List[int]
        :type profit: List[int]
        :rtype: int
        """
        dp = [[0]*(G+1) for _ in xrange(P+1)]
        dp[0][0] = 1
        for p, g in itertools.izip(profit, group):
            for i in xrange(P, -1, -1):
                for j in xrange(G-g, -1, -1):
                    i2, j2 = min(i+p, P), j+g
                    dp[i2][j2] += dp[i][j]
        return sum(dp[P]) % (10**9 + 7)

    def profitableSchemes(self, G, P, group, profit): # same as the above, traverse forward
        dp = [[0] * (G + 1) for _ in xrange(P + 1)]
        dp[0][0] = 1

        for p, g in zip(profit, group):
            # p, g : the current crime profit and group size
            dp2 = [row[:] for row in dp]
            for i in xrange(P + 1):
                # i : the current profit
                # p2 : the new profit after committing this crime
                p2 = min(i + p, P)
                for j in xrange(G - g + 1):
                    # j : the current group size
                    # g2 : the new group size after committing this crime
                    g2 = j + g
                    dp2[p2][g2] += dp2[i][j]
                    dp2[p2][g2] %= (10**9 + 7)
            dp = dp2

        # Sum all schemes with profit P and group size 0 <= g <= G.
        return sum(dp[-1]) % (10**9 + 7)

print(Solution().profitableSchemes(5,3,[2,2],[2,3]))