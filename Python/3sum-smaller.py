# Time:  O(n^2)
# Space: O(1)

# Given an array of n integers nums and a target, find the number of index triplets i, j, k 
# with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.
# For example, given nums = [-2, 0, 1, 3], and target = 2.
# Return 2. Because there are two triplets which sums are less than 2.

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumSmaller(self, nums, target):
        nums.sort()
        n = len(nums)

        count, k = 0, 2
        while k < n:
            i, j = 0, k - 1
            while i < j:  # Two Pointers, linear time.
                if nums[i] + nums[j] + nums[k] >= target:
                    j -= 1
                else:
                    count += j - i
                    i += 1
            k += 1

        return count
