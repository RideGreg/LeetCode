# Time:  O(max(m, n)^2)
# Space: O(1)

# 885
# On a 2 dimensional grid with R rows and C columns,
# we start at (r0, c0) facing east.
#
# Here, the north-west corner of the grid is at the first row and column,
# and the south-east corner of the grid is at the last row and column.
#
# Now, we walk in a clockwise spiral shape to visit every position in this grid. 
#
# Whenever we would move outside the boundary of the grid,
# we continue our walk outside the grid (but may return to the grid boundary later.) 
#
# Eventually, we reach all R * C spaces of the grid.
#
# Return a list of coordinates representing the positions of the grid
# in the order they were visited.
#
# Example 1:
#
# Input: R = 1, C = 4, r0 = 0, c0 = 0
# Output: [[0,0],[0,1],[0,2],[0,3]]
#
# Example 2:
#
# Input: R = 5, C = 6, r0 = 1, c0 = 4
# Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],
#          [0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],
#          [4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],
#          [0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]
#
# Note:
# - 1 <= R <= 100
# - 1 <= C <= 100
# - 0 <= r0 < R
# - 0 <= c0 < C

class Solution(object):
    def spiralMatrixIII(self, R, C, r0, c0): # Ming, USE THIS
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ans = [[r0, c0]]
        n, steps = 0, 1
        while len(ans) < R * C:
            for _ in (0, 1):
                dr, dc = dirs[n % 4]
                for _ in xrange(steps):
                    nr, nc = r0 + dr, c0 + dc
                    if 0 <= nr < R and 0 <= nc < C:
                        ans.append([nr, nc])
                    r0, c0 = nr, nc
                n += 1 # change direction
            steps += 1
        return ans

    def spiralMatrixIII_generator(self, R, C, r0, c0):
        def get_next(r, c):
            n = 0
            while True:
                dx, dy = [(0, 1), (1, 0), (0, -1), (-1, 0)][n % 4]
                steps = n / 2 + 1
                for _ in xrange(steps):
                    yield r + dx, c + dy
                    r, c = r + dx, c + dy
                n += 1

        ans = [[r0, c0]]
        for nx, ny in get_next(r0, c0):
            if len(ans) == R * C:
                return ans
            if 0 <= nx < R and 0 <= ny < C:
                ans.append([nx, ny])

    def spiralMatrixIII2_kamyu(self, R, C, r0, c0):
        r, c = r0, c0
        result = [[r, c]]
        x, y, n, i = 0, 1, 0, 0
        while len(result) < R*C:
            r, c, i = r+x, c+y, i+1
            if 0 <= r < R and 0 <= c < C:
                result.append([r, c])
            if i == n//2+1:
                x, y, n, i = y, -x, n+1, 0
        return result


print(Solution().spiralMatrixIII(1,1,0,0)) # [[0,0]]
print(Solution().spiralMatrixIII(1,4,0,0)) # [[0,0],[0,1],[0,2],[0,3]]

