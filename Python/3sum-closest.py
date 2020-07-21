# Time:  O(n^2)
# Space: O(1)

# 16
# Given an array S of n integers,
# find three integers in S such that the sum is closest to a given number,
# target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.
#
# For example, given array S = {-1 2 1 -4}, and target = 1.
#
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        ans = float('inf')
        for i in range(len(nums)-2):
            if i != 0 and nums[i] == nums[i-1]: continue # prune duplicates

            j, k = i+1, len(nums)-1
            while j < k:
                sm = nums[i] + nums[j] + nums[k]
                if abs(sm-target) < abs(ans-target):
                    ans = sm

                if sm == target:
                    return ans
                elif sm < target:
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                else:
                    k -= 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
        return ans
