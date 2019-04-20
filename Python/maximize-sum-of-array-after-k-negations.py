# Time:  O(n) ~ O(n^2), O(n) on average.
# Space: O(1)

# 1005
# Given an array A of integers, we must modify the array in the following way: we choose an i and replace
# A[i] with -A[i], and we repeat this process K times in total.  (We may choose the same index i multiple times.)
#
# Return the largest possible sum of the array after modifying it in this way.

import random


# quick select solution: improve this to O(N) by quick selecting the Kth in the negative numbers.
class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        def kthElement(nums, k, compare):
            def PartitionAroundPivot(left, right, pivot_idx, nums, compare):
                new_pivot_idx = left
                nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
                for i in range(left, right):
                    if compare(nums[i], nums[right]):
                        nums[i], nums[new_pivot_idx] = nums[new_pivot_idx], nums[i]
                        new_pivot_idx += 1

                nums[right], nums[new_pivot_idx] = nums[new_pivot_idx], nums[right]
                return new_pivot_idx

            left, right = 0, len(nums) - 1
            while left <= right:
                pivot_idx = random.randint(left, right)
                new_pivot_idx = PartitionAroundPivot(left, right, pivot_idx, nums, compare)
                if new_pivot_idx == k - 1:
                    return
                elif new_pivot_idx > k - 1:
                    right = new_pivot_idx - 1
                else:  # new_pivot_idx < k - 1.
                    left = new_pivot_idx + 1
                    
        kthElement(A, K, lambda a, b: a < b)
        remain = K
        for i in range(K):
            if A[i] < 0:
                A[i] = -A[i]
                remain -= 1
        return sum(A) - ((remain)%2)*min(A)*2


# Time:  O(nlogn)
# Space: O(1)
class Solution2(object):
    # USE THIS: easy to understand, sort + modify
    # if not modify, hard to quickly find min(A)
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A.sort()
        i = 0
        while i < len(A) and A[i] < 0 and i < K:
            A[i] = -A[i]
            i += 1
        return sum(A) - (K - i) % 2 * min(A) * 2

    def largestSumAfterKNegations_kamyu(self, A, K): # not very good by introducing more var 'remain'
        A.sort()
        remain = K
        for i in range(K):
            if A[i] >= 0:
                break
            A[i] = -A[i]
            remain -= 1
        return sum(A) - (remain%2)*min(A)*2

print(Solution2().largestSumAfterKNegations([4,2,3], 1)) # 5
print(Solution2().largestSumAfterKNegations([3,-1,0,2], 3)) # 6
print(Solution2().largestSumAfterKNegations([2,-3,-1,5,-4], 2)) # 13