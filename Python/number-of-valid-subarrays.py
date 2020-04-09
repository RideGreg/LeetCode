# Time:  O(n)
# Space: O(n)

# 1063
# Given an array A of integers, return the number of non-empty continuous subarrays
# that satisfy the following condition:
# The leftmost element of the subarray is not larger than other elements in the subarray.

class Solution(object):
    def validSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        s = []
        for num in nums:  # reverse traversal to solve rightmost element
            while s and s[-1] > num: # change to >=, <, <= can solve array w/ first elem less than / not less than / greater than
                s.pop()
            s.append(num)
            result += len(s)
        return result

print(Solution().validSubarrays([1,4,2,5,3])) # 11 [1]; [1,4] [4]; [1,4,2] [2]; [1,4,2,5] [2,5] [5]; [1,4,2,5,3] [2,5,3] [3]
print(Solution().validSubarrays([3,2,1])) # 3
print(Solution().validSubarrays([2,2,2])) # 6
