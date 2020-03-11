# Time:  O(n)
# Space: O(1)

# 1304 weekly contest 169 12/28/2019

# Given an integer n, return any array containing n unique integers such that they add up to 0.

class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        return [i for i in xrange(-(n//2), n//2+1) if not (i == 0 and n%2 == 0)]
