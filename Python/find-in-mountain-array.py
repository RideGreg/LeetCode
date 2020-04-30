# Time:  O(logn)
# Space: O(1)

# 1095
# (This problem is an interactive problem.)
#
# You may recall that an array A is a mountain array if and only if:
#   1. A.length >= 3
#   2. There exists some i with 0 < i < A.length - 1 such that:
#      A[0] < A[1] < ... A[i-1] < A[i], and A[i] > A[i+1] > ... > A[A.length - 1]

# Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target.
# If such an index doesn't exist, return -1.
#
# You can't access the mountain array directly.  You may only access the array using a MountainArray interface:
#   MountainArray.get(k) returns the element of the array at index k (0-indexed).
#   MountainArray.length() returns the length of the array.
# Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer.  Also, any solutions
# that attempt to circumvent the judge will result in disqualification.


# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class MountainArray(object):
    def __init__(self, nums):
        self.nums = nums
    def get(self, index: int) -> int:
        return self.nums[index]
    def length(self):
        return len(self.nums)

class Solution(object):
    def findInMountainArray(self, target, mountain_arr):
        """
        :type target: integer
        :type mountain_arr: MountainArray
        :rtype: integer
        """
        def bisearch(l, r, check):
            while l < r:
                m = (l + r) // 2
                if check(m):
                    r = m
                else:
                    l = m + 1
            return l

        N = mountain_arr.length()
        peak = bisearch(0, N-1, lambda x: mountain_arr.get(x) > mountain_arr.get(x+1))
        # search left side (mono increasing)
        i = bisearch(0, peak, lambda x: mountain_arr.get(x) >= target)
        if mountain_arr.get(i) == target:
            return i
        # search right side (mono decreasing)
        i = bisearch(peak+1, N-1, lambda x: mountain_arr.get(x) <= target)
        if mountain_arr.get(i) == target:
            return i
        return -1

    # 1st binary_search is written differently with the 2nd/3rd binary_search
    def findInMountainArray_leetcodeCNofficial(self, target: int, mountain_arr: 'MountainArray') -> int:
        def bisearch(a, l, r, target, transform):
            target = transform(target)
            while l <= r:
                m = (l+r)//2
                cur = transform(a.get(m))
                if cur == target:
                    return m
                elif cur > target:
                    r = m - 1
                else:
                    l = m + 1
            return -1

        N = mountain_arr.length()
        l, r = 0, N - 1
        while l < r:
            m = (l+r) // 2
            if mountain_arr.get(m) < mountain_arr.get(m+1):
                l = m + 1
            else:
                r = m
        peak = l
        # search left side (mono increasing)
        i = bisearch(mountain_arr, 0, peak, target, lambda x: x)
        if i != -1:
            return i
        # search right side (mono decreasing)
        i = bisearch(mountain_arr, peak+1, N-1, target, lambda x: -x)
        return i

print(Solution().findInMountainArray(3, MountainArray([1,2,3,4,5,3,1]))) # 2
print(Solution().findInMountainArray(3, MountainArray([0,1,2,4,2,1]))) # -1