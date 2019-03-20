# Time:  O(nlogs), s is the sum of nums
# Space: O(1)

# 410
# Given an array which consists of non-negative integers and an integer m,
# you can split the array into m non-empty continuous subarrays.
# Write an algorithm to minimize the largest sum among these m subarrays.
#
# Note:
# Given m satisfies the following constraint: 1 <= m <= length(nums) <= 14,000.
#
# Examples:
#
# Input:
# nums = [7,2,5,10,8]
# m = 2
#
# Output:
# 18
#
# Explanation:
# There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8],
# where the largest sum among the two subarrays is only 18.

# Minimize the largest subarray sum.
class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        def canSplit(nums, m, s):
            curr_sum = 0
            for num in nums:
                if curr_sum + num > s:
                    curr_sum = 0
                    m -= 1
                    if m <= 0: return False
                curr_sum += num
            return True


        left, right = max(nums), sum(nums)
        left = max(left, int(math.ceil(right/m))) #optimization, search range low end is max(largest item, subarray average)
        while left <= right:
            mid = left + (right - left) / 2

            if canSplit(nums, m, mid):
                right = mid
            else:
                left = mid + 1
        return left


# Time:  O(nlogs), s is the sum of nums
# Space: O(1)

# Maximize the smallest subarray sum.
class SolutionFindMaxMin(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        def canSplit(nums, m, s):
            cnt, curr_sum = 1, 0
            for num in nums:
                curr_sum += num
                if curr_sum > s:
                    curr_sum = 0
                    cnt += 1
            return cnt <= m

        left, right = min(nums), sum(nums)
        while left <= right:
            mid = left + (right - left) / 2
            x = canSplit(nums, m, mid)
            if x:
                right = mid - 1
            else:
                left = mid + 1
        return left
