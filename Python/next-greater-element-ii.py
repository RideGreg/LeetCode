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


# 单调递减栈
class Solution(object):
    def nextGreaterElements(self, nums): # USE THIS: easy to understand, 300ms
        n = len(nums)
        stk, ans = [], [-1]*n
        for i in range(n*2):
            while stk and nums[stk[-1]] < nums[i%n]:
                ans[stk.pop()] = nums[i%n]
            if i < n:   # if don't check this, get 'list index out of range' on line 39
                stk.append(i)
        return ans

    # Time O(n^2) 8000ms
    def nextGreaterElements_bruteFroce(self, nums):
        ans = []
        for i, x in enumerate(nums):
            for k in range(1, len(nums)):
                y = (i+k) % len(nums)
                if nums[y] > x:
                    ans.append(nums[y])
                    break
            else:
                ans.append(-1)
        return ans

print(Solution().nextGreaterElements([3,2,1,0])) # [-1,3,3,3]
print(Solution().nextGreaterElements([0,1,2,3])) # [1,2,3,-1]
print(Solution().nextGreaterElements([1,2,1,0])) # [2,-1,2,1]