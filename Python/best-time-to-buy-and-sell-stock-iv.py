# Time:  O(k * n)
# Space: O(k)
#
# Say you have an array for which the ith element is
# the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit.
# You may complete at most k transactions.
#
# Note:
# You may not engage in multiple transactions at the same time
# (ie, you must sell the stock before you buy again).
#

try:
    xrange          # Python 2
except NameError:
    xrange = range  # Python 3


class Solution(object):
    # @return an integer as the maximum profit
    def maxProfit(self, k, prices): # USE THIS: refer to at most 2 transactions problem (best-time-to-buy-and-sell-iii.py)
        if k == 0 or len(prices) == 0: return 0

        # corner case: huge k will cause memory error in allocating cost array
        # this case is as many transactions as you like problem (best-time-to-buy-and-sell-ii.py)
        n = len(prices)
        if k >= n // 2:
            return sum(max(0, prices[i] - prices[i - 1]) for i in range(1, n))

        bal_buy = [float('-inf')] * k
        bal_sell = [0] * k
        for i in range(n):
            # optimization skip unnecessary large k. Need to be i+1, so when i is 0, still set bal_buy[0].
            # kamyu solution uses min(k, i//2+1) + 1, but I think for day i, we can do i transactions.
            for j in range(min(k, i+1)):
                bal_after_last_sell = bal_sell[j-1] if j > 0 else 0
                bal_buy[j] = max(bal_buy[j], bal_after_last_sell - prices[i]) # maximize max_buy means price at buy point needs to be as small as possible
                bal_sell[j] = max(bal_sell[j], bal_buy[j] + prices[i])
        return bal_sell[k-1]

