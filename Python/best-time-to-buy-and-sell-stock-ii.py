# Time:  O(n)
# Space: O(1)

# 122
# Say you have an array for which the ith element is
# the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit.
# You may complete as many transactions as you like
# (ie, buy one and sell one share of the stock multiple times).
# However, you may not engage in multiple transactions at the same time
# (ie, you must sell the stock before you buy again).

try:
    xrange          # Python 2
except NameError:
    xrange = range  # Python 3


class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        profit = 0
        for i in xrange(len(prices) - 1):
            profit += max(0, prices[i + 1] - prices[i])
        return profit

    def maxProfit2(self, prices):
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))

    # two pointers: Instinct is to find each peak and valley before making a calculation
    def maxProfit3(self, prices):
        ans, i = 0, 0
        while i < len(prices):
            j = i + 1
            while j < len(prices) and prices[j] >= prices[j-1]:
                j += 1
            ans += prices[j-1] - prices[i]
            i = j
        return ans
