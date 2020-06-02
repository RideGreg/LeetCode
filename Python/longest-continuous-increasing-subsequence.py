# Time:  O(n)
# Space: O(1)

# 674
# Given an unsorted array of integers,
# find the length of longest continuous increasing subsequence.
#
# Example 1:
# Input: [1,3,5,4,7]
# Output: 3
# Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3.
# Even though [1,3,5,7] is also an increasing subsequence,
# it's not a continuous one where 5 and 7 are separated by 4.
# Example 2:
# Input: [2,2,2,2,2]
# Output: 1
# Explanation: The longest continuous increasing subsequence is [2], its length is 1.
# Note: Length of the array will not exceed 10,000.

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result, count = 0, 0
        for i in xrange(len(nums)):
            if i == 0 or nums[i-1] < nums[i]:
                count += 1
                result = max(result, count)
            else:
                count = 1
        return result

# Follow up: Give you an integer matrix (with row size n, column size m), find the longest increasing continuous subsequence in this matrix.
# (The definition of the longest increasing continuous subsequence here can start at any row or column and go up/down/right/left any direction).
#
# Given a matrix:
# [
# [1 ,2 ,3 ,4 ,5],
# [16,17,24,23,6],
# [15,18,25,22,7],
# [14,19,20,21,8],
# [13,12,11,10,9]
# ]
# return 25
'''
# If direction is limited, e.g. left to right in single sequence, we know the order of DP transfer function. But this question
# has undetermined directions, normal DP cannot solve this; must use dfs + memorization
# (LCIS, visited) for each position is recorded in dp[][]. 
# In dfs: if matrix[x][y] > matrix[nx][ny] means extending to smaller num (ie. current is the tail of sequence), 
# solving the smaller position FIRST as leaf, before use the value for larger position. 
# if matrix[x][y] < matrix[nx][ny] also ok, extending to larger nums (i.e. current is the head of sequence).
# Time complexity O(n*n) each position is visited once.
'''

class Solution2():
    def LCIS(self, matrix):
        def dfs(x, y):
            if dp[x][y][1]: return dp[x][y][0]
            ans = 1
            for dx, dy in dirs:
                nx, ny = x+dx, y+dy
                if 0<=nx<len(matrix) and 0<=ny<len(matrix[0]):
                    if matrix[x][y] > matrix[nx][ny]: # current as tail
                    # if matrix[x][y] < matrix[nx][ny]: # current as head, both ok
                        ans = max(ans, dfs(nx, ny)+1)

            dp[x][y] = (ans, 1)
            return ans

        if not matrix: return 0
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m, n, ans = len(matrix), len(matrix[0]), 1
        dp = [[(1, 0)]*n for _ in range(m)] # (LCIS, visited) OR use a standalone 'visited' 2d array
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))
        return ans

print(Solution2().LCIS([
    [1,2,3],
    [8,9,4],
    [7,6,5]
]))
