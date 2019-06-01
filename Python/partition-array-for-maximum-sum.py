# Time:  O(n * k)
# Space: O(k)

# 1043
# Given an integer array A, you partition the array into (contiguous) subarrays of length at most K.
# After partitioning, each subarray has their values changed to become the maximum value of that subarray.
#
# Return the largest sum of the given array after partitioning.

# Solution:
# dp[i] record the maximum sum we can get considering A[0] ~ A[i]
# To get dp[i], we will try to change k last numbers separately to the maximum of them,
# for k = 1..K.

class Solution(object):
    def maxSumAfterPartitioning(self, A, K): # USE THIS space O(n)
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        N = len(A)
        dp = [0]*N
        for i in range(N):
            mx = float('-inf')
            for l in range(1, K+1):
                if i+1 >= l:
                    mx = max(mx, A[i-l+1])
                    dp[i] = max(dp[i], (dp[i-l] if i>=l else 0) + l*mx)
        return dp[N-1]

    # best space complexity, reuse rolling spaces.
    def maxSumAfterPartitioning_kamyu(self, A, K):
        W = K+1
        dp = [0]*W
        for i in range(len(A)):
            curr_max = 0
            for k in range(1, min(K, i+1) + 1):
                curr_max = max(curr_max, A[i-k+1])
                dp[i % W] = max(dp[i % W], (dp[(i-k) % W] if i >= k else 0) + curr_max*k)
        return dp[(len(A)-1) % W]

    # negative indices are circular from the end of dp array, not easy to understand
    def maxSumAfterPartitioning_lee215(self, A, K):
        N = len(A)
        dp = [0] * (N + K)
        for i in range(N):
            curMax = 0
            for k in range(1, min(K, i + 1) + 1):
                curMax = max(curMax, A[i - k + 1])
                dp[i] = max(dp[i], dp[i - k] + curMax * k)
        return dp[N - 1]

    # TLE, DP: start with shorter sequence; result for longer sequence can always be obtained from 2 sub-sequence
    # O(n^3)
    def maxSumAfterPartitioning_ming(self, A: List[int], K: int) -> int:
        N = len(A)
        dp = [[0] * N for _ in range(N)]
        mx = [[0] * N for _ in range(N)]
        for i in range(N):
            mx[i][i] = A[i]
            for j in range(i + 1, N):
                mx[i][j] = max(mx[i][j - 1], A[j])

        for l in range(1, N + 1):
            for i in range(N - l + 1):
                j = i + l - 1
                if l <= K:
                    dp[i][j] = l * mx[i][j]
                else:
                    for k in range(i, j):
                        dp[i][j] = max(dp[i][j], dp[i][k] + dp[k + 1][j])

        return dp[0][-1]

print(Solution().maxSumAfterPartitioning([1,15,7,9,2,5,10], 3)) # 84, A becomes [15,15,15,9,10,10,10]
