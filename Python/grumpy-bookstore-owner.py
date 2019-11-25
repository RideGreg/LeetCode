# Time:  O(n)
# Space: O(1)

# 1052 weekly contest 138 5/25/2019
#
# Today, the bookstore owner has a store open for customers.length minutes.  Every minute, some number of
# customers (customers[i]) enter the store, and all those customers leave after the end of that minute.
#
# On some minutes, the bookstore owner is grumpy.  If the bookstore owner is grumpy on the i-th minute,
# grumpy[i] = 1, otherwise grumpy[i] = 0.  When the bookstore owner is grumpy, the customers of that minute
# are not satisfied, otherwise they are satisfied.
#
# The bookstore owner knows a secret technique to keep themselves not grumpy for X minutes straight,
# but can only use it once.
#
# Return the maximum number of customers that can be satisfied throughout the day.

# 1 <= X <= customers.length == grumpy.length <= 20000
# 0 <= customers[i] <= 1000
# 0 <= grumpy[i] <= 1

class Solution(object):
    def maxSatisfied(self, customers, grumpy, X):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        """
        ans, max_extra, extra = 0, 0, 0
        for i, c in enumerate(customers):
            if grumpy[i]:
                extra += c
            else:
                ans += c

            if i >= X and grumpy[i-X]:
                extra -= customers[i-X]
            max_extra = max(max_extra, extra)
        return ans + max_extra

    # Space O(n) use extra space not good
    def maxSatisfied_ming(self, customers, grumpy, X):
        prefix, N = [0], len(grumpy)
        for i in range(N):
            if grumpy[i] == 1:
                prefix.append(prefix[-1]+customers[i])
            else:
                prefix.append(prefix[-1])
        mn = float('inf')
        for start in range(1, N-X+1):
            mn = min(mn, prefix[-1]-prefix[start-1+X]+prefix[start-1])
        return sum(customers)-mn

print(Solution().maxSatisfied([1,0,1,2,1,1,7,5], [0,1,0,1,0,1,0,1], 3)) # 16
