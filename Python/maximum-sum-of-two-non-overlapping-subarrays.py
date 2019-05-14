# Time:  O(n)
# Space: O(1)

# 1031
# Given an array A of non-negative integers, return the maximum sum of elements in two non-overlapping (contiguous) subarrays, which have lengths L and M.  (For clarification, the L-length subarray could occur before or after the M-length subarray.)
#
# Formally, return the largest V for which V = (A[i] + A[i+1] + ... + A[i+L-1]) + (A[j] + A[j+1] + ... + A[j+M-1]) and either:
#
# 0 <= i < i + L - 1 < j < j + M - 1 < A.length, or
# 0 <= j < j + M - 1 < i < i + L - 1 < A.length.

# Note: L + M <= A.length <= 1000, L>=1, M>=1
#
# Input: A = [0,6,5,2,2,5,1,9,4], L = 1, M = 2
# Output: 20
# Explanation: One choice of subarrays is [9] with length 1, and [6,5] with length 2.
#
# Input: A = [3,8,1,3,2,1,8,9,0], L = 3, M = 2
# Output: 29
# Explanation: One choice of subarrays is [3,8,1] with length 3, and [8,9] with length 2.
#
# Input: A = [2,1,5,6,0,9,5,0,3,8], L = 4, M = 3
# Output: 31
# Explanation: One choice of subarrays is [5,6,0,9] with length 4, and [3,8] with length 3.

class Solution(object):
    def maxSumTwoNoOverlap(self, A, L, M):  # 40 ms
        """
        :type A: List[int]
        :type L: int
        :type M: int
        :rtype: int
        """
        for i in range(1, len(A)):
            A[i] += A[i-1]
        result, Lmax, Mmax = A[L+M-1], A[L-1], A[M-1]
        for i in range(L+M, len(A)):
            Lsum = A[i] - A[i-L]    # sum of the last L elements
            Msum = A[i] - A[i-M]    # sum of the last M elements
            Lmax = max(Lmax, A[i-M] - A[i-M-L]) # max sum of contiguous L elements before the last M elements
            Mmax = max(Mmax, A[i-L] - A[i-L-M]) # max sum of contiguous M elements before the last L elements
            result = max(result, Lmax + Msum, Mmax + Lsum)
        return result

    # Time O(n^2), 1200 ms
    def maxSumTwoNoOverlap_2loop(self, A, L, M):
        N = len(A)
        prefix = [0]
        for a in A:
            prefix.append(prefix[-1] + a)

        ans = 0
        for i in range(N):
            for j in range(N):
                if i+L<=N and j+M<=N and (i+L<=j or j+M<=i):
                    ans = max(ans, prefix[i+L]-prefix[i]+prefix[j+M]-prefix[j])
        return ans

print(Solution().maxSumTwoNoOverlap([3,8,1,3,2,1,8,9,0], 3, 2)) # 29