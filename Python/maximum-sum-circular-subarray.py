# Time:  O(n)
# Space: O(1)

# 918
# Given a circular array C of integers represented by A,
# find the maximum possible sum of a non-empty subarray of C.
#
# Here, a circular array means the end of the array connects to the beginning of the array.
# (Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)
#
# Also, a subarray may only include each element of the fixed buffer A at most once.
# (Formally, for a subarray C[i], C[i+1], ..., C[j],
# there does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)
#
# Example 1:
#
# Input: [1,-2,3,-2]
# Output: 3
# Explanation: Subarray [3] has maximum sum 3
# Example 2:
#
# Input: [5,-3,5]
# Output: 10
# Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10
# Example 3:
#
# Input: [3,-1,2,-1]
# Output: 4
# Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4
# Example 4:
#
# Input: [3,-2,2,-3]
# Output: 3
# Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3
# Example 5:
#
# Input: [-2,-3,-1]
# Output: -1
# Explanation: Subarray [-1] has maximum sum -1
#
# Note:
# - -30000 <= A[i] <= 30000
# - 1 <= A.length <= 30000


# The answer is a subarray either not cross boundary (max-sum non-circular subarray) or cross boundary (max-sum
# circular subarray). We take the max from the above two. The first is a classical problem LeetCode 53,
# the second can be got by (sum of array - min-sum non-circular subarray).
class Solution(object):
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        total, cur_max, cur_min = 0, 0, 0
        global_max, global_min = -float("inf"), float("inf")
        for a in A:
            cur_max = max(cur_max, 0) + a
            global_max = max(global_max, cur_max)
            cur_min = min(cur_min, 0) + a
            global_min = min(global_min, cur_min)
            total += a
        return max(global_max, total-global_min) if global_max >= 0 else global_max # >= 0 or > 0

    # Time O(n^2)
    def maxSubarraySumCircular_TLE(self, A):
        def helper(nums):
            ans, cur = nums[0], nums[0]
            for n in nums[1:]:
                cur = max(0, cur) + n
                ans = max(ans, cur)
            return ans

        B = A * 2
        return max(helper(B[i:i + len(A)]) for i in xrange(A))

print(Solution().maxSubarraySumCircular([5,-3,6]))
