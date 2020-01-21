# Time:  O(logn)
# Space: O(1)

# 1283 weekly contest 166 12/7/2019

# Given an array of integers nums and an integer threshold, we will choose a positive integer divisor and divide
# all the array by it and sum the result of the division. Find the smallest divisor such that the result mentioned
# above is less than or equal to threshold.
#
# Each result of division is rounded to the nearest integer greater than or equal to that element.
# (For example: 7/3 = 3 and 10/2 = 5).
#
# It is guaranteed that there will be an answer.
# Constraints:
#
#     1 <= nums.length <= 5 * 10^4
#     1 <= nums[i] <= 10^6
#     nums.length <= threshold <= 10^6

class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        def check(d):
            return sum((n-1)//d + 1 for n in nums) <= threshold
            #return sum(math.ceil(n / d) for n in nums) <= threshold

        left, right = 1, max(nums)
        while left < right:
            mid = left + (right-left)//2
            if check(mid):
                right = mid
            else:
                left = mid+1
        return left

print(Solution().smallestDivisor([1,2,5,9], 6)) # 5
print(Solution().smallestDivisor([2,3,5,7,11], 11)) # 3
print(Solution().smallestDivisor([19], 5)) # 4