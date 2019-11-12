# Time:  O(n * m^2), n is the number of rows with 1s, m is the number of cols with 1s
# Space: O(n * m)

# 750
# Given a grid where each entry is only 0 or 1, find the number of corner rectangles.
#
# A corner rectangle is 4 distinct 1s on the grid that form an axis-aligned rectangle.
# Note that only the corners need to have the value 1. Also, all four 1s used must be distinct.
#
# Example 1:
# Input: grid =
# [[1, 0, 0, 1, 0],
#  [0, 0, 1, 0, 1],
#  [0, 0, 0, 1, 0],
#  [1, 0, 1, 0, 1]]
# Output: 1
# Explanation: There is only one corner rectangle, with corners grid[1][2], grid[1][4], grid[3][2], grid[3][4].
#
# Example 2:
# Input: grid =
# [[1, 1, 1],
#  [1, 1, 1],
#  [1, 1, 1]]
# Output: 9
# Explanation: There are four 2x2 rectangles, four 2x3 and 3x2 rectangles, and one 3x3 rectangle.
#
# Example 3:
# Input: grid =
# [[1, 1, 1, 1]]
# Output: 0
# Explanation: Rectangles must have four distinct corners.
# Note:
# - The number of rows and columns of grid will each be in the range [1, 200].
# - Each grid[i][j] will be either 0 or 1.
# - The number of 1s in the grid will be at most 6000.

class Solution(object):
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # get effective cols in each row
        rows = [[c for c, val in enumerate(row) if val]
                for row in grid]
        result = 0
        for i in range(len(rows)):
            lookup = set(rows[i])
            for j in range(i):
                count = sum(1 for c in rows[j] if c in lookup)
                result += count*(count-1)//2
        return result

    ''' bookshadow 没有事先去除非1列的优化
    枚举起始行x，终止行y：
        遍历各列z，统计满足grid[x][z] == 1并且grid[y][z] == 1条件的列数，记为cnt
        根据组合公式，C(cnt, 2) = cnt * (cnt - 1) / 2，累加至答案。
    
    class Solution {
    public int countCornerRectangles(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int ans = 0;
        for (int x = 0; x < m; x++) {
            for (int y = x + 1; y < m; y++) {
                int cnt = 0;
                for (int z = 0; z < n; z++) {
                    if (grid[x][z] == 1 && grid[y][z] == 1) {
                        cnt++;
                    }
                }
                ans += cnt * (cnt - 1) / 2;
            }
        }
        return ans;
    }
    }
    '''


    # O(len(grid)*len(grid[0]))
    def countCornerRectangles_ming(self, grid):
        m, n, ans = len(grid), len(grid[0]), 0
        if m == 1 or n == 1: return ans
        # traverse all internal points
        for i in range(1, m-1):
            for j in range(1, n-1):
                if grid[0][0]:
                    ans += (grid[0][j] and grid[i][0])
                if grid[0][n-1]:
                    ans += (grid[0][j] and grid[i][n-1])
                if grid[m-1][0]:
                    ans += (grid[m-1][j] and grid[i][0])
                if grid[m-1][n-1]:
                    ans += (grid[m-1][j] and grid[i][n-1])
            # traverse point pairs on left and right cols
            if grid[0][0] and grid[0][n-1]:
                ans += (grid[i][0] and grid[i][n-1])
            if grid[m-1][0] and grid[m-1][n-1]:
                ans += (grid[i][0] and grid[i][n-1])
        # traverse point pairs on top and bottom rows
        for j in range(1, n-1):
            if grid[0][0] and grid[m-1][0]:
                ans += (grid[0][j] and grid[m-1][j])
            if grid[0][n-1] and grid[m-1][n-1]:
                ans += (grid[0][j] and grid[m-1][j])
        return ans + (grid[0][0] and grid[m-1][0] and grid[0][n-1] and grid[m-1][n-1])


print(Solution().countCornerRectangles([
 [1, 0, 0, 1, 0],
 [0, 0, 1, 0, 1],
 [0, 0, 0, 1, 0],
 [1, 0, 1, 0, 1]])) # 1
print(Solution().countCornerRectangles([
 [1, 1, 1],
 [1, 1, 1],
 [1, 1, 1]])) # 9
print(Solution().countCornerRectangles([[1,1,1,1]])) # 0
