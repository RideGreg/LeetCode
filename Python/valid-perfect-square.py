# Time:  O(logn)
# Space: O(1)

# 367
# Given a positive integer num, write a function
# which returns True if num is a perfect square else False.
#
# Note: Do not use any built-in library function such as sqrt.
#
# Example 1:
#
# Input: 16
# Returns: True
# Example 2:
#
# Input: 14
# Returns: False

class Solution(object):
    def isPerfectSquare(self, num): # USE THIS: similar to sqrt.py. find max y where y**2 <= x
        """
        :type num: int
        :rtype: bool
        """
        if num < 2: return True
        l, r = 1, num // 2
        while l < r:
            m = (r - l + 1) // 2 + l
            if m*m <= num:
                l = m
            else:
                r = m - 1
        return l ** 2 == num

    def isPerfectSquare_kamyu(self, num):
        left, right = 1, num
        while left <= right:
            mid = left + (right - left) / 2
            if mid >= num / mid:
                right = mid - 1
            else:
                left = mid + 1
        return left == num / left and num % left == 0
