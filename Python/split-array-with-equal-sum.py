# Time:  O(n^2)
# Space: O(n)

# 548
# Given an array with n integers, find if there are triplets (i, j, k) which satisfies:
#
# 1. 0 < i, i + 1 < j, j + 1 < k < n - 1
# 2. Sum of subarrays (0, i - 1), (i + 1, j - 1), (j + 1, k - 1) and (k + 1, n - 1)
# should be equal.
# where we define that subarray (L, R) represents a slice of the original array starting
# from the element indexed L to the element indexed R.

class Solution(object):
    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 7:
            return False

        prefixSum = [0] * len(nums)
        prefixSum[0] = nums[0]
        for i in range(1, len(nums)):
            prefixSum[i] = prefixSum[i-1] + nums[i]
        for j in range(3, len(nums)-3):
            lookup = set()
            for i in range(1, j-1):
                if prefixSum[i-1] == prefixSum[j-1] - prefixSum[i]:
                    lookup.add(prefixSum[i-1])
            for k in range(j+2, len(nums)-1):
                if prefixSum[-1] - prefixSum[k] == prefixSum[k-1] - prefixSum[j] and \
                   prefixSum[k - 1] - prefixSum[j] in lookup:
                    return True
        return False

print(Solution().splitArray([1,9,2,10,90,2,8,22,3,5,2])) # True i,j,k = 2,4,7