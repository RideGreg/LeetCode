class Solution(object):
    def orderOfLargestPlusSign(self, N, mines):
        grid = [[1]*N for _ in xrange(N)]
        for m in mines:
            grid[m[0]][m[1]] = 0
        def isSign(r,c,k,grid):
            if any(grid[r][j]==0 for j in xrange(c-k+1, c+k)):
                return False
            if any(grid[i][c]==0 for i in xrange(r-k+1, r+k)):
                return False
            return True

        maxx = (N+1)/2
        for k in reversed(xrange(1, maxx+1)):
            for i in xrange(k-1, N-(k-1)):
                for j in xrange(k-1, N-(k-1)):
                    if isSign(i,j,k, grid):
                        return k
        return 0

print Solution().orderOfLargestPlusSign(5, [[4,2]])
print Solution().orderOfLargestPlusSign(2, [])
print Solution().orderOfLargestPlusSign(1, [[0,0]])