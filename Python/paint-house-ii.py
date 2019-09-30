# Time:  O(n * k)
# Space: O(k)

# 265
# There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with
# a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

# The cost of painting each house with a certain color is represented by a n x k cost matrix. For example,
# costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2,
# and so on... Find the minimum cost to paint all houses.

# TLE if using the same way in 256 paint-house which is O(nk^2).

import functools

class Solution2(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        return min(functools.reduce(self.combine, costs)) if costs else 0

    def combine(self, tmp, house):
        smallest, k, i = min(tmp), len(tmp), tmp.index(min(tmp))
        tmp, tmp[i] = [smallest] * k, min(tmp[:i] + tmp[i+1:])
        return map(sum, zip(tmp, house))


class Solution(object): # USE THIS
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0
        m, n = len(costs), len(costs[0])
        dp = [0] * n
        for i in range(m):
            min1, min2, idmin1 = float('inf'), float('inf'), None
            for j in range(n):
                if dp[j] < min1:
                    min1, min2, idmin1 = dp[j], min1, j
                elif dp[j] < min2:
                    min2 = dp[j]
            for j in range(n):
                dp[j] = costs[i][j] + (min1 if j != idmin1 else min2)
        return min(dp)

print(Solution().minCostII([[1,1,1,2],[3,10,11,12]])) # 4 = 1 + 3
