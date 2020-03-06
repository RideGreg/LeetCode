# Time:  O(n)
# Space: O(1)

# 1330 biweekly contest 18 1/25/2020

# You are given an integer array nums. The value of this array is defined as the sum of |nums[i]-nums[i+1]|
# for all 0 <= i < nums.length-1.
#
# You are allowed to select any subarray of the given array and reverse it. You can perform this operation only once.
#
# Find maximum possible value of the final array.

# total calculate the total sum of |A[i] - A[j]|.
# impv record the value the we can improve.
#
# Assume the current pair is (a,b) = (A[i], A[i+1]).
#
# If we reverse all element from A[0] to A[i], improve abs(A[0] - b) - abs(a - b)
# If we reverse all element from A[i+1] to A[n-1], improve abs(A[n - 1] - a) - abs(a - b).

# Also find the optimal subarray whose edges are not nums[0] or nums[-1]:
# Assume the list is : x, y, ..., a, [b, ..., c], d, ..., and we are going to reverse [b, ..., c]
# Value only improved if interval [min(a,b), max(a,b)] does not intersect with [min(c,d), max(c,d)],
# and the improvement is 2 * (min(c,d) - max(a,b)). So  find out max(min(c,d) for any c,d) and min(max(a,b) for any a,b)).
# Also compare the boundary situation

class Solution(object):
    def maxValueAfterReverse(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total, impv, valley, peak = 0, 0, float('inf'), -float('inf')
        for i in range(1, len(nums)):
            a, b = nums[i-1], nums[i]
            total += abs(a - b)
            impv = max(impv, abs(nums[0] - b) - abs(a - b))
            impv = max(impv, abs(nums[-1] - a) - abs(a - b))
            valley, peak = min(valley, max(a, b)), max(peak, min(a, b))
        return total + max(impv, (peak - valley) * 2)

print(Solution().maxValueAfterReverse([2, 3, 1, 5, 4])) # 10 reverse to [2,5,1,3,4]
print(Solution().maxValueAfterReverse([2,4,9,24,2,1,10])) # 68