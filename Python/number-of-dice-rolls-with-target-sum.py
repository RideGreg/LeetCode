# Time:  O(d * f * t)
# Space: O(t)

# 1155 weekly contest 149 8/10/2019
# You have d dice, and each die has f faces numbered 1, 2, ..., f.
#
# Return the number of possible ways (out of f^d total ways) modulo 10^9 + 7 to roll the dice
# so the sum of the face up numbers equals target.

# 1 <= d, f <= 30
# 1 <= target <= 1000

import collections

class Solution(object):
    def numRollsToTarget(self, d: int, f: int, target: int) -> int: # USE THIS
        M, dp = 10**9+7, {0:1}
        for _ in range(d):
            ndp = collections.defaultdict(int)
            for k, ways in dp.items(): # k: 前面几个dice的点数和
                for i in range(1, f+1): #当前dice的点数
                    if k+i <= target:
                        ndp[k+i] = (ndp[k+i] + ways) % M
            dp = ndp
        return dp[target]

    def numRollsToTarget_kamyu(self, d, f, target):
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        """
        MOD = 10**9+7
        dp = [[0 for _ in range(target+1)] for _ in range(2)]
        dp[0][0] = 1
        for i in range(1, d+1):
            dp[i%2] = [0 for _ in range(target+1)]
            for k in range(1, f+1):
                for j in range(k, target+1):
                    dp[i%2][j] = (dp[i%2][j] + dp[(i-1)%2][j-k]) % MOD
        return dp[d%2][target] % MOD

print(Solution().numRollsToTarget(1, 6, 3)) # 1
print(Solution().numRollsToTarget(2, 6, 7)) # 6
print(Solution().numRollsToTarget(2, 5, 10)) # 1
print(Solution().numRollsToTarget(1, 2, 3)) # 0
print(Solution().numRollsToTarget(30, 30, 500)) # 222616187