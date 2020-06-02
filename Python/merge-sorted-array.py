# Time:  O(n)
# Space: O(1)
# 88
# Given two sorted integer arrays A and B, merge B into A as one sorted array.
#
# Note:
# You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B.
# The number of elements initialized in A and B are m and n respectively.
#

class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        while m > 0 and n > 0:
            if A[m-1] > B[n-1]:
                A[m+n-1] = A[m-1]
                m -= 1
            else:
                A[m+n-1] = B[n-1]
                n -= 1
        while n > 0:
            A[n-1] = B[n-1]
            n -= 1
        ''' List slice creates a new list, bad space complexity
        if n > 0:
            A[:n] = B[:n]  # Space: O(n),
                                   # Reference:
                                   # - https://stackoverflow.com/questions/4948293/python-slice-assignment-memory-usage
                                   # - https://stackoverflow.com/questions/10623302/how-assignment-works-with-python-list-slice
        '''

    def merge2(self, A, m, B, n):
        last, i, j = m + n - 1, m - 1, n - 1

        while i >= 0 and j >= 0:
            if A[i] > B[j]:
                A[last] = A[i]
                last, i = last - 1, i - 1
            else:
                A[last] = B[j]
                last, j = last - 1, j - 1

        while j >= 0:
                A[last] = B[j]
                last, j = last - 1, j - 1

if __name__ == "__main__":
    A = [1, 3, 5, 0, 0, 0, 0]
    B = [2, 4, 6, 7]
    Solution().merge(A, 3, B, 4)
    print(A)

