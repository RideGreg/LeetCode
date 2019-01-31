# Time:  O(n^2), amortized from O(n^2*alpha(n)) where alpha(n) is the Inverse-Ackermann function
# (if we were to use union-find by rank) and amortized to 1.
# Space: O(n^2)

# 959
# In a N x N grid composed of 1 x 1 squares, each 1 x 1 square consists of a /, \, or blank space.
# These characters divide the square into contiguous regions.
# (Note that backslash characters are escaped, so a \ is represented as "\\".)
#
# Return the number of regions.

# Input: [
#   " /",
#   "/ "
]
# Output: 2

# Input: [
#   " /",
#   "  "
# ]
# Output: 1

# Input:
# [
#   "\\/",
#   "/\\"
# ]
# Output: 4

# Input:
# [
#   "/\\",
#   "\\/"
# ]
# Output: 5

# Input:
# [
#   "//",
#   "/ "
# ]
# Output: 3


# Solution: Union-Find. The main difficulty with this problem is in specifying the graph.
#
# One "brute force" way to specify the graph is to associate each grid square with 4 nodes
# (north, south, west, and east), representing 4 triangles inside the square if it were to have both slashes.
# Then connect all neighboring nodes. Finally connect all 4 nodes if the grid square is " ",
# and connect two pairs if the grid square is "/" or "\".

class UnionFind(object):
    def __init__(self, n):
        self.set = range(n)
        self.count = n

    def find_set(self, x):
       if self.set[x] != x:
           self.set[x] = self.find_set(self.set[x])  # path compression.
       return self.set[x]

    def union_set(self, x, y):
        x_root, y_root = map(self.find_set, (x, y))
        if x_root != y_root:
            self.set[min(x_root, y_root)] = max(x_root, y_root)
            self.count -= 1


class Solution(object):
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        def index(n, i, j, k):
            return (i*n + j)*4 + k
    
        m = len(grid)
        union_find = UnionFind(n**2 * 4)
        N, E, S, W = range(4)
        for i in xrange(m):
            for j in xrange(m):
                if i:
                    union_find.union_set(index(m, i-1, j, S),
                                         index(m,i, j, N))
                if j:
                    union_find.union_set(index(m, i, j-1, E),
                                         index(m, i, j, W))
                if grid[i][j] != "/":
                    union_find.union_set(index(m, i, j, N),
                                         index(m, i, j, E))
                    union_find.union_set(index(m, i, j, S),
                                         index(m, i, j, W))
                if grid[i][j] != "\\":
                    union_find.union_set(index(m, i, j, W),
                                         index(m, i, j, N))
                    union_find.union_set(index(m, i, j, E),
                                         index(m, i, j, S))
        return union_find.count
