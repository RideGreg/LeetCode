# Time:  O(1)
# Space: O(1)
# 231
# Given an integer, write a function to determine if it is a power of two.


# BitOps skill:
# 1. get rightmost 1: x & (-x)
# 2. set rightmost 1 to 0: x & (x-1)

class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        return n > 0 and (n & (n - 1)) == 0

    def isPowerOfTwo2(self, n):
        return n > 0 and (n & -n) == n

    # Time O(logn)
    def isPowerOfTwo3(self, n):
        if n <= 0:
            return False
        while n % 2 == 0:
            n /= 2
        return n == 1
