# Time:  O(n * k), n is the number of coins, k is the amount of money
# Space: O(k)

# 322
# You are given coins of different denominations and
# a total amount of money amount. Write a function to
# compute the fewest number of coins that you need to
# make up that amount. If that amount of money cannot
# be made up by any combination of the coins, return -1.
#
# Example 1:
# coins = [1, 2, 5], amount = 11
# return 3 (11 = 5 + 5 + 1)
#
# Example 2:
# coins = [2], amount = 3
# return -1.
#
# Note:
# You may assume that you have an infinite number of each kind of coin.

# DP solution. (1680ms)
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for c in coins:
            for x in range(c, amount + 1):
                dp[x] = min(dp[x], 1 + dp[x-c])
        return dp[-1] if dp[-1] != float('inf') else -1


    def coinChange_kamyu(self, coins, amount):
        INF = 0x7fffffff  # Using float("inf") would be slower.
        dp = [INF] * (amount + 1)
        dp[0] = 0
        for i in xrange(amount + 1):
            if dp[i] != INF:
                for coin in coins:
                    if i + coin <= amount:
                        dp[i + coin] = min(dp[i + coin], dp[i] + 1)
        return dp[amount] if dp[amount] != INF else -1

print(Solution().coinChange([1], 0)) # 0

