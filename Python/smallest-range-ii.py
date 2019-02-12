# Time:  O(nlogn)
# Space: O(1)

# 910
# Given an array A of integers, for each integer A[i]
# we need to choose either x = -K or x = K, and add x to A[i] (only once).
#
# After this process, we have some array B.
#
# Return the smallest possible difference
# between the maximum value of B and the minimum value of B.
#
# Example 1:
#
# Input: A = [1], K = 0
# Output: 0
# Explanation: B = [1]
# Example 2:
#
# Input: A = [0,10], K = 2
# Output: 6
# Explanation: B = [2,8]
# Example 3:
#
# Input: A = [1,3,6], K = 3
# Output: 3
# Explanation: B = [4,6,3]
#
# Note:
# - 1 <= A.length <= 10000
# - 0 <= A[i] <= 10000
# - 0 <= K <= 10000

# Solution:
# Intuition is increase smaller A[i] (go up) and decrease larger A[i] (go down).
# Formalize this concept: if A[i] < A[j], we don't need to consider when A[i] goes down
# while A[j] goes up. Because the interval (A[i]+K, A[j]-K) is a subset of (A[i]-K, A[j]+K).
#
# For sorted A, *say A[i] is the largest i that goes up.* We don't care A[j]-K for 0<=j<i due to
# the above reason. Both A[0]+K, A[1]+K, ... A[i]+K and A[i+1]-K, A[i+2]-K, ... A[-1]-K are
# mono increasing sequences, we only care the extremal values at 2 ends.
# Then A[0]+K, A[i]+K, A[i+1]-K, A[-1]-K are the only relevant values for calculating the answer:
# every other value is between one of these extremal values.

class Solution(object):
    def smallestRangeII(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A.sort()
        result = A[-1]-A[0] # this is the answer if A[-1] is the largest i that goes up
        for i in xrange(len(A)-1):
            result = min(result,
                         max(A[i]+K, A[-1]-K) - min(A[0]+K, A[i+1]-K))
            #            high ends of 2 sequences - low ends of 2 sequences
        return result
