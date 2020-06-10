# Time:  O(logn)
# Space: O(1)
# 35
# Given a sorted array and a target value, return the index if the target is found.
#
# If not, return the index where it would be if it were inserted in order.
#
# You may assume no duplicates in the array.
#
# Here are few examples.
# [1,3,5,6], 5 -> 2
# [1,3,5,6], 2 -> 1
# [1,3,5,6], 7 -> 4
# [1,3,5,6], 0 -> 0
#

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        import bisect
        return bisect.bisect_left(nums, target)

        # OR self implement: find minimal index i where nums[i] >= target
        l, r = 0, len(nums)
        while l < r:
            m = (l+r) // 2
            if nums[m] >= target:
                r = m
            else:
                l = m + 1
        return l


if __name__ == "__main__":
    print(Solution().searchInsert([1, 3, 5, 6], 5)) # 2
    print(Solution().searchInsert([1, 3, 5, 6], 2)) # 1
    print(Solution().searchInsert([1, 3, 5, 6], 7)) # 4
    print(Solution().searchInsert([1, 3, 5, 6], 0)) # 0
