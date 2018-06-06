# Time:  O(n)
# Space: O(1)

'''
Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.

Example 1:

Input: [1,0,1,1,0]
Output: 4
Explanation: Flip the first zero will get the the maximum number of consecutive 1s.
    After flipping, the maximum number of consecutive 1s is 4.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
'''

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result, prev, curr = 0, 0, 0
        for n in nums:
            if n == 0:
                prev, curr = curr, 0
            else:
                curr += 1
            result = max(result, prev + curr + 1)
        return min(result, len(nums))  # for all 1 array edge case
