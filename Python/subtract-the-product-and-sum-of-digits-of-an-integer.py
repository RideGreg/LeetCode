# Time:  O(logn)
# Space: O(1)

# 1281 weekly contest 166 12/7/2019

# Given an integer number n, return the difference between the product of its digits and the sum of its digits.

class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        product, total = 1, 0
        while n:
            n, r = divmod(n, 10)
            product *= r
            total += r
        return product-total


# Time:  O(logn)
# Space: O(logn)
import operator


class Solution2(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        import functools
        A = map(int, str(n))
        return functools.reduce(operator.mul, A) - sum(A)

print(Solution().subtractProductAndSum(234)) # 15
print(Solution().subtractProductAndSum(4421)) # 21
