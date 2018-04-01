class Solution:
    """
    @param grid: an integer matrix
    @return: an integer
    """
    def numIslandCities(self, grid):
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]

        ans = 0
        import collections
        q=collections.deque([])

        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j] == 2:
                    ans += 1
                    q.append((i,j))
                    while q:
                        x,y = q.popleft()
                        for dx, dy in dirs:
                            nx, ny = x+dx, y+dy
                            if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and grid[nx][ny] in [1,2]:
                                q.append((nx,ny))
                                grid[nx][ny] = 0
        return ans

print Solution().numIslandCities([
     [1,1,0,0,0],
     [0,1,0,0,1],
     [0,0,0,1,1],
     [0,0,0,0,0],
     [0,0,0,0,1]
])
print Solution().numIslandCities([
     [1,1,0,0,0],
     [0,1,0,0,1],
     [0,0,2,1,2],
     [0,0,0,0,0],
     [0,0,0,0,2]
])
