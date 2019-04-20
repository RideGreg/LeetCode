# Time:  O(nlogn)
# Space: O(1)

# 976
# Given an array A of positive lengths, return the largest perimeter of a triangle with non-zero area,
# formed from 3 of these lengths.
#
# If it is impossible to form any triangle of non-zero area, return 0.

class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        for i in reversed(xrange(len(A) - 2)):
            if A[i] + A[i+1] > A[i+2]:
                return A[i] + A[i+1] + A[i+2]
        return 0
