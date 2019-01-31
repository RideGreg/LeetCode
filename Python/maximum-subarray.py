# Time:  O(n)
# Space: O(1)
#
# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
#
# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.
#
# click to show more practice.
#
# More practice:
# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
#

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Kadane's algorithm
        ans, cur = float('-inf'), 0
        for n in nums:
            cur = max(0, cur) + n
            ans = max(ans, cur)
        return ans

    def maxSubArray_print_index(self, nums):
        localMax, gMax = nums[0], nums[0]
        start, end, s = 0, 0, 0
        for i, n in enumerate(nums[1:], 1):
            if localMax >= 0:
                localMax = n + localMax
            else:
                localMax = n
                s = i
            if localMax > gMax:
                gMax, start, end = localMax, s, i
        return gMax, start, end

if __name__ == "__main__":
    print Solution().maxSubArray_print_index([-2,1,-3,4,-1,2,1,-5,4])
