# Time:  O(n)
# Space: O(1)

# 121
# Say you have an array for which the ith element
# is the price of a given stock on day i.
#
# If you were only permitted to complete at most one transaction
# (ie, buy one and sell one share of the stock),
# design an algorithm to find the maximum profit.
#


class Solution(object):
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        ans, mmin = 0, float('inf')
        for p in prices:
            mmin = min(mmin, p)
            ans = max(ans, p-mmin)
        return ans
