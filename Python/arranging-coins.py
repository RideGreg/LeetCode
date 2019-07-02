# -*- encoding=utf-8 -*-
# Time:  O(logn)
# Space: O(1)

# You have a total of n coins that you want to form in a staircase shape,
# where every k-th row must have exactly k coins.
#
# Given n, find the total number of full staircase rows that can be
# formed.
#
# n is a non-negative integer and fits within the range of a 32-bit
# signed integer.
#
# Example 1:
#
# n = 5
#
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤
#
# Because the 3rd row is incomplete, we return 2.
# Example 2:
#
# n = 8
#
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤ ¤
# ¤ ¤
#
# Because the 4th row is incomplete, we return 3.

import math


class Solution(object):
    # 一元二次方程ax^2 + bx + c = 0 求根公式 x1 = -b-sqrt(b^2-4ac)/2a, x2 = -b+sqrt(b^2-4ac)/2a
    # x(x+1)//2 <= n => x^2+x-2n <= 0 因为判别式b^2-4ac = 8n+1 > 0 所以有两实数解，所以不等式的解集为 
    # (-sqrt(8n + 1) -1)/2 <= x <= (sqrt(8n + 1) -1)/2
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int((math.sqrt(8*n+1)-1) / 2)  # sqrt is O(logn) time.


# Time:  O(logn)
# Space: O(1)
class Solution2(object):
    def arrangeCoins_ming(self, n):
        def check(k):
            return k*(k+1)//2 <= n
        
        l, r = 0, n              # range [l, r] contains at least one valid solution 0
        while l < r:
            m = l + (r-l+1)//2   # m is close to r not l, since we have l = m below. 
            if check(m):
                l = m
            else:
                r = m - 1
        return l                 # reutrn r is also okay, since l equals to r.

    def arrangeCoins_kamyu(self, n):
        """
        :type n: int
        :rtype: int
        """
        def check(mid, n):
            return mid*(mid+1) <= 2*n

        left, right = 1, n
        while left <= right:
            mid = left + (right-left)//2
            if not check(mid, n):
                right = mid-1
            else:
                # becuase left maybe = mid, in the case of check ok, cannot set left=mid which is dead loop never converge.
                # so left-1 is actually a valid answer, so when left>right exit, the answer is left-1 or right.
                left = mid+1
        return left-1   # return right is also okay
