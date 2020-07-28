# Time:  O(n)
# Space: O(1)
# 260
# Given an array of numbers nums, in which exactly two
# elements appear only once and all the other elements
# appear exactly twice. Find the two elements that appear only once.
#
# For example:
#
# Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].
#
# Note:
# The order of the result is not important. So in the
# above example, [5, 3] is also correct.
# Your algorithm should run in linear runtime complexity.
# Could you implement it using only constant space complexity?
import operator
import collections


class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def singleNumber(self, nums): # USE THIS
        # bit difference of the two nums appearing only once
        x_xor_y = reduce(operator.xor, nums)

        # rightmost 1, it must in x (or y) and must not in y (or x). e.g. 6(0110) & -6(1010) = 2(0010)
        bit =  x_xor_y & -x_xor_y

        x = 0
        for i in nums:
            if i & bit: x ^= i
        return [x, x ^ x_xor_y] # x ^ (x ^ y) = y
        ''' OR do more xor computation
        x = y = 0
        for i in nums:
            if i & bit: x^=i      # get number with the rightmost '1' bit
            else:       y^=i      # get number w/o the rightmost '1' bit
        return [x, y]
        '''

    def singleNumber2(self, nums): # space O(n)
        return [x[0] for x in sorted(collections.Counter(nums).items(), key=lambda i: i[1], reverse=False)[:2]]
