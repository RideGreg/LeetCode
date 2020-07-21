# Time:  O(m * n)
# Space: O(m * n)

# 694
# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land)
# connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid
# are surrounded by water.
#
# Count the number of distinct islands. An island is considered to be the same as another
# if and only if one island can be translated (and not rotated or reflected) to equal the other.

class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        directions = {'u':[-1,  0], 'd':[ 1,  0], \
                      'l':[ 0, -1], 'r':[ 0,  1]}

        def dfs(i, j):
            if not (0 <= i < len(grid) and \
                    0 <= j < len(grid[0]) and \
                    grid[i][j] > 0):
                return False
            grid[i][j] *= -1 # mark visited
            for k, v in directions.items():
                island.append(k)
                dfs(i+v[0], j+v[1])
            return True

        islands = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                island = []
                if dfs(i, j):
                    islands.add("".join(island))
        return len(islands)

    def numDistinctIslands_wrong(self, grid):
        """ cannot differentiate, both return 'dr'
        1 1     and    1
        1              1 1
        """
        directions = {'u':[-1,  0], 'd':[ 1,  0], \
                      'l':[ 0, -1], 'r':[ 0,  1]}

        def dfs(i, j):
            grid[i][j] *= -1 # mark visited
            for k, v in directions.items():
                ni, nj = i+v[0], j+v[1]
                if 0<=ni<len(grid) and 0<=nj<len(grid[0]) and grid[ni][nj] > 0:
                    island.append(k)
                    dfs(ni, nj)

        islands = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    island = []
                    dfs(i, j)
                    islands.add("".join(island))
        return len(islands)

print(Solution().numDistinctIslands([
    [1,1,0,1,1],
    [1,0,0,0,0],
    [0,0,0,0,1],
    [1,1,0,1,1]
])) # 3 {'udlr udlr', 'ud udl udlr r lr', 'ud udlr l rudlr'}

print(Solution().numDistinctIslands([
    [1,1,0,1,1],
    [1,0,0,0,0],
    [0,0,0,1,0],
    [1,1,0,1,1]
])) # 3 {'udlrudlr', 'ududlrudlrlr', 'ududlrlrudlr'}

print(Solution().numDistinctIslands([
    [1,1,0,0,1],
    [1,1,0,0,0],
    [0,0,0,1,1],
    [0,0,0,1,1]
])) # 2 {'udlr', 'ududlruudlrdlrlr'}