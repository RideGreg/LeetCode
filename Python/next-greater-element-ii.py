# Time:  O(n)
# Space: O(n)

# 503
# Given a circular array (the next element of the last element is the first element of the array),
# print the Next Greater Number for every element.
# The Next Greater Number of a number x is the first greater number to its traversing-order next in the array,
# which means you could search circularly to find its next greater number.
# If it doesn't exist, output -1 for this number.
#
# Example 1:
# Input: [1,2,1]
# Output: [2,-1,2]
# Explanation: The first 1's next greater number is 2;
# The number 2 can't find next greater number;
# The second 1's next greater number needs to search circularly, which is also 2.
# Note: The length of given array won't exceed 10000.

class Solution(object):
    def nextGreaterElements_kamyu(self, nums): # hard to understand: reverse loop, keep greater in stack
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result, stk = [0] * len(nums), []
        for i in reversed(range(2*len(nums))):
            while stk and stk[-1] <= nums[i % len(nums)]:
                stk.pop()
            result[i % len(nums)] = stk[-1] if stk else -1
            stk.append(nums[i % len(nums)])
        return result

    def nextGreaterElements(self, nums): # USE THIS: easy to understand
        L = len(nums)
        stk, ans = [], [-1]*L
        for i in range(len(nums)*2):
            while stk and nums[i%L] > nums[stk[-1]]:
                ans[stk.pop()] = nums[i%L]
            if i < L:
                stk.append(i)

        return ans

    # actually we can just traverse index 0->L twice, no need 0->2*L and module
    def nextGreaterElements(self, nums):
        L = len(nums)
        stk, ans = [], [-1]*L
        for i in list(range(len(nums)))*2:
            while stk and nums[i] > nums[stk[-1]]:
                ans[stk.pop()] = nums[i]
            stk.append(i)

        return ans