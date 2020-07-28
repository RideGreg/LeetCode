# Time:  O(logn) ~ O(n)
# Space: O(1)
# 154
# Follow up for "Find Minimum in Rotated Sorted Array":
# What if duplicates are allowed?
#
# Would this affect the run-time complexity? How and why?
# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
#
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#
# Find the minimum element.
#
# The array may contain duplicates.
#

class Solution(object):
    def findMin(self, nums): # USE THIS
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right and nums[left] >= nums[right]:  #prune: check whether search space already monotonic:
                    # 注意不能是要求 nums[left] > nums[right]。因为left和right相等时仍然需要二分检查，比如 3 3 3 1 1 3 3 3
            mid = left + (right - left) / 2

            if nums[mid] == nums[right]: #由于重复元素的存在，无法确定mid在最小值左或右，不能扔掉任一边。缩小右边界因为最小值一定还在
                right -= 1
            elif nums[mid] < nums[right]: # mid在最小值右侧
                right = mid
            else: # mid在最小值左侧
                left = mid + 1

        return nums[left]


class Solution2(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right and nums[left] >= nums[right]:
            mid = left + (right - left) / 2

            if nums[mid] == nums[left]:
                left += 1
            elif nums[mid] < nums[left]:
                right = mid
            else:
                left = mid + 1

        return nums[left]


if __name__ == "__main__":
    print Solution().findMin([3, 1, 1, 2, 2, 3])
    print Solution2().findMin([2, 2, 2, 3, 3, 1])
