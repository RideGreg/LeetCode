# Time:  O(n)
# Space: O(1)
#
# Say you have an array for which the ith element
# is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit.
# You may complete at most two transactions.
#
# Note:
# You may not engage in multiple transactions at the same time
# (ie, you must sell the stock before you buy again).
#

# Input: [3,3,5,0,0,3,1,4]
# Output: 6 (= 3-0 + 4-1)

# Input: [1,2,3,4,5]
# Output: 4

try:
    xrange          # Python 2
except NameError:
    xrange = range  # Python 3


class Solution(object):  # USE THIS: CAN EXTEND to k transactions.
    # @param prices, a list of integer
    # @return an integer

    # This solution is AN EXTENSION OF SOLUTION for buy-and-sell-stock-i.
    # Maintain the min of if we just buy 1, 2, 3... stock, and the max of if we just sell 1,2,3... stock.
    # In order to get the final max profit, profit1 must be as relatively most as possible to produce a small cost2,
    # and therefore cost2 can be as less as possible to give the final max profit2.
    def maxProfit(self, prices):
        cost1, cost2 = float("inf"), float("inf")
        profit1, profit2 = 0, 0
        for i in prices:
            cost1 = min(cost1, i)
            profit1 = max(profit1, i - cost1)
            cost2 = min(cost2, i - profit1)
            profit2 = max(profit2, i - cost2)
        return profit2


# Time:  O(k * n)
# Space: O(k)
class Solution2(object):
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        return self.maxAtMostKPairsProfit(prices, 2)

    def maxAtMostKPairsProfit(self, prices, k):
        max_buy = [float("-inf") for _ in xrange(k + 1)]
        max_sell = [0 for _ in xrange(k + 1)]

        for i in xrange(len(prices)):
            for j in xrange(1, min(k, i/2+1) + 1):
                max_buy[j] = max(max_buy[j], max_sell[j-1] - prices[i])
                max_sell[j] = max(max_sell[j], max_buy[j] + prices[i])

        return max_sell[k]


# This solution cannot extend to k transactions.
# Time:  O(n)
# Space: O(n)
class Solution3(object):
    # @param prices, a list of integer
    # @return an integer

    # use any day as divider for 1st and 2nd stock transaction. Compare all possible division
    # (linear time). Ok to sell then buy at the same day, so divider is on each day (dp array
    # is length N), not between two days.
    def maxProfit(self, prices):
        N = len(prices)
        min_price, max_profit_from_left, max_profits_from_left = \
            float("inf"), 0, [0]*N
        max_price, max_profit_from_right, max_profits_from_right = 0, 0, [0]*N

        for i in range(N):
            min_price = min(min_price, prices[i])
            max_profit_from_left = max(max_profit_from_left, prices[i] - min_price)
            max_profits_from_left[i] = max_profit_from_left

            max_price = max(max_price, prices[N-1-i])
            max_profit_from_right = max(max_profit_from_right,
                                        max_price - prices[N-1-i])
            max_profits_from_right[N-1-i] = max_profit_from_right

        return max(max_profits_from_left[i]+max_profits_from_right[i]
                   for i in range(N)) if N else 0

print(Solution().maxProfit([1,2,3,4,5])) # 4
print(Solution().maxProfit([3,3,5,0,0,3,1,4])) # 6