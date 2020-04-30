# Time:  O(logn) if input is sorted, otherwise O(n)
# Space: O(1)
#
# Given an array containing n distinct numbers taken from
# 0, 1, 2, ..., n, find the one that is missing from the array.
#
# For example,
# Given nums = [0, 1, 3] return 2.
#
# Note:
# Your algorithm should run in linear runtime complexity.
# Could you implement it using only constant extra space complexity?
#

import operator, functools


class Solution(object):
    # assume input is sorted.
    # binary search: find the smallest index i where nums[i] != i, except the edge case all nums[i]==i
    def missingNumber(self, nums):
        # edge case
        if nums[-1] == len(nums)-1: return len(nums)

        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] != m:
                r = m
            else:
                l = m + 1
        return l

    # bit op O(n)
    def missingNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing
        # OR
        #return functools.reduce(operator.xor, nums,
        #              functools.reduce(operator.xor, range(len(nums) + 1)))

    # sum O(n)
    def missingNumber3(self, nums):
        n = len(nums)
        return n*(n+1)//2 - sum(nums)

print(Solution().missingNumber([1,2,3,4,5,6,7,8,9])) # 0
print(Solution().missingNumber([0,2,3,4,5,6,7,8,9])) # 1
print(Solution().missingNumber([0,1,3,4,5,6,7,8,9])) # 2
print(Solution().missingNumber([0,1,2,4,5,6,7,8,9])) # 3
print(Solution().missingNumber([0,1,2,3,5,6,7,8,9])) # 4
print(Solution().missingNumber([0,1,2,3,4,6,7,8,9])) # 5
print(Solution().missingNumber([0,1,2,3,4,5,7,8,9])) # 6
print(Solution().missingNumber([0,1,2,3,4,5,6,8,9])) # 7
print(Solution().missingNumber([0,1,2,3,4,5,6,7,9])) # 8
print(Solution().missingNumber([0,1,2,3,4,5,6,7,8])) # 9