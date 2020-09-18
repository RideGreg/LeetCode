# Time:  O(n) ~ O(n^2)
#        O(n) on average, using Median of Medians could achieve O(n) (Intro Select)
# Space: O(logn), use stack space for recursive call

# 215
# Find the kth largest element in an unsorted array. Note that it is
# the kth largest element in the sorted order, not the kth distinct element.

from random import randint


# optimized for duplicated nums
class Solution2(object):  # kamyu's tri_partition solution. need to research
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def nth_element(nums, n, compare=lambda a, b: a < b):
            def tri_partition(nums, left, right, target, compare):
                mid = left
                while mid <= right:
                    if nums[mid] == target:
                        mid += 1
                    elif compare(nums[mid], target):
                        nums[left], nums[mid] = nums[mid], nums[left]
                        left += 1
                        mid += 1
                    else:
                        nums[mid], nums[right] = nums[right], nums[mid]
                        right -= 1
                return left, right

            left, right = 0, len(nums)-1
            while left <= right:
                pivot_idx = randint(left, right)
                pivot_left, pivot_right = tri_partition(nums, left, right, nums[pivot_idx], compare)
                if pivot_left <= n <= pivot_right:
                    break
                elif pivot_left > n:
                    right = pivot_left-1
                else:  # pivot_right < n.
                    left = pivot_right+1
            return nums[n]

        return nth_element(nums, k-1, compare=lambda a, b: a > b)


# Time:  O(n) on average, using Median of Medians could achieve O(n) (Intro Select)
# Space: O(1)
class Solution2(object):
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        def partition(l, r):
            # random pick a pivot value in order to make time complexity close to O(n)
            # If just use right end as pivot value, worse case time complexity is O(n^2)
            pivot_idx = randint(l, r)
            nums[pivot_idx], nums[r] = nums[r], nums[pivot_idx]

            ans = l
            for i in range(l, r):
                if nums[i] > nums[r]:    # also ok to use >=. If ask KthSmallest, use <
                    nums[ans], nums[i] = nums[i], nums[ans]
                    ans += 1

            nums[ans], nums[r] = nums[r], nums[ans]
            return ans

        l, r = 0, len(nums)-1
        while l < r:    # ok to use l<=r, but one more unnecessary call to partition
            idx = partition(l, r)
            if idx == k-1: return nums[idx]
            elif idx < k-1: l = idx + 1
            else: r = idx - 1
        return nums[l]



    def findKthLargest2(self, nums, k):
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot_idx = randint(left, right)
            new_pivot_idx = self.PartitionAroundPivot(left, right, pivot_idx, nums)
            if new_pivot_idx == k - 1:
                return nums[new_pivot_idx]
            elif new_pivot_idx > k - 1:
                right = new_pivot_idx - 1
            else:  # new_pivot_idx < k - 1.
                left = new_pivot_idx + 1

    def PartitionAroundPivot(self, left, right, pivot_idx, nums):
        pivot_value = nums[pivot_idx]
        new_pivot_idx = left
        nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
        for i in range(left, right):
            if nums[i] > pivot_value:
                nums[i], nums[new_pivot_idx] = nums[new_pivot_idx], nums[i]
                new_pivot_idx += 1

        nums[right], nums[new_pivot_idx] = nums[new_pivot_idx], nums[right]
        return new_pivot_idx


# sorted = [1,2,2,3,3,4,5,5,6]
print(Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 1)) # 6
print(Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 2)) # 5
print(Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 3)) # 5
print(Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 4)) # 4
print(Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 5)) # 3
print(Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 6)) # 3
print(Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 7)) # 2
print(Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 8)) # 2
print(Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 9)) # 1