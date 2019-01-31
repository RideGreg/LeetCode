# Time:  O((logn)^2), n is the bound. log(n, x) = log(n)/log(x), where log(x) < and be bound by log(n)
# Space: O(r), r is the size of the result

# 970
# Given two non-negative integers x and y, an integer is powerful if it is equal to x^i + y^j for some integers i >= 0 and j >= 0.
#
# Return a list of all powerful integers that have value less than or equal to bound.
# You may return the answer in any order.  In your answer, each value should occur at most once.

# Note:
# 1 <= x <= 100
# 1 <= y <= 100
# 0 <= bound <= 10^6

import math


class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        # Continually multiply to avoid pitfalls when calling math.log():
        # log(0, 10) ValueError: math domain error
        # log(100, 1) ZeroDivisionError: float division by zero

        if x == 1 and y == 1: return [2] if bound>1 else []

        ans = set()
        if x == 1 or y == 1:
            x, y = 1, max(x, y)
            py = 1
            while 1+py <= bound:
                ans.add(1+py)
                py *= y
            return list(ans)
        else:
            px = 1
            while px < bound:
                py = 1
                while px+py <= bound:
                    ans.add(px+py)
                    py *= y
                px *= x
            return list(ans)

    def powerfulIntegers_kamyu(self, x, y, bound):
        if bound < 2: return []

        result = set()
        log_x = int(math.log(bound,x))+1 if x != 1 else 1
        log_y = int(math.log(bound,y))+1 if y != 1 else 1
        pow_x = 1
        for i in xrange(log_x):
            pow_y = 1
            for j in xrange(log_y):
                val = pow_x + pow_y
                if val <= bound:
                    result.add(val)
                pow_y *= y
            pow_x *= x
        return list(result)

print(Solution().powerfulIntegers(2,3,0)) # []
print(Solution().powerfulIntegers(1,2,100)) # [2,3,5,9,17,33,65]
print(Solution().powerfulIntegers(3,5,15)) # [2,4,6,8,10,14]
