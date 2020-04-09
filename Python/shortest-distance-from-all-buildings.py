# Time:  O(k * m * n), k is the number of the buildings
# Space: O(m * n)

# 317
# You want to build a house on an empty land which reaches all buildings in the shortest amount of distance.
# You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:
#
# Each 0 marks an empty land which you can pass by freely.
# Each 1 marks a building which you cannot pass through.
# Each 2 marks an obstacle which you cannot pass through.

try:
    xrange
except NameError:
    xrange = range

class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def bfs(x, y):
            dist = 0
            visited = [[False for _ in xrange(n)] for _ in xrange(m)]
            visited[x][y] = True

            pre_level = [(x, y)]
            while pre_level:
                dist += 1
                cur_level = []
                for i, j in pre_level:
                    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        I, J = i+di, j+dj
                        if 0 <= I < m and 0 <= J < n and grid[I][J] == 0 and not visited[I][J]:
                            cnts[I][J] += 1
                            dists[I][J] += dist
                            cur_level.append((I, J))
                            visited[I][J] = True

                pre_level = cur_level


        m, n, cnt = len(grid),  len(grid[0]), 0
        # dists stores the total distance from this cell to all houses
        # cnts stores how many houses can be reached from this cell
        dists = [[0 for _ in xrange(n)] for _ in xrange(m)]
        cnts = [[0 for _ in xrange(n)] for _ in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 1:
                    cnt += 1
                    bfs(i, j)

        shortest = float("inf")
        for i in xrange(m):
            for j in xrange(n):
                if dists[i][j] < shortest and cnts[i][j] == cnt: # make sure reached all houses
                    shortest = dists[i][j]

        return shortest if shortest != float("inf") else -1

print(Solution().shortestDistance([
    [1,0,2,0,1],
    [0,0,0,0,0],
    [0,0,1,0,0]
])) # 7
# dists
# [[0,9,0,9,0],
#  [9,8,7,8,9],
#  [10,9,0,9,10]]
# cnts
# [[0,3,0,3,0],
#  [3,3,3,3,3],
#  [3,3,0,3,3]]
