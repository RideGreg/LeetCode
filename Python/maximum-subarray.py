# Time:  O(n)
# Space: O(1)
#
# 53
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
        ans, cur = float('-inf'), 0 # cur can be initialized as float('-inf')
        for n in nums:
            cur = max(0, cur) + n
            ans = max(ans, cur)
        return ans

    def maxSubArray_print_index(self, nums):
        cur, s = float('-inf'), 0
        ans = (float('-inf'), None, None)
        for i, n in enumerate(nums):
            if cur >= 0:
                cur = n + cur
            else:
                cur = n
                s = i
            if cur > ans[0]:
                ans = cur, s, i
        return ans

if __name__ == "__main__":
    print(Solution().maxSubArray_print_index([-2,1,-3,4,-1,2,1,-5,4])) # (6,3,6)
    print(Solution().maxSubArray_print_index([2,-3,-4])) # (2,0,0)
