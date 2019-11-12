# Time:  O(N * m * n)
# Space: O(m * n)

# 576
# There is an m by n grid with a ball. Given the start coordinate (i,j) of the ball,
# you can move the ball to adjacent cell or cross the grid boundary in
# four directions (up, down, left, right). However, you can at most move N times.
# Find out the number of paths to move the ball out of grid boundary.
# The answer may be very large, return it after mod 109 + 7.
#
# Example 1:
# Input:m = 2, n = 2, N = 2, i = 0, j = 0
# Output: 6
#
# Example 2:
# Input:m = 1, n = 3, N = 3, i = 0, j = 1
# Output: 12
#
# Note:
# Once you move the ball out of boundary, you cannot move it back.
# The length and height of the grid is in range [1,50].
# N is in range [0,50].

# DP: 必须记住移动后的坐标，因为向外移和向内移的后续结果不一样。因为坐标总数是有限的，考虑所有坐标即可。
#
# 数组dp[t][x][y]表示第t次移动时，坐标x, y处的移动路径总数。
# 状态转移方程：
# dp[t + 1][x + dx][y + dy] += dp[t][x][y]    其中t表示移动的次数，dx, dy 取值 (1,0), (-1,0), (0,1), (0,-1)
#
# 当x + dx或者y + dy超出边界时，将结果累加至最终答案。

class Solution(object):
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        import collections
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        dmap = {(i,j): 1}
        ans, MOD = 0, 10**9+7
        for _ in range(N):
            ndmap = collections.defaultdict(int)
            for (x,y), cnt in dmap.items():
                for dx,dy in dirs:
                    nx, ny = x+dx, y+dy
                    if 0<=nx<m and 0<=ny<n:
                        ndmap[nx,ny] += cnt
                    else:
                        ans = (ans+cnt) % MOD
            dmap = ndmap
        return ans

        ''' same algorithm as the above, but use full 2D array vs. dict with reachable cells only
        M = 10**9 + 7
        dirs = [(-1,0), (1,0), (0,-1), (0,1)]
        dp = [[0]*n for _ in range(m)]
        dp[i][j] = 1
        ans = 0
        for _ in range(N):
            ndp = [[0]*n for _ in range(m)]
            for x in range(m):
                for y in range(n):
                    if dp[x][y]:
                        for dx, dy in dirs:
                            nx, ny = x+dx, y+dy
                            if 0<=nx<m and 0<=ny<n:
                                ndp[nx][ny] = (ndp[nx][ny] + dp[x][y]) % M
                            else:
                                ans = (ans + dp[x][y]) % M
            dp = ndp
        return ans % M'''

    def findPaths_kamyu(self, m, n, N, x, y):
        """
        :type m: int
        :type n: int
        :type N: int
        :type x: int
        :type y: int
        :rtype: int
        """
        M = 1000000000 + 7
        dp = [[[0 for _ in xrange(n)] for _ in xrange(m)] for _ in xrange(2)]
        for moves in xrange(N):
            for i in xrange(m):
                for j in xrange(n):
                    dp[(moves + 1) % 2][i][j] = (((1 if (i == 0) else dp[moves % 2][i - 1][j]) + \
                                                  (1 if (i == m - 1) else dp[moves % 2][i + 1][j])) % M + \
                                                 ((1 if (j == 0) else dp[moves % 2][i][j - 1]) + \
                                                  (1 if (j == n - 1) else dp[moves % 2][i][j + 1])) % M) % M
        return dp[N % 2][x][y]

print(Solution().findPaths(1,3,3,0,1))