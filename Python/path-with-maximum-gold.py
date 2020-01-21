# Time:  O(m^2 * n^2)
# Space: O(m * n)

# 1219 weekly contest 157 10/5/2019

# In a gold mine grid of size m * n, each cell has an integer representing the amount of gold in that cell, 0 if it is empty.
#
# Return the maximum amount of gold you can collect under the conditions:
#
# - Every time you are located in a cell you will collect all the gold in that cell.
# - From your position you can walk one step to the left, right, up or down.
# - You can't visit the same cell more than once.
# - Never visit a cell with 0 gold.
# - You can start and stop collecting gold from any position in the grid that has some gold.

# 1 <= grid.length, grid[i].length <= 15
# 0 <= grid[i][j] <= 100
# There are at most 25 cells containing gold.

class Solution(object):
    def getMaximumGold(self, grid): # USE THIS: dfs uses 'cur' value as param
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dirs = [(-1,0),(1,0),(0,-1), (0,1)]
        m, n = len(grid), len(grid[0])

        def dfs(x, y, cur):
            ans[0] = max(ans[0], cur)

            grid[x][y] *= -1  # better than maintain a 'used' matrix
            for dx, dy in dirs:
                nx, ny = x+dx, y+dy
                if 0<=nx<m and 0<=ny<n and grid[nx][ny] > 0:
                    dfs(nx, ny, cur+grid[nx][ny])
            grid[x][y] *= -1

        ans = [0]
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    dfs(i, j, grid[i][j])
        return ans[0]


    # use return value
    def getMaximumGold_kamyu(self, grid):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def backtracking(i, j):
            result = 0
            grid[i][j] *= -1
            for dx, dy in directions:
                ni, nj = i+dx, j+dy
                if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] > 0:
                    result = max(result, backtracking(ni, nj)) # 四条子路径中最大一条
            grid[i][j] *= -1
            return grid[i][j] + result

        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    ans = max(ans, backtracking(i, j))
        return ans

print(Solution().getMaximumGold([[0,6,0],[5,8,7],[0,9,0]])) # 24: 9 -> 8 -> 7.
print(Solution().getMaximumGold([[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]])) # 28: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.
print(Solution().getMaximumGold([
    [0, 0,34,0, 5, 0,7,0, 0,0],
    [0, 0, 0,0,21, 0,0,0, 0,0],
    [0,18, 0,0, 8, 0,0,0, 4,0],
    [0, 0, 0,0, 0, 0,0,0, 0,0],
    [15,0, 0,0, 0,22,0,0, 0,21],
    [0, 0, 0,0, 0, 0,0,0, 0,0],
    [0, 7, 0,0, 0, 0,0,0,38,0]])) # 38