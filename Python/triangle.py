# Time:  O(m * n)
# Space: O(n)
#
# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
#
# For example, given the following triangle
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
#
# Note:
# Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
#

class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal_bottomup(self, triangle): # USE THIS
        if not triangle:
            return 0
        dp = triangle[-1]
        for i in reversed(xrange(len(triangle)-1)):
            for j in xrange(i+1):
                dp[j] = triangle[i][j] + min(dp[j], dp[j+1])
        return dp[0]

    # Top Down
    def minimumTotal(self, triangle):
        if not triangle:
            return 0

        n = len(triangle)
        dp = [0]*n
        dp[0] = triangle[0][0]
        for i in xrange(1, n):
            dp[i] = dp[i-1] + triangle[i][i]
            for j in reversed(xrange(1, i)):
                dp[j] = min(dp[j], dp[j-1]) + triangle[i][j]
            dp[0] += triangle[i][0]
        return min(dp)
        '''
        cur = triangle[0] + [float("inf")]
        for i in xrange(1, len(triangle)):
            next = []
            next.append(triangle[i][0] + cur[0])
            for j in xrange(1, i + 1):
                next.append(triangle[i][j] + min(cur[j - 1], cur[j]))
            cur = next + [float("inf")]

        return reduce(min, cur)
        '''

if __name__ == "__main__":
    print Solution().minimumTotal_ming([[-1], [2, 3], [1, -1, -3]]) # -1
    print Solution().minimumTotal_ming([[2], [3,4], [6,5,7], [4,1,8,3]]) # 11

