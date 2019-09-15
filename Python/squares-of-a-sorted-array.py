# Time:  O(n)
# Space: O(1)

# 977
# Given an array of integers A sorted in non-decreasing order, return an array of the
# squares of each number, also in sorted non-decreasing order.
# Input: [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

class Solution(object):
    # Two pointers. Time O(n)
    def sortedSquares(self, A):
        pivot = min(xrange(len(A)), key=lambda i: abs(A[i]))
        ans = [A[pivot]**2]
        i, j = pivot-1, pivot+1
        while i>-1 or j<len(A):
            prev = A[i]**2 if i>-1 else float('inf')
            nex = A[j]**2 if j<len(A) else float('inf')
            if prev < nex:
                ans.append(prev)
                i -= 1
            else:
                ans.append(nex)
                j += 1
        return ans

    def sortedSquares2(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        right = 0
        while right < len(A) and A[right] < 0:
            right += 1
        left = right-1

        result = []
        while 0 <= left or right < len(A):
            if right == len(A) or \
               (0 <= left and A[left]**2 < A[right]**2):
                result.append(A[left]**2)
                left -= 1
            else:
                result.append(A[right]**2)
                right += 1
        return result

    # Sort. Time O(nlogn)
    def sortedSquares_sort(self, A):
        return sorted(x*x for x in A)
