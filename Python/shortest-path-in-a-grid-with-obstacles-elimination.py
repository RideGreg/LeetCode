# Time:  O(m * n * k)
# Space: O(m * n)

# 1293 weekly contest 167 12/14/2019

# Given a m * n grid, where each cell is either 0 (empty) or 1 (obstacle). In one step, you can move up, down,
# left or right from and to an empty cell.
#
# Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m-1, n-1)
# given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.

# 1 <= m, n <= 40
# 1 <= k <= m*n
# grid[i][j] == 0 or 1
# grid[0][0] == grid[m-1][n-1] == 0


# A* Search Algorithm without heap
class Solution(object):
    def shortestPath(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def dot(a, b):
            return a[0]*b[0]+a[1]*b[1]

        def g(a, b):
            return abs(a[0]-b[0])+abs(a[1]-b[1])
        
        def a_star(grid, b, t, k):
            f, dh = g(b, t), 2
            closer, detour = [(b, k)], []
            lookup = {}
            while closer or detour:
                if not closer:
                    f += dh
                    closer, detour = detour, closer
                b, k = closer.pop()
                if b == t:
                    return f
                if b in lookup and lookup[b] >= k:
                    continue
                lookup[b] = k
                for dx, dy in directions:
                    nb = (b[0]+dx, b[1]+dy)
                    if not (0 <= nb[0] < len(grid) and 0 <= nb[1] < len(grid[0]) and
                            (grid[nb[0]][nb[1]] == 0 or k > 0) and
                            (nb not in lookup or lookup[nb] < k)):
                        continue
                    (closer if dot((dx, dy), (t[0]-b[0], t[1]-b[1])) > 0 else detour).append((nb, k-int(grid[nb[0]][nb[1]] == 1)))
            return -1

        return a_star(grid, (0, 0), (len(grid)-1, len(grid[0])-1), k)


    def shortestPath_ming(self, grid, k):
        import collections
        dirs = [(-1,0), (1,0), (0,-1), (0,1)]
        m, n = len(grid), len(grid[0])
        #print(m*n, k)
        dp = [[collections.defaultdict(lambda: float('inf') ) for _ in range(n)] for _ in range(m)]
        q = collections.deque([(0,0)])
        dp[0][0][0] = 0
        done = {(0,0)}
        while q:
            x,y = q.popleft()
            for dx, dy in dirs:
                nx, ny = x+dx, y+dy
                if 0<=nx<m and 0<=ny<n and (k<200 or (nx,ny) not in done):
                    done.add((nx,ny))
                    for ob, step in dp[x][y].items():
                        if step == float('inf'): continue
                        nob = ob + grid[nx][ny]
                        if nob <= k and step+1 < dp[nx][ny][nob]:
                            # check less obstacles
                            if any(dp[nx][ny][obob] < step+1 for obob in range(nob)):
                                continue

                            dp[nx][ny][nob] = step+1
                            q.append((nx,ny))
        res = min(dp[m-1][n-1][i] for i in range(k+1))
        return -1 if res == float('inf') else res

print(Solution().shortestPath([[0,0,0,1,0,1,0,0,0,1,0,1,1,1,1,0,0,0],[1,0,0,0,1,0,0,1,0,0,1,0,0,1,0,1,1,0],[1,0,0,1,1,1,0,0,0,1,1,0,0,1,1,1,0,1],[0,0,1,0,0,0,1,0,0,0,0,1,0,0,1,1,0,1],[1,1,0,0,0,0,0,0,0,0,1,1,0,0,1,1,1,1],[0,0,1,1,0,0,0,1,0,0,0,1,0,0,1,1,0,0],[0,0,0,0,0,1,1,0,1,0,0,1,1,1,1,1,0,0],[1,1,1,0,1,0,1,0,1,0,0,0,0,0,0,1,0,0],[0,0,1,1,0,0,1,0,0,1,1,1,1,1,0,0,1,0],[1,0,0,0,0,1,1,1,1,1,0,0,1,1,1,1,0,0],[0,0,1,1,1,0,0,0,1,1,0,1,0,1,1,1,1,0],[1,0,0,0,0,0,1,0,0,1,1,0,1,0,0,1,1,1],[0,0,1,0,1,0,0,0,1,1,0,0,1,0,1,0,0,0],[1,1,0,0,1,1,1,0,0,0,1,0,0,0,1,0,1,0],[1,0,1,1,1,1,0,1,0,1,0,1,0,0,0,0,0,0],[0,0,0,0,0,1,0,1,0,0,0,1,1,1,1,1,1,0],[0,0,1,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1],[0,1,1,1,0,0,0,1,1,0,0,0,1,0,1,0,0,0],[1,1,1,0,0,0,1,1,0,0,0,1,0,1,0,0,1,1],[0,0,1,1,1,1,0,1,0,0,1,1,0,1,1,1,1,0],[0,1,1,0,1,0,0,1,0,1,0,0,0,0,0,0,1,1],[1,1,0,0,1,0,0,1,0,1,1,1,0,0,0,1,0,1],[0,0,1,1,0,1,0,1,0,1,1,1,0,0,1,1,0,1],[0,1,0,0,0,0,1,0,1,0,1,0,1,1,1,0,1,0],[0,1,0,0,1,0,0,0,0,1,0,0,1,1,0,0,1,1],[0,1,1,1,1,1,0,1,1,1,0,1,0,0,0,1,0,0],[0,0,1,0,1,0,1,1,1,0,1,0,0,0,0,0,1,1],[0,0,0,1,1,0,0,1,1,0,0,0,0,1,0,0,1,0],[1,1,1,1,0,1,0,0,1,0,0,0,1,1,0,0,1,0],[0,1,0,1,0,1,0,0,0,1,0,0,1,0,1,0,1,0],[1,0,0,1,0,0,1,1,1,1,1,1,1,1,0,1,1,0],[1,1,1,1,1,0,1,0,1,1,1,0,0,0,1,0,0,1],[0,0,0,0,1,0,1,1,1,1,1,0,0,1,0,1,0,1],[1,0,0,1,0,0,1,0,0,0,1,1,0,0,0,0,1,0],[1,0,1,1,1,0,1,0,0,1,1,0,0,1,1,1,0,0],[1,1,1,1,1,1,0,0,0,0,0,1,0,0,1,1,1,0],[0,1,0,0,1,1,1,0,0,0,1,1,0,1,0,0,1,0],[1,0,1,1,0,0,0,0,0,1,1,1,0,0,1,1,1,1],[1,1,0,0,0,1,1,0,0,0,0,1,0,1,1,0,0,0],[0,1,1,1,0,1,1,0,1,1,1,1,0,1,1,1,0,0]],
                              696)) # 56
print(Solution().shortestPath([[0,0,0,1,0,1,1,1,1,1,1,1,1,1,0,0,0,1,1,0,1,1,1,1,0,1,1,0,1,1,1,0,0,0,1,1,1,1,0,1],[0,0,0,1,0,0,1,1,1,1,1,1,0,0,0,1,0,1,0,0,1,0,1,1,0,1,1,0,0,0,1,0,1,1,1,0,1,0,1,0],[0,0,0,0,1,0,1,1,0,0,1,0,0,1,1,1,0,0,0,1,0,1,1,0,0,1,0,0,1,1,0,1,0,1,0,1,0,1,0,1],[0,0,1,0,0,0,0,1,0,1,0,0,1,0,0,0,0,1,1,1,1,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,0,0],[0,1,0,1,0,0,0,1,1,0,1,0,0,1,0,0,0,1,0,1,0,0,0,0,1,1,1,0,1,1,1,0,1,1,0,1,0,1,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0,1,0,1,0,1,1,0,1,0,0,0,0,1,0,1,0,0,0,1,1,1,1,0,0,0,1,1],[1,1,0,0,1,0,0,1,0,1,1,0,0,0,1,0,1,1,0,0,1,0,0,1,1,1,0,0,0,0,1,0,1,1,1,1,0,1,1,0],[0,0,0,0,1,1,1,1,1,1,1,1,0,0,1,1,0,1,1,1,0,0,1,1,0,0,0,1,0,0,1,1,1,1,1,0,1,0,1,1],[0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1,1,1,0,0,0,1,1,0,1,0,1,0,0,1,0,0,1,0,1,1,0,0],[1,0,1,1,0,1,1,0,1,0,1,0,1,0,1,0,0,1,0,0,0,1,0,1,1,0,0,1,1,0,0,1,0,0,1,0,0,1,0,1],[0,0,1,0,1,1,1,1,1,0,1,1,1,1,1,0,0,1,1,0,1,0,0,1,1,0,0,1,0,1,1,1,1,0,0,1,0,1,1,0],[1,1,1,1,1,1,0,1,0,0,1,1,1,0,0,0,0,0,1,0,1,1,0,1,1,0,0,1,1,0,1,1,0,1,1,1,0,1,1,1],[0,1,1,1,1,1,0,0,1,0,1,0,1,0,0,0,1,0,0,1,0,1,1,0,0,0,0,0,0,1,0,0,0,1,0,1,1,1,0,1],[0,1,0,0,1,1,0,1,1,1,1,1,0,0,0,0,1,1,1,1,0,0,0,0,0,1,0,1,0,0,1,0,1,1,0,0,1,1,1,1],[1,0,0,0,1,1,0,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1,0,0,1,0,1,0,0,1,1,0,1,1,1,1,0,1,0,1],[1,1,1,1,0,1,0,1,1,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,1,0,0,1,0,0,1,0,1,0,0,1,1,0,0,0]],
257)) #54
print(Solution().shortestPath([
 [0,0,0],
 [1,1,0],
 [0,0,0],
 [0,1,1],
 [0,0,0]], 1)) # 6
print(Solution().shortestPath([[0,1,1],
 [1,1,1],
 [1,0,0]], 1)) # -1
