# Time:  O(logn), pow is O(logn).
# Space: O(1)

# 343
# Given a positive integer n, break it into the sum of
# at least two positive integers and maximize the product
# of those integers. Return the maximum product you can get.
#
# For example, given n = 2, return 1 (2 = 1 + 1); given n = 10,
# return 36 (10 = 3 + 3 + 4).
#
# Note: you may assume that n is not less than 2.
#
# Hint:
#
# There is a simple O(n) solution to this problem.
# You may check the breaking results of n ranging from 7 to 10
# to discover the regularities.

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 4:
            return n - 1

        #  Proof.
        #  1. Let n = a1 + a2 + ... + ak, product = a1 * a2 * ... * ak
        #      - For each ai >= 4, we can always maximize the product by:
        #        ai <= 2 * (ai - 2)
        #      - For each aj >= 5, we can always maximize the product by:
        #        aj <= 3 * (aj - 3)
        #
        #     Conclusion 1:
        #      - For n >= 4, the max of the product must be in the form of
        #        3^a * 2^b, s.t. 3a + 2b = n
        #
        #  2. To maximize the product = 3^a * 2^b s.t. 3a + 2b = n
        #      - For each b >= 3, we can always maximize the product by:
        #        3^a * 2^b <= 3^(a+2) * 2^(b-3) s.t. 3(a+2) + 2(b-3) = n
        #
        #     Conclusion 2:
        #      - For n >= 4, the max of the product must be in the form of
        #        3^Q * 2^R, 0 <= R < 3 s.t. 3Q + 2R = n
        #        i.e.
        #          if n = 3Q + 0,   the max of the product = 3^Q * 2^0
        #          if n = 3Q + 2,   the max of the product = 3^Q * 2^1
        #          if n = 3Q + 2*2, the max of the product = 3^Q * 2^2

        res = 0
        if n % 3 == 0:            #  n = 3Q + 0, the max is 3^Q * 2^0
            res = 3 ** (n // 3)
        elif n % 3 == 2:          #  n = 3Q + 2, the max is 3^Q * 2^1
            res = 3 ** (n // 3) * 2
        else:                     #  n = 3Q + 4, the max is 3^Q * 2^2
            res = 3 ** (n // 3 - 1) * 4
        return res



# Time:  O(n)
# Space: O(1)
# DP solution.
from functools import lru_cache
class Solution2(object):
    # integerBreak(n) = max(integerBreak(n - 2) * 2, integerBreak(n - 3) * 3)
    # Proof: assume break n into 7 + ..., see solution 1 we know we SHOULD further break 7 into 2 + ...
    # or 3 + ... for max. So the final is always like 2 + ... or 3 + ...
    def integerBreak(self, n):  # USE THIS: cache version
        """
        :type n: int
        :rtype: int
        """
        @lru_cache(None)
        def dp(m):
            if m < 4: return m-1
            # both "no more break" and "break further"
            return max(x * max(m-x, dp(m-x)) for x in (2, 3))

        return dp(n)

    def integerBreak(self, n: int) -> int:
        if n < 4: return n - 1

        res = [0, 1, 2, 3] # this is not answer for n = 1,2,3. This is actually max(x, res[x])
        for i in range(4, n + 1):
            res[i % 4] = max(res[(i - 2) % 4] * 2, res[(i - 3) % 4] * 3)
        return res[n % 4]


    # normal DP: Time O(n^2) Space O(n)
    # don't consider break into (1, n-1) which is wasted 1*...
    # DP is max(x * max(m-x, dp[m-x])) where m-x is no more break, dp[m-x] is break further.
    def integerBreak2(self, n: int) -> int:
        dp = [0,0,1,2]
        for m in range(4, n+1):
            dp.append(max(x * max(m-x, dp[m-x]) for x in range(2, m-1)))
        return dp[n]

    # cache version
    def integerBreak3(self, n: int) -> int:
        @lru_cache(None)
        def dp(m):
            if m < 4: return m-1
            return max(x * max(m-x, dp(m-x)) for x in range(2, m-1))

        return dp(n)

print(Solution2().integerBreak(10)) # 36