# Time:  O(n)
# Space: O(1)
#
# 123
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

    # This solution is AN EXTENSION OF SOLUTION for buy-and-sell-stock-i, and can extend to k.
    # bal_buy[i] is the balance after ith buy, bal_sell[i] is the balance after ith sell.
    def maxProfit(self, prices):
        n, k = len(prices), 2
        bal_buy = [float('-inf')] * (k+1)
        bal_sell = [0] * (k+1)
        for i in range(n):
            # optimization skip unnecessary large k. Need to be i+1, so when i is 0, still set bal_buy[0].
            # kamyu solution uses min(k, i//2+1) + 1, but I think for day i, we can do i transactions.
            for j in range(1, min(k, i+1)+1):
                bal_buy[j] = max(bal_buy[j], bal_sell[j-1] - prices[i]) # maximize max_buy means price at buy point needs to be as small as possible
                bal_sell[j] = max(bal_sell[j], bal_buy[j] + prices[i])
        return bal_sell[k]


# Time:  O(n)
# Space: O(1)
class Solution2(object):
    # similar to Solution 1, but track cost/profit instead of balances.

    # Maintain the min COST of if we just buy 1, 2, 3... stock, and the max PROFIT (balance) of if we just sell 1,2,3... stock.
    # In order to get the final max profit, profit1 must be as relatively large as possible to produce a small cost2,
    # and therefore cost2 can be as small as possible to give the final max profit2.
    def maxProfit(self, prices):
        cost1, cost2 = float("inf"), float("inf")
        profit1, profit2 = 0, 0
        for p in prices:
            cost1 = min(cost1, p)             # lowest price
            profit1 = max(profit1, p - cost1) # global max profit for 1 buy-sell transaction
            cost2 = min(cost2, p - profit1)   # adjust the cost by reducing 1st profit
            profit2 = max(profit2, p - cost2) # global max profit for 1 to 2 transactions
        return profit2


# This solution CANNOT extend to k transactions.
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
        _min, maxProfitLeft, maxProfitsLeft = float("inf"), 0, [0]*N
        _max, maxProfitRight, maxProfitsRight = 0, 0, [0]*N

        for i in range(N):
            _min = min(_min, prices[i])
            maxProfitLeft = max(maxProfitLeft, prices[i] - _min)
            maxProfitsLeft[i] = maxProfitLeft

            _max = max(_max, prices[N-1-i])
            maxProfitRight = max(maxProfitRight, _max - prices[N-1-i])
            maxProfitsRight[N-1-i] = maxProfitRight

        return max(maxProfitsLeft[i]+maxProfitsRight[i]
                   for i in range(N)) if N else 0

print(Solution().maxProfit([1,2,3,4,5])) # 4
print(Solution().maxProfit([3,3,5,0,0,3,1,4])) # 6