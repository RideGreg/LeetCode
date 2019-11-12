# Time:  O(n)
# Space: O(1)

# 714
# Your are given an array of integers prices,
# for which the i-th element is the price of a given stock on day i;
# and a non-negative integer fee representing a transaction fee.
#
# You may complete as many transactions as you like,
# but you need to pay the transaction fee for each transaction.
# You may not buy more than 1 share of a stock at a time
# (ie. you must sell the stock share before you buy again.)
#
# Return the maximum profit you can make.
#
# Example 1:
# Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
# Output: 8
# Explanation: The maximum profit can be achieved by:
# Buying at prices[0] = 1
# Selling at prices[3] = 8
# Buying at prices[4] = 4
# Selling at prices[5] = 9
# The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
#
# Note:
# - 0 < prices.length <= 50000.
# - 0 < prices[i] < 50000.
# - 0 <= fee < 50000.

# optimal substructure and overlapping sub-problem
try:
    xrange          # Python 2
except NameError:
    xrange = range  # Python 3

# optimal substructure and overlapping sub-problem

class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        cash, hold = 0, -prices[0]
        for p in prices[1:]:
            cash, hold = max(cash, hold + p - fee), max(hold, cash-p)
            ''' 先算cash再算hold，updated cash其实不影响hold（先算hold也不影响）。但最好像上面同时计算
            cash = max(cash, hold+p-fee)
            hold = max(hold, cash-p)
            '''
        return cash

    # 栈中保存交易序列[buy, sell]，当sell为0时表示还没有卖出
    # 遍历prices，记当前价格为price：
    # 若栈顶交易sell为0，并且price <= buy，则将栈顶buy替换为price
    # 否则，若price >= max(栈顶sell，栈顶buy + fee)，则替换栈顶sell为price
    # 否则，若堆栈顶已有完整交易(sell不为0)，将[price, 0]压栈
    # 当栈元素>1，并且合并栈顶的两组交易可以获得更大收益时，对栈顶的两个交易进行合并

    def maxProfit_bookshadow(self, prices, fee):
        ts = [[50000, 0]]
        for price in prices:
            if not ts[-1][1] and price <= ts[-1][0]:
                ts[-1][0] = price
            elif price >= max(ts[-1][1], ts[-1][0] + fee):
                ts[-1][1] = price
            elif ts[-1][1]:
                ts.append([price, 0])
            while len(ts) > 1 and ts[-2][1] < ts[-1][0] + fee:
                ts[-1][1] = max(ts.pop()[1], ts[-1][1])
        return sum(t[1] - t[0] - fee for t in ts if t[1] - t[0] > fee)

print(Solution().maxProfit([1,3,2,8,4,9], 2))
