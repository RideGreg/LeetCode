# Time:  O(n)
# Space: O(1)

# 746
# On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).
#
# Once you pay the cost, you can either climb one or two steps.
# You need to find minimum cost to reach the top of the floor,
# and you can either start from the step with index 0, or the step with index 1.
#
# Example 1:
# Input: cost = [10, 15, 20]
# Output: 15
# Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
# Example 2:
# Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# Output: 6
# Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
# Note:
#  - cost will have a length in the range [2, 1000].
#  - Every cost[i] will be an integer in the range [0, 999].


# DP: dp[x] = min(dp[x - 1], dp[x - 2]) + cost[x]

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        prev, cur = cost[0], cost[1]
        for i in range(2, len(cost)):
            prev, cur = cur, cost[i] + min(prev, cur)
        return min(prev, cur)

        ''' space not optimized
        size = len(cost)
        dp = [cost[0], cost[1]]
        for x in range(2, size):
            dp.append(min(dp[x - 1], dp[x - 2]) + cost[x])
        return min(dp[-1], dp[-2])
        '''

    def minCostClimbingStairs_ming(self, cost):
        N = len(cost)
        dp = [None] * N

        def re(n):
            if dp[n] == None:
                if n == 0 or n == 1:
                    return cost[n]

                dp[n] = cost[n] + min(re(n - 1), re(n - 2))

            return dp[n]

        return min(re(N-1), re(N-2))


print(Solution().minCostClimbingStairs([0,1,2,0])) # 1
print(Solution().minCostClimbingStairs([0,0,0,1])) # 0
