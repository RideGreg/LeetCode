# Time:  O(logn)
# Space: O(1)
#
# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
#
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#
# Find the minimum element.
#
# You may assume no duplicate exists in the array.
#

# 考虑区间最右边的数x，最小值右侧的元素都<= x，最小值左侧的元素都>= x。利用此性质二分查找。
class Solution(object):
    def findMin(self, nums):  # hard to understand!!!
        left, right = 0, len(nums)
        target = nums[-1]

        while left < right:
            mid = left + (right - left) / 2

            if nums[mid] <= target:
                right = mid
            else:
                left = mid + 1

        return nums[left]


class Solution2(object):
    def findMin(self, nums):   # USE THIS
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right and nums[left] >= nums[right]:  #prune: check whether search space already monotonic
            mid = left + (right - left) / 2

            # should compare to right, because: 1. left and mid may be same. 2. we check whether mid->right is
            # mono-increasing. If right half is monotonic, then min must be left half increasing slope.
            if nums[mid] < nums[right]: # mid在最小值右侧
                right = mid
            else:   # mid在最小值左侧。或者考虑right half is not monotonic, then min must be at the gap in right half.
                left = mid + 1

        return nums[left]    #doesn't matter return left or right, because left equals to right


if __name__ == "__main__":
    print Solution().findMin([1])
    print Solution().findMin([1, 2])
    print Solution().findMin([2, 1])
    print Solution().findMin([3, 1, 2])
    print Solution().findMin([2, 3, 1])
