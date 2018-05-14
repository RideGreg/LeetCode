# Time:  O(logn)
# Space: O(1)
#
# Given a sorted array of integers, find the starting and ending position of a given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
# For example,
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return [3, 4].
#

class Solution(object):
    def searchRange_bisect(self, nums, target): # equavilent to using binarySearch API
        import bisect
        lindex = bisect.bisect_left(nums, target)
        if lindex >= len(nums) or nums[lindex] != target:
            return [-1, -1]
        rindex = bisect.bisect(nums, target)
        return [lindex, rindex-1]

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Find the first idx where nums[idx] >= target
        left = self.binarySearch(lambda x, y: x >= y, nums, target)
        if left >= len(nums) or nums[left] != target: #if not check equality, [5,7,7,8,8,10] 6 return [1,0] wrong
            return [-1, -1]
        # Find the first idx where nums[idx] > target
        right = self.binarySearch(lambda x, y: x > y, nums, target)
        return [left, right - 1]

    def binarySearch(self, compare, nums, target):
        left, right = 0, len(nums) #if use len(nums)-1, [2,2] 2 return [0, 0] wrong
        while left < right:
            mid = left + (right - left) / 2
            if compare(nums[mid], target):
                right = mid
            else:
                left = mid + 1
        return left

    def binarySearch2(self, compare, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if compare(nums[mid], target):
                right = mid - 1
            else:
                left = mid + 1
        return left

    def binarySearch3(self, compare, nums, target):
        left, right = -1, len(nums)
        while left + 1 < right:
            mid = left + (right - left) / 2
            if compare(nums[mid], target):
                right = mid
            else:
                left = mid
        return left if left != -1 and compare(nums[left], target) else right


if __name__ == "__main__":
    print Solution().searchRange([2, 2], 3)
    print Solution().searchRange([5, 7, 7, 8, 8, 10], 8)
