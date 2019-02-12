# Time:  O(n)
# Space: O(1)

# 915
# Given an array A, partition it into two (contiguous) subarrays
# left and right so that:
#
# Every element in left is less than or equal to every element in right.
# left and right are non-empty.
# left has the smallest possible size.
# Return the length of left after such a partitioning.
# It is guaranteed that such a partitioning exists.
#
# Example 1:
#
# Input: [5,0,3,8,6]
# Output: 3
# Explanation: left = [5,0,3], right = [8,6]
# Example 2:
#
# Input: [1,1,1,0,6,12]
# Output: 4
# Explanation: left = [1,1,1,0], right = [6,12]
#
# Note:
# - 2 <= A.length <= 30000
# - 0 <= A[i] <= 10^6
# - It is guaranteed there is at least one way to partition A as described.

class Solution(object):
    # USE THIS. Ming solution Time O(n) Space(n)
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        leftMax, curMax, ans = A[0], A[0], 1
        for i in xrange(1, len(A)):
            curMax = max(curMax, A[i])
            if A[i] < leftMax:
                ans = i+1
                leftMax = curMax
        return ans

    def partitionDisjoint_LeetCodeOfficial(self, A):
        # check max(left) <= min(right).
        # Time: O(n), Space: O(n)
        N = len(A)
        maxleft = [None] * N
        minright = [None] * N

        m = A[0]
        for i in xrange(N):
            m = max(m, A[i])
            maxleft[i] = m

        m = A[-1]
        for i in xrange(N-1, -1, -1):
            m = min(m, A[i])
            minright[i] = m

        for i in xrange(1, N):
            if maxleft[i-1] <= minright[i]:
                return i

