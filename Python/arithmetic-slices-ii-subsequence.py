# Time:  O(n^2)
# Space: O(n * d)

# 446
# A sequence of numbers is called arithmetic if it consists of
# at least three elements
# and if the difference between any two consecutive elements is the same.
#
# For example, these are arithmetic sequences:
#
# 1, 3, 5, 7, 9
# 7, 7, 7, 7
# 3, -1, -5, -9
# The following sequence is not arithmetic.
#
# 1, 1, 2, 5, 7
#
# A zero-indexed array A consisting of N numbers is given.
# A subsequence slice of that array is any sequence of integers
# (P0, P1, ..., Pk)
# such that 0 ≤ P0 < P1 < ... < Pk < N.
#
# A subsequence slice (P0, P1, ..., Pk) of array A is called arithmetic
# if the sequence A[P0], A[P1], ..., A[Pk-1], A[Pk] is arithmetic.
# In particular, this means that k >= 2.
#
# The function should return the number of arithmetic subsequence
# slices in the array A.
#
# The input contains N integers. Every integer is in the range of
# -2^31 and 2^31-1 and 0 <= N <= 1000.
# The output is guaranteed to be less than 2^31-1.
#
#
# Example:
#
# Input: [2, 4, 6, 8, 10]
#
# Output: 7
#
# Explanation:
# All arithmetic subsequence slices are:
# [2,4,6]
# [4,6,8]
# [6,8,10]
# [2,4,6,8]
# [4,6,8,10]
# [2,4,6,8,10]
# [2,6,10]

import collections

try:
    xrange          # Python 2
except NameError:
    xrange = range  # Python 3


# DP: dp[i, d] stores the COUNT of arithmetic subsequence with diff d and ending at i.
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ans = 0
        dp = collections.defaultdict(int) #single item has zero count, a pair items has 1 count
        for i in range(len(A)):
            for j in range(i):
                d = A[i] - A[j]
                dp[i, d] += (dp[j, d] + 1) # increment, not assign
                ans += dp[j, d]
        return ans

    def numberOfArithmeticSlices_kamyu(self, A):
        result = 0
        dp = [collections.defaultdict(int) for _ in xrange(len(A))]
        for i in xrange(len(A)):
            for j in xrange(i):
                diff = A[i]-A[j]
                dp[i][diff] += 1
                if diff in dp[j]:
                    dp[i][diff] += dp[j][diff]
                    result += dp[j][diff]
        return result

    # cannot use same algorithm for longest arithmetic subsequence. Wrong on [2,2,3,4]
    # need to record COUNT, not LENGTH.
    def numberOfArithmeticSlices_wrong(self, A):
        ans = 0
        dp = collections.defaultdict(lambda: 1)
        for i in range(len(A)):
            for j in range(i):
                d = A[i] - A[j]
                dp[i,d] = dp[j,d] + 1  # LENGTH rely on prev item; COUNT should self-increment
                ans += max(0, dp[i,d] - 2)
        return ans

print(Solution().numberOfArithmeticSlices([2,4,6,8,10])) # 7
print(Solution().numberOfArithmeticSlices([2,2,3,4])) # 2