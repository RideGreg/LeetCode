class Solution(object):
    def minCostClimbingStairs(self, cost):
        dp = [0]*(len(cost)+1)
        for i in xrange(2,len(cost)+1):
            dp[i] = min(dp[i-2]+cost[i-2], dp[i-1]+cost[i-1])
        return dp[-1]
print Solution().minCostClimbingStairs([10, 15, 20])
print Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
