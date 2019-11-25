# Time:  O(k * n^2)
# Space: O(n)

# 813
# We partition a row of numbers A into at most K adjacent (non-empty) groups,
# then our score is the sum of the average of each group. What is the largest
# score we can achieve?
#
# Note that our partition must use every number in A, and that scores are not
# necessarily integers.
#
# Example:
# Input:
# A = [9,1,2,3,9]
# K = 3
# Output: 20
# Explanation:
# The best choice is to partition A into [9], [1, 2, 3], [9]. The answer is
# 39 + (1 + 2 + 3) / 3 + 9 = 20.
# We could have also partitioned A into [9, 1], [2], [3, 9], for example.
# That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.
#
# Note:
# - 1 <= A.length <= 100.
# - 1 <= A[i] <= 10000.
# - 1 <= K <= A.length.
# Answers within 10^-6 of the correct answer will be accepted as correct.



# DP: dp[x][y]表示将数组的前y个元素至多分成x个子数组的最优解
# dp[x][y] = max(dp[x][y], dp[x - 1][z] + avg(z..y))
# where 0 <= x < K,  x <= y < N, x <= z < y

try:
    xrange          # Python 2
except NameError:
    xrange = range  # Python 3

from typing import List
class Solution(object):
    def largestSumOfAverages(self, A: List[int], K: int) -> float: # USE THIS, clearer
        psum = [0]
        for a in A:
            psum.append(psum[-1]+a)

        N = len(A)
        dp = [0] + [psum[i]/i for i in range(1, N+1)] # all in 1 group
        ans = dp[-1]
        for x in range(2, K+1): # 2..k groups
            ndp = [0]*(N+1)
            for y in range(x, N+1):
                for z in range(x-1, y): # prev x-1 groups have at least x-1 numbers
                    ndp[y] = max(ndp[y], dp[z] + (psum[y]-psum[z])/(y-z))
            dp = ndp
            ans = max(ans, dp[-1])
        return ans


    def largestSumOfAverages_kamyu(self, A, K):
        accum_sum = [A[0]]
        for i in xrange(1, len(A)):
            accum_sum.append(A[i]+accum_sum[-1])

        dp = [[0]*len(A) for _ in xrange(2)]
        for k in xrange(1, K+1):
            for i in xrange(k-1, len(A)):
                if k == 1:
                    dp[k % 2][i] = float(accum_sum[i])/(i+1)
                else:
                    for j in xrange(k-2, i):
                        dp[k % 2][i] = \
                            max(dp[k % 2][i],
                                dp[(k-1) % 2][j] +
                                float(accum_sum[i]-accum_sum[j])/(i-j))
        return dp[K % 2][-1]

print(Solution().largestSumOfAverages([9,1,2,3,9], 3)) # 20
