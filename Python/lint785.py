class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        sum = list(grid[0])
        for j in reversed(xrange(0, len(grid[0])-1)):
            sum[j] = sum[j + 1] + grid[0][j]

        for i in xrange(1, len(grid)):
            sum[-1] += grid[i][-1]
            for j in reversed(xrange(0, len(grid[0])-1)):
                sum[j] = max(sum[j + 1], sum[j]) + grid[i][j]

        return sum[0]
print Solution().minPathSum([
[1,2,3,4],
[3,5,6,7],
[9,10,1,2],
[4,4,5,5]
])
print Solution().minPathSum([
[1,2,3],
[4,5,6],
[7,9,8]
])