# Time:  O(n)
# Space: O(n)

# 188
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

from random import randint


class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        def nth_element(nums, n, compare=lambda a, b: a < b):
            def tri_partition(nums, left, right, target, compare):
                mid = left
                while mid <= right:
                    if nums[mid] == target:
                        mid += 1
                    elif compare(nums[mid], target):
                        nums[left], nums[mid] = nums[mid], nums[left]
                        left += 1
                        mid += 1
                    else:
                        nums[mid], nums[right] = nums[right], nums[mid]
                        right -= 1
                return left, right

            left, right = 0, len(nums)-1
            while left <= right:
                pivot_idx = randint(left, right)
                pivot_left, pivot_right = tri_partition(nums, left, right, nums[pivot_idx], compare)
                if pivot_left <= n <= pivot_right:
                    return
                elif pivot_left > n:
                    right = pivot_left-1
                else:  # pivot_right < n.
                    left = pivot_right+1

        profits = []
        v_p_stk = []  # mono stack, where v is increasing and p is strictly decreasing
        v, p = -1, -1
        while p+1 < len(prices): # at most O(n) peaks, so v_p_stk and profits are both at most O(n) space
            for v in xrange(p+1, len(prices)-1):
                if prices[v] < prices[v+1]:
                    break
            else:
                v = len(prices)-1
            for p in xrange(v, len(prices)-1):
                if prices[p] > prices[p+1]:
                    break 
            else:
                p = len(prices)-1
            while v_p_stk and prices[v_p_stk[-1][0]] > prices[v]:  # not overlapped
                last_v, last_p = v_p_stk.pop()
                profits.append(prices[last_p]-prices[last_v])  # count [prices[last_v], prices[last_p]] interval
            while v_p_stk and prices[v_p_stk[-1][1]] <= prices[p]:  # overlapped
                # prices[last_v] <= prices[v] <= prices[last_p] <= prices[p],
                # treat overlapped as [prices[v], prices[last_p]], [prices[last_v], prices[p]] intervals due to invariant max profit
                last_v, last_p = v_p_stk.pop()
                profits.append(prices[last_p]-prices[v])  # count [prices[v], prices[last_p]] interval
                v = last_v
            v_p_stk.append((v, p))  # keep [prices[last_v], prices[p]] interval to check overlapped      
        while v_p_stk:
            last_v, last_p = v_p_stk.pop()
            profits.append(prices[last_p]-prices[last_v])  # count [prices[last_v], prices[last_p]] interval
        if k > len(profits):
            k = len(profits)
        else:
            nth_element(profits, k-1, compare=lambda a, b: a > b)
        return sum(profits[i] for i in xrange(k))  # top k profits of nonoverlapped intervals


# Time:  O(k * n)
# Space: O(k)
class Solution2(object):
    def maxProfit(self, k, prices): # USE THIS: refer to at most 2 transactions problem (best-time-to-buy-and-sell-iii.py)
        if k == 0 or len(prices) == 0: return 0

        # corner case: huge k will cause memory error in allocating cost array
        # this case is as many transactions as you like problem (best-time-to-buy-and-sell-ii.py)
        n = len(prices)
        if k >= n // 2:
            return sum(max(0, prices[i] - prices[i - 1]) for i in range(1, n))

        bal_buy = [float('-inf')] * (k+1)
        bal_sell = [0] * (k+1)
        for i in range(n):
            # optimization skip unnecessary large k. Need to be i+1, so when i is 0, still set bal_buy[0].
            # kamyu solution uses min(k, i//2+1) + 1, but I think for day i, we can do i transactions.
            for j in range(1, k+1):
                bal_buy[j] = max(bal_buy[j], bal_sell[j-1] - prices[i]) # maximize max_buy means price at buy point needs to be as small as possible
                bal_sell[j] = max(bal_sell[j], bal_buy[j] + prices[i])
        return bal_sell[-1]
