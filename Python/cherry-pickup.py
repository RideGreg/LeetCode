# Time:  O(n^3)
# Space: O(n^2)

# 741 Uber
# In a N x N grid representing a field of cherries, each cell is one of three possible integers.
#
# 0 means the cell is empty, so you can pass through;
# 1 means the cell contains a cherry, that you can pick up and pass through;
# -1 means the cell contains a thorn that blocks your way.
# Your task is to collect maximum number of cherries possible by following the rules below:
#
# Starting at the position (0, 0) and reaching (N-1, N-1) by moving right
# or down through valid path cells (cells with value 0 or 1);
#
# After reaching (N-1, N-1), returning to (0, 0) by moving left or up through valid path cells;
# When passing through a path cell containing a cherry, you pick it up and the cell becomes an empty cell (0);
# If there is no valid path between (0, 0) and (N-1, N-1), then no cherries can be collected.
# Example 1:
# Input: grid =
# [[0, 1, -1],
#  [1, 0, -1],
#  [1, 1,  1]]
# Output: 5
# Explanation:
# The player started at (0, 0) and went down, down, right right to reach (2, 2).
# 4 cherries were picked up during this single trip, and the matrix becomes [[0,1,-1],[0,0,-1],[0,0,0]].
# Then, the player went left, up, up, left to return home, picking up one more cherry.
# The total number of cherries picked up is 5, and this is the maximum possible.
#
# Note:
# - grid is an N by N 2D array, with 1 <= N <= 50.
# - Each grid[i][j] is an integer in the set {-1, 0, 1}.
# - It is guaranteed that grid[0][0] and grid[N-1][N-1] are not -1.

