# Time:  O(n)
# Space: O(1)

# 978
# A subarray A[i], A[i+1], ..., A[j] of A is said to be turbulent if and only if:
# - For i <= k < j, A[k] > A[k+1] when k is odd, and A[k] < A[k+1] when k is even;
# - OR, for i <= k < j, A[k] > A[k+1] when k is even, and A[k] < A[k+1] when k is odd.

# That is, the subarray is turbulent if the comparison sign flips between each adjacent
# pair of elements in the subarray.
#
# Return the length of a maximum size turbulent subarray of A.
#
# Example 1:
# Input: [9,4,2,10,7,8,8,1,9]
# Output: 5
# Explanation: (A[1] > A[2] < A[3] > A[4] < A[5])

class Solution(object):
    # Solution: sliding window
    # If we are at the end of a window (last elements OR it stopped alternating), then we
    # record the length of that window as our candidate answer, and set the start of a new window.
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ans = 1
        start = 0
        for i in xrange(1, len(A)):
            c = cmp(A[i-1], A[i])
            if c == 0:
                start = i
            elif i == len(A)-1 or c * cmp(A[i], A[i+1]) != -1:
                ans = max(ans, i-start+1)
                start = i
        return ans

    # Dynamic programming. Time O(n), Space O(n). Many values stored in dp array are not needed.
    # E.g up/down values followed by a comma is not useful.
    # A =  [9, 4,2,10,7,8,8,1,9]
    # up=   1  1 1,3  1,5 1 1,3
    # down= 1, 2 2 1, 4 1,1,2 1,
    def maxTurbulenceSize_dp(self, A):
        N = len(A)
        up, down, ans = [1]*N, [1]*N, 1
        for i in xrange(1, len(A)):
            if A[i] > A[i-1]:
                up[i] = down[i-1] + 1
            elif A[i] < A[i-1]:
                down[i] = up[i-1] + 1
            ans = max(ans, up[i], down[i])
        return ans

print(Solution().maxTurbulenceSize([1,1,1,1,1]))