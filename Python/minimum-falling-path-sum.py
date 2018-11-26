# Time:  O(n^2)
# Space: O(1)

# 931 contest 108 10/27/2018
#Given a square array of integers A, we want the minimum sum of a falling path through A.

#A falling path starts at any element in the first row, and chooses one element from each row.  
#The next row's choice must be in a column that is different from the previous row's column by at most one.

#Example 1:
#Input: [[1,2,3],[4,5,6],[7,8,9]]
#Output: 12
#Explanation: 
#The possible falling paths are:
#[1,4,7], [1,4,8], [1,5,7], [1,5,8], [1,5,9]
#[2,4,7], [2,4,8], [2,5,7], [2,5,8], [2,5,9], [2,6,8], [2,6,9]
#[3,5,7], [3,5,8], [3,5,9], [3,6,8], [3,6,9]
#The falling path with the smallest sum is [1,4,7], so the answer is 12.

#Note:
#1 <= A.length == A[0].length <= 100
#-100 <= A[i][j] <= 100

class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        for i in xrange(1, len(A)):
            for j in xrange(len(A[i])):
                A[i][j] += min(A[i-1][max(j-1, 0):j+2])
        return min(A[-1])

    # if not allowing to overwrite input list
    def minFallingPathSum_auxSpace(self, A):
        n = len(A)
        dp = [A[0], [0]*n]
        for i in xrange(1, n):
            for j in xrange(n):
                start = max(j-1, 0)
                dp[i%2][j] = min(dp[(i-1)%2][start:j+2]) + A[i][j]
        return min(dp[(n-1)%2])

print(Solution().minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]])) # 12
