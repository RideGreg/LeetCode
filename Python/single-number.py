# Time:  O(n)
# Space: O(1)
#
# Given an array of integers, every element appears twice except for one. Find that single one.
#
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
#

import functools, operator


class Solution:
    """
    :type nums: List[int]
    :rtype: int
    """
    def singleNumber(self, A):
        return functools.reduce(operator.xor, A)

    # Space O(n), need set to store items
    def singleNumber2(self, A):
        return sum(set(A)) * 2 - sum(A)

if __name__ == '__main__':
    print(Solution().singleNumber([1, 1, 2, 2, 3]))
