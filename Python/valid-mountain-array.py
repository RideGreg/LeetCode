# Time:  O(n)
# Space: O(1)

# 941
# Given an array A of integers, return true if and only if it is a valid mountain array.
# Recall that A is a mountain array if and only if:
#
# 1. A.length >= 3
# 2. There exists some i with 0 < i < A.length - 1 such that:
# A[0] < A[1] < ... A[i-1] < A[i]
# A[i] > A[i+1] > ... > A[B.length - 1]

# [2,1] -> False, [3,5,5] -> False, [0,3,2,1] = True

class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        i = 0
        while i+1 < len(A) and A[i] < A[i+1]:
            i += 1
        j = len(A)-1
        while j-1 >= 0 and A[j-1] > A[j]:
            j -= 1
        return 0 < i == j < len(A)-1

    # One passs from left to right
    def validMountainArray_LeetCodeOfficial(self, A):
        N = len(A)
        i = 0

        # walk up
        while i+1 < N and A[i] < A[i+1]:
            i += 1

        # peak can't be first or last
        if i == 0 or i == N-1:
            return False

        # walk down
        while i+1 < N and A[i] > A[i+1]:
            i += 1

        return i == N-1