# DP: Instead of walking from end to beginning, let's reverse the second leg of the path, so we are only considering two paths from the beginning to the end.
#
# Notice after t steps, each position (r, c) we could be, is on the line r + c = t. So if we have two people at positions
# (r1, c1) and (r2, c2), then r2 = r1 + c1 - c2. That means the variables r1, c1, c2 uniquely determine 2 people who
# have walked the same r1 + c1 number of steps. This sets us up for dynamic programming quite nicely.
#
# Algorithm
#
# Say r1 + c1 = t is the t-th layer. Since our recursion only references the next layer, we only need to keep two layers
# in memory at a time. Or 1 layer is enough if we reverse traverse the array.
#
# At time t, let dp[c1][c2] be the most cherries that we can pick up for two people going from (0, 0) to (r1, c1) and
# (0, 0) to (r2, c2), where r1 = t-c1, r2 = t-c2. Our dynamic program:
#
# If grid[r1][c1] and grid[r2][c2] are not thorns, then the value is (grid[r1][c1] + grid[r2][c2]),
# We should also be careful to not double count in case (r1, c1) == (r2, c2).
# plus the maximum of dp[r1+1][c1][c2], dp[r1][c1+1][c2], dp[r1+1][c1][c2+1], dp[r1][c1+1][c2+1] as appropriate.
#
# Why did we say it was the maximum of dp[r+1][c1][c2] etc.? It corresponds to the 4 possibilities for person 1 and 2
# moving down and right:
#
# Person 1 down and person 2 down: dp[r1+1][c1][c2]; also r2->r2+1
# Person 1 right and person 2 down: dp[r1][c1+1][c2]; also r2->r2+1
# Person 1 down and person 2 right: dp[r1+1][c1][c2+1]; also r2->r2
# Person 1 right and person 2 right: dp[r1][c1+1][c2+1]; also r2->r2
#
# Algorithm
#
class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # dp holds the max # of cherries two k-length paths can pickup.
        # The two k-length paths arrive at (i, k - i) and (j, k - j),
        # respectively.
        n = len(grid)
        dp = [[-1 for _ in range(n)] for _ in range(n)]
        dp[0][0] = grid[0][0]
        max_len = 2 * (n-1)
        directions = [(0, 0), (-1, 0), (0, -1), (-1, -1)]
        for k in range(1, max_len+1):
            for i in reversed(range(max(0, k-n+1), min(k+1, n))):  # 0 <= i < n, 0 <= k-i < n
                for j in reversed(range(i, min(k+1, n))):          # i <= j < n, 0 <= k-j < n
                    # j < i no longer consider due to symmetry
                    if grid[i][k-i] == -1 or grid[j][k-j] == -1:
                        dp[i][j] = -1
                        continue
                    # cherries at current 2 girds
                    cnt = grid[i][k-i]
                    if i != j:
                        cnt += grid[j][k-j]

                    cand = [dp[ii][jj] + cnt
                            for ii in (i-1, i) for jj in (j-1, j)
                            if ii >= 0 and jj >= 0 and dp[ii][jj] >= 0]

                    dp[i][j] = max(cand + [-1])
                    '''
                    max_cnt = -1
                    for direction in directions:
                        ii, jj = i+direction[0], j+direction[1]
                        if ii >= 0 and jj >= 0 and dp[ii][jj] >= 0:
                            max_cnt = max(max_cnt, dp[ii][jj]+cnt)
                    dp[i][j] = max_cnt
                    '''
        return max(dp[n-1][n-1], 0)


    def cherryPickup_wrong1(self, grid): # record path along the way to calc dp
        n = len(grid)
        dp = [[float('-inf')] * n for _ in range(n)]
        dp[0][0] = grid[0][0]
        path = [[None] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if dp[i][j] == -1 or (i == 0 and j == 0): continue

                dp[i][j] = grid[i][j] + max(dp[i - 1][j] if i>0 else float('-inf'),
                                            dp[i][j - 1] if j>0 else float('-inf'))
                if dp[i][j] != float('-inf'):
                    if j == 0 or (i > 0 and dp[i - 1][j] >= dp[i][j - 1]):
                        path[i][j] = (i - 1, j)
                    else:
                        path[i][j] = (i, j - 1)

        if dp[n - 1][n - 1] <= 0: return 0
        r, c = n - 1, n - 1
        while path[r][c]:
            r, c = path[r][c]
            grid[r][c] = 0

        for i in reversed(range(n)):
            for j in reversed(range(n)):
                if dp[i][j] == -1 or (i == n - 1 and j == n - 1): continue

                dp[i][j] = grid[i][j] + max(dp[i + 1][j] if i<n-1 else float('-inf'),
                                            dp[i][j + 1] if j<n-1 else float('-inf'))
        return dp[0][0]

    def cherryPickup_wrong2(self, grid): # same algorithm, just don't use a matrix for prev (i,j) in path

        def bestpath(grid):
            N = len(grid)
            dp = [[float('-inf')] * N for _ in range(N)]
            dp[-1][-1] = grid[-1][-1]
            for i in range(N-1, -1, -1):
                for j in range(N-1, -1, -1):
                    if grid[i][j] >= 0 and (i != N-1 or j != N-1):
                        dp[i][j] = max(dp[i+1][j] if i+1 < N else float('-inf'),
                                       dp[i][j+1] if j+1 < N else float('-inf'))
                        dp[i][j] += grid[i][j]

            if dp[0][0] < 0: return None
            ans = [(0, 0)]
            i = j = 0
            while i != N-1 or j != N-1:
                if j+1 == N or (i+1 < N and dp[i+1][j] >= dp[i][j+1]):
                    i += 1
                else:
                    j += 1
                ans.append((i, j))
            return ans

        ans = 0
        path = bestpath(grid)
        if path is None: return 0

        for i, j in path:
            ans += grid[i][j]
            grid[i][j] = 0

        for i, j in bestpath(grid):
            ans += grid[i][j]

        return ans
print(Solution().cherryPickup([[1,1,1,0,0,0]
                              ,[0,0,1,0,0,0]
                              ,[0,0,1,0,0,1]
                              ,[1,0,1,0,0,0]
                              ,[0,0,1,0,0,0]
                              ,[0,0,1,1,0,1]])) # 12
print(Solution().cherryPickup([[0, 1, -1],
                               [1, 0, -1],
                               [1, 1,  1]])) # 5
print(Solution().cherryPickup([[1, 1, -1],
                               [1, -1, 1],
                               [-1, 1, 1]])) # 0