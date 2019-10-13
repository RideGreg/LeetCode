# Time:  O(m * n)
# Space: O(m * n)

# 361
# Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum
# enemies you can kill using one bomb.
# The bomb kills all the enemies in the same row and column from the planted point until it hits the wall
# since the wall is too strong to be destroyed.
# Note: You can only put the bomb at an empty cell.

try:
    xrange          # Python 2
except NameError:
    xrange = range  # Python 3


# 直接的遍历。row里存的是当前横向能杀的敌人个数，cols[j]存的是在col j杀伤的敌人个数
# 只有在前一位是'W'的时候，才会重启设置能杀伤多少敌人
class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        ans = 0
        if not grid or not grid[0]:
            return ans

        m, n = len(grid), len(grid[0])
        row, cols = 0, [0]*n
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'W':
                    continue

                # first column (each new row or after 'W'), count how many E cell in the row segment
                if j == 0 or grid[i][j-1] == 'W':
                    row, jj = 0, j
                    while jj < n and grid[i][jj] != 'W':
                        if grid[i][jj] == 'E':
                            row += 1
                        jj += 1

                # first row (new row or after 'W'), count how many E cell in the col segment
                if i == 0 or grid[i-1][j] == 'W':
                    cols[j], ii = 0, i
                    while ii < m and grid[ii][j] != 'W':
                        if grid[ii][j] == 'E':
                            cols[j] += 1
                        ii += 1

                if grid[i][j] == '0':
                    ans = max(ans, row + cols[j])
        return ans


    def maxKilledEnemies_kamyu(self, grid):
        result = 0
        if not grid or not grid[0]:
            return result
        
        m, n = len(grid), len(grid[0])

        down = [[0]*n for _ in xrange(m)]
        right = [[0]*n for _ in xrange(m)]
        for i in reversed(xrange(m)):
            for j in reversed(xrange(n)):
                if grid[i][j] != 'W':
                    if i < m-1:
                        down[i][j] = down[i + 1][j]
                    if j < n-1:
                        right[i][j] = right[i][j + 1]
                    if grid[i][j] == 'E':
                        down[i][j] += 1
                        right[i][j] += 1

        up = [0 for _ in xrange(n)]
        for i in xrange(m):
            left = 0
            for j in xrange(n):
                if grid[i][j] == 'W':
                    up[j], left = 0, 0
                elif grid[i][j] == 'E':
                    up[j] += 1
                    left += 1
                else:
                    result = max(result, left + up[j] + right[i][j] + down[i][j])

        return result

print(Solution().maxKilledEnemies([["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]])) # 3
#down = [[1, 2, 0, 1],
#        [1, 1, 0, 1],
#        [0, 1, 0, 0]]
#right = [[1, 1, 0, 0],
#         [1, 0, 0, 1],
#         [1, 1, 0, 0]]