# Time:  O(n^2)
# Space: O(n^2)

# 1027
# Given an array A of integers, return the length of the longest arithmetic subsequence in A.
#
# Recall that a subsequence of A is a list A[i_1], A[i_2], ..., A[i_k] with 0 <= i_1 < i_2
# < ... < i_k <= A.length - 1, and that a sequence B is arithmetic if B[i+1] - B[i] are
# all the same value (for 0 <= i < B.length - 1).

# 2 <= A.length <= 2000
# 0 <= A[i] <= 10000


# Input: [20,1,15,3,10,5,8]
# Output: 4
# Explanation:
# The longest arithmetic subsequence is [20,15,10,5].

# https://aonecode.com/getArticle/204
# https://www.geeksforgeeks.org/longest-arithmetic-progression-dp-35/

import collections

class Solution(object):
    def longestArithSeqLength(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # usually dp is list of int, here dp is list of dict -> we can use ONE dict with 2d key instead
        # collections.defaultdict(int) only difference is default to 0
        ans = 1
        dp = collections.defaultdict(lambda: 1)
        for i in range(1, len(A)):
            for j in range(i):
                d = A[i]-A[j]
                dp[i,d] = dp[j,d] + 1
                ans = max(ans, dp[i,d])
        return ans

    # The solution 2d DP only works if input A is sorted.
    # https://www.geeksforgeeks.org/longest-arithmetic-progression-dp-35/
    def longestArithSeqLength_2(self, A):
        n = len(A)
        if (n <= 2):
            return n
        L = [[0] * n for _ in xrange(n)] # L[i][j] stores LLAS (Length of Longest Arithmetic Seq) from [A[i]..A[j]]
        llap = 2  # Initialize the result

        for i in xrange(n):
            L[i][n - 1] = 2

        for j in range(n - 2, 0, -1):
            i = j - 1
            k = j + 1
            while i >= 0 and k <= n - 1:
                if A[i] + A[k] < 2 * A[j]:
                    k += 1
                elif A[i] + A[k] > 2 * A[j]:
                    L[i][j] = 2
                    i -= 1
                else:
                    L[i][j] = L[j][k] + 1
                    llap = max(llap, L[i][j])
                    i -= 1
                    k += 1

            while i >= 0:
                L[i][j] = 2
                i -= 1
        return llap

print(Solution().longestArithSeqLength([83,20,17,43,52,78,68,45])) # 2
print(Solution().longestArithSeqLength([3,6,9,12])) # 4
print(Solution().longestArithSeqLength([9,4,7,2,10])) # 3
print(Solution().longestArithSeqLength([20,1,15,3,10,5,8])) # 4
