# Time:  O((m * n) * log(m * n))
# Space: O(m * n)

# 711
# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land)
# connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid
# are surrounded by water.
#
# Count the number of distinct islands. An island is considered to be the same as another
# if they have the same shape, or have the same shape after rotation (90, 180, or 270 degrees only)
# or reflection (left/right direction or up/down direction).

class Solution(object):
    def numDistinctIslands2(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        def dfs(i, j, grid, island):
            if not (0 <= i < len(grid) and \
                    0 <= j < len(grid[0]) and \
                    grid[i][j] > 0):
                return False
            grid[i][j] *= -1
            island.append((i, j));
            for d in directions:
                dfs(i+d[0], j+d[1], grid, island)
            return True

        def normalize(island):
            shapes = [[] for _ in xrange(8)]
            for x, y in island:
                rotations_and_reflections = [[ x,  y], [ x, -y], [-x, y], [-x, -y],
                                             [ y,  x], [ y, -x], [-y, x], [-y, -x]]
                for i in xrange(len(rotations_and_reflections)):
                    shapes[i].append(rotations_and_reflections[i])
            for shape in shapes:
                shape.sort()  # Time: O(ilogi), i is the size of the island, the max would be (m * n)
                origin = list(shape[0])
                for p in shape:
                    p[0] -= origin[0]
                    p[1] -= origin[1]
            return min(shapes)

        islands = set()
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                island = []
                if dfs(i, j, grid, island):
                    islands.add(str(normalize(island)))
        return len(islands)
