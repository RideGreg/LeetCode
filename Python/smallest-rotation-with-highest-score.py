# Time:  O(n)
# Space: O(n)

# Given an array A, we may rotate it by a non-negative integer K
# so that the array becomes A[K], A[K+1], A{K+2], ... A[A.length - 1], A[0], A[1], ..., A[K-1].
# Afterward, any entries that are less than or equal to their index are worth 1 point.
#
# For example, if we have [2, 4, 1, 3, 0], and we rotate by K = 2,
# it becomes [1, 3, 0, 2, 4].
# This is worth 3 points because 1 > 0 [no points], 3 > 1 [no points],
# 0 <= 2 [one point], 2 <= 3 [one point], 4 <= 4 [one point].
#
# Over all possible rotations,
# return the rotation index K that corresponds to the highest score we could receive.
# If there are multiple answers, return the smallest such index K.
#
# Example 1:
# Input: [2, 3, 1, 4, 0]
# Output: 3
# Explanation:
# Scores for each K are listed below:
# K = 0,  A = [2,3,1,4,0],    score 2
# K = 1,  A = [3,1,4,0,2],    score 3
# K = 2,  A = [1,4,0,2,3],    score 3
# K = 3,  A = [4,0,2,3,1],    score 4
# K = 4,  A = [0,2,3,1,4],    score 3
# So we should choose K = 3, which has the highest score.
#
# Example 2:
# Input: [1, 3, 0, 2, 4]
# Output: 0
# Explanation:  A will always have 3 points no matter how it shifts.
# So we will choose the smallest K, which is 0.
#
# Note:
# - A will have length at most 20000.
# - A[i] will be in the range [0, A.length].

# Interval Stabbing
#
# Intuition
# Say N = 10 and A[2] = 5. Then there are 5 rotations that are bad for this number: rotation indexes 0, 1, 2, 8, 9.
#
# In general, for each number in the array, we can map out what rotation indexes will be bad for this number.
# It will always be a region of 1 interval, possibly 2 if the interval wraps around (eg. 8, 9, 0, 1, 2 wraps around, to become [8, 9] and [0, 1, 2].)
#
# At the end of plotting these intervals, we need to know which rotation index has the least intervals overlapping it - this one is the answer.
#
# Algorithm
# First, an element like A[2] = 5 will not get score in 5 positions: when the 5 is at final index 0, 1, 2, 3, or 4.
# val:            A[i]
# id:   0  1  2 .. i .. A[i]-1
# When we shift by 2, we'll get final index 0. If we shift opporite direction by A[i]-1-i, this elem ends up at final index A[i]-1.
# In general (modulo N), a shift of i - (A[i]-1) to i will be the rotation indexes that will make A[i] not score a point.
#
# Don't mark all bad shifts 0,1,2,3,4,5, which leads to O(n^2) time complexity. We mark the double ends, and do accumulation at the end.
# To plot an interval like [2, 3, 4], then instead of doing bad[2]--; bad[3]--; bad[4]--;, what we will do instead
# is keep track of the cumulative total: bad[2]--; bad[5]++. For "wrap-around" intervals like [8, 9, 0, 1, 2], we will
# keep track of this as two separate intervals: bad[8]--, bad[10]++, bad[0]--, bad[3]++. (Actually, because our implementation
# ends at bad[9], we don't need to remember the bad[10]++ part.)
#
# At the end, we want to find a rotation index with the least intervals overlapping. We'll maintain a cumulative total cur
# representing how many intervals are currently overlapping our current rotation index, then update it as we step through each rotation index.

class Solution(object):
    def bestRotation(self, A):  # USE THIS
        N = len(A)
        badShift = [0] * N
        for i, x in enumerate(A):
            left, right = (i - x + 1) % N, (i + 1) % N
            badShift[left] -= 1
            badShift[right] += 1
            if left > right:
                badShift[0] -= 1

        for i in xrange(1, N):
            badShift[i] += badShift[i-1]

        return badShift.index(max(badShift))

    def bestRotation_kamyu(self, A):  # don't understand
        """
        :type A: List[int]
        :rtype: int
        """
        N = len(A)
        change = [1] * N
        for i in xrange(N):
            change[(i-A[i]+1)%N] -= 1
        for i in xrange(1, N):
            change[i] += change[i-1]
        return change.index(max(change))

print(Solution().bestRotation([2,3,1,4,0]))
