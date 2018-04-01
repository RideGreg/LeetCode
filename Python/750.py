class Solution(object):
    def countCornerRectangles(self, grid):
        # O(min(m, n) * (m+n))
        if len(grid) < 2 or len(grid[0]) < 2: return 0
        ans, ones = 0, []
        for r in grid:
            cur = [i for i, x in enumerate(r) if x == 1]
            if len(cur) > 1:
                curset = set(cur)
                for one in ones:
                    overlap = len(curset.intersection(one))
                    ans += overlap * (overlap-1) / 2
                ones.append(cur)
        return ans
        ''' This solution assumes we have to include the corner points.
        ans = 0
        if len(grid) < 2 or len(grid[0]) < 2: return 0

        row, col = len(grid), len(grid[0])
        if grid[0][0] == 1:
            for r in xrange(1, row):
                if grid[r][0] == 1:
                    for c in xrange(1, col):
                        if grid[0][c] == 1 and grid[r][c] == 1:
                            ans += 1
        if grid[row-1][0] == 1:
            for r in xrange(1, row-1):
                if grid[r][0] == 1:
                    for c in xrange(1, col):
                        if grid[row-1][c] == 1 and grid[r][c] == 1:
                            ans += 1
        if grid[0][col-1] == 1:
            for r in xrange(1, row):
                if grid[r][col-1] == 1:
                    for c in xrange(1, col-1):
                        if grid[0][c] == 1 and grid[r][c] == 1:
                            ans += 1
        if grid[row-1][col-1] == 1:
            for r in xrange(1, row-1):
                if grid[r][col-1] == 1:
                    for c in xrange(1, col-1):
                        if grid[row-1][c] == 1 and grid[r][c] == 1:
                            ans += 1
        return ans'''

print Solution().countCornerRectangles([[1, 0, 0, 1, 0],
 [0, 0, 1, 0, 1],
 [0, 0, 0, 1, 0],
 [1, 0, 1, 0, 1]])
print Solution().countCornerRectangles([[1, 1, 1],
 [1, 1, 1],
 [1, 1, 1]])
print Solution().countCornerRectangles([[1, 1, 1, 1]])
print Solution().countCornerRectangles([[0,1,0],[1,0,1],[1,0,1],[0,1,0]])