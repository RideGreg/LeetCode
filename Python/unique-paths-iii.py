# Time:  O(m * n * 2^(m * n))
# Space: O(m * n * 2^(m * n))

# 980
# On a 2-dimensional grid, there are 4 types of squares:
#
# 1 represents the starting square.  There is exactly one starting square.
# 2 represents the ending square.  There is exactly one ending square.
# 0 represents empty squares we can walk over.
# -1 represents obstacles that we cannot walk over.

# Return the number of 4-directional walks from the starting square to the ending square,
# that walk over every non-obstacle square exactly once.

class Solution(object):
    # DFS backtracking: Time O(4^(R*C)), Space O(1)
    #
    # walking to each 0, change to an obstacle for each that we walked. After, we can revert the obstacle back.
    # Given the input limits, this can work because bad paths tend to get stuck quickly
    # and run out of free squares.
    def uniquePathsIII(self, grid): # USE THIS: my dfs
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(i,j, cnt):
            if grid[i][j] == 2:
                if cnt == 0:
                    self.ans += 1
                return

            for dx, dy in dirs:
                nx, ny = i+dx, j+dy
                if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and grid[nx][ny] in (0,2):
                    if grid[nx][ny] == 0:
                        grid[nx][ny] = -1 # similar to 'used' array
                    dfs(nx, ny, cnt-1)
                    if grid[nx][ny] == -1:
                        grid[nx][ny] = 0

        dirs = [(-1,0), (1,0), (0,-1), (0,1)]
        self.ans, cnt = 0, 0
        startx, starty = None, None

        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j] in (0, 2):
                    cnt += 1
                elif grid[i][j] == 1:
                    startx, starty = i, j

        dfs(startx, starty, cnt)
        return self.ans

    # Dynamic Programming
    # Let dp(r, c, todo) be the # of paths starting from where we are (r, c), and given
    # that todo is the set of empty squares we've yet to walk on.
    # Memoize these states (r, c, todo) so as not to repeat work.

    def uniquePathsIII_dp(self, grid):
        R, C = len(grid), len(grid[0])

        def index(r, c):
            return 1 << (r*C + c)

        def neighbors(r, c):
            for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] in (0, 2):
                    yield nr, nc

        def dp(src, todo):
            if src == dst:
                return int(todo == 0)
            key = (src, todo)
            if key in lookup:
                return lookup[key]

            result = 0
            for nr, nc in neighbors(src[0], src[1]):
                if todo & index(nr, nc):
                    result += dp((nr, nc), todo ^ index(nr, nc))

            lookup[key] = result
            return lookup[key]

        todo, src, dst, lookup = 0, None, None, {}
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val % 2 == 0:
                    todo |= index(r, c)

                if val == 1:
                    src = (r, c)
                elif val == 2:
                    dst = (r, c)
        return dp(src, todo)


    def uniquePathsIII_dfs_usedArray(self, grid): # more space required
        def dfs(i,j, cnt):
            if grid[i][j] == 2:
                if cnt == 0:
                    self.ans += 1
                return

            for dx, dy in dirs:
                nx, ny = i+dx, j+dy
                if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and grid[nx][ny] in (0,2) and not used[nx][ny]:
                    used[nx][ny] = True
                    dfs(nx, ny, cnt-1)
                    used[nx][ny] = False

        dirs = [(-1,0), (1,0), (0,-1), (0,1)]
        self.ans, cnt = 0, 0
        startx, starty = None, None
        used = [[False]*len(grid[0]) for _ in xrange(len(grid))]

        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j] in (0, 2):
                    cnt += 1
                elif grid[i][j] == 1:
                    startx, starty = i, j
                    used[startx][starty] = True

        dfs(startx, starty, cnt)
        return self.ans

print(Solution().uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]])) # 2