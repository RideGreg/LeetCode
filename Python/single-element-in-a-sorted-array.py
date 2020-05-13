# Time:  O(logn)
# Space: O(1)

# 540
# Given a sorted array consisting of only integers
# where every element appears twice except for one element
# which appears once. Find this single element that appears only once.
#
# Example 1:
# Input: [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:
# Input: [3,3,7,7,10,11,11]
# Output: 10
# Note: Your solution should run in O(log n) time and O(1) space.


# 对所有三种算法，即使数组没有经过排序，只要将同一元素放在一起，该算法仍然起作用
# 顺序无关紧要，重要的是含有单个元素的子数组元素个数为奇数。

class Solution(object):
    # 对偶数索引进行二分搜索 O(logn)
    # 这是对方法3（线性搜索偶数索引）的优化。原数组是奇数长度；一对数应为偶-奇索引。
    # 取mid并调整为偶数索引，如果它与其后元素相同，则单个元素在其后；如果不同，则单个元素
    # 在mid或之前。一旦只剩一个元素，即为返回值。
    def singleNonDuplicate(self, nums): # USE THIS
        """
        :type nums: List[int]
        :rtype: int
        """
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if mid % 2 == 1:
                mid -= 1

            if nums[mid] == nums[mid + 1]:
                lo = mid + 2
            else:
                hi = mid
        return nums[lo]

    # 对所有索引进行二分搜索 O(logn)，需要判断的情况较多
    def singleNonDuplicate2(self, nums):
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            halves = hi - mid # mid后有几个数
            if nums[mid + 1] == nums[mid]:
                if halves % 2 == 0:
                    lo = mid + 2
                else:
                    hi = mid - 1
            elif nums[mid - 1] == nums[mid]:
                if halves % 2 == 0:
                    hi = mid - 2
                else:
                    lo = mid + 1
            else:
                return nums[mid]
        return nums[lo]


    # 对偶数索引进行线性搜索 Time O(n)
    def singleNonDuplicate3(self, nums):
        for i in range(0, len(nums) - 2, 2):
            if nums[i] != nums[i + 1]:
                return nums[i]
        return nums[-1]

print(Solution().singleNonDuplicate([1,1,2,3,3,4,4,8,8])) # 2