# Time:  O(n)
# Space: O(1)

# 309
# Say you have an array for which the ith element is the price of
# a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete as
# many transactions as you like (ie, buy one and sell one share of the
# stock multiple times) with the following restrictions:
#
# You may not engage in multiple transactions at the same time
# (ie, you must sell the stock before you buy again).
# After you sell your stock, you cannot buy stock on next day.
# (ie, cooldown 1 day)

try:
    xrange          # Python 2
except NameError:
    xrange = range  # Python 3

# three states buy/sell/coolDown can be simplified as 2 states own/notOwn

class Solution(object):
    # only relay on the balance of past two days
    # holdpre, hold: balance if own stock in previous day and current day
    # cashpre, cash: balance if not own stock in previous day and current day
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0

        holdpre = -prices[0]
        hold = max(-prices[0], -prices[1])
        cashpre = 0
        cash = max(0, prices[1]-prices[0])

        for p in prices[2:]:
            holdpre, cashpre, hold, cash = hold, cash, max(hold, cashpre-p), max(cash, hold+p)
        return max(cash, hold)

    # or more clear with a rotating array
    # notOwn[i]表示在第i天不持有股票所能获得的最大累计收益
    # own[i]表示在第i天持有股票所能获得的最大累计收益
    # also do space optimization
    def maxProfit_rotatingArray(self, prices):
        N = len(prices)
        if N < 2:
            return 0

        own = [-prices[0], max(-prices[0], -prices[1]), 0]
        notOwn = [0, max(0, prices[1]-prices[0]), 0]
        for i in range(2, N):
            notOwn[i%3] = max(notOwn[(i-1)%3], own[(i-1)%3] + prices[i])
            own[i%3] = max(own[(i-1)%3], notOwn[(i-2)%3] - prices[i])
        return notOwn[(N-1)%3]


    # 3 states
    def maxProfit_kamyu(self, prices):
        if not prices:
            return 0
        buy, sell, coolDown = [0] * 2, [0] * 2, [0] * 2
        buy[0] = -prices[0]
        for i in xrange(1, len(prices)):
            # Bought before or buy today.
            buy[i % 2] = max(buy[(i - 1) % 2],
                             coolDown[(i - 1) % 2] - prices[i])
            # Sell today.
            sell[i % 2] = buy[(i - 1) % 2] + prices[i]
            # Sold before yesterday or sold yesterday.
            coolDown[i % 2] = max(coolDown[(i - 1) % 2], sell[(i - 1) % 2])
        return max(coolDown[(len(prices) - 1) % 2],
                   sell[(len(prices) - 1) % 2])


print(Solution().maxProfit([1, 2, 3, 0, 2])) # 3 = [buy, sell, cooldown, buy, sell]
