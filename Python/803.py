'''
We have a grid of 1s and 0s; the 1s in a cell represent bricks.  A brick will not drop if and only if it is directly connected to the top of the grid, or at least one of its (4-way) adjacent bricks will not drop.

We will do some erasures sequentially. Each time we want to do the erasure at the location (i, j), the brick (if it exists) on that location will disappear, and then some other bricks may drop because of that erasure.

Return an array representing the number of bricks that will drop after each erasure in sequence.

Example 1:
Input:
grid = [[1,0,0,0],[1,1,1,0]]
hits = [[1,0]]
Output: [2]
Explanation:
If we erase the brick at (1, 0), the brick at (1, 1) and (1, 2) will drop. So we should return 2.
Example 2:
Input:
grid = [[1,0,0,0],[1,1,0,0]]
hits = [[1,1],[1,0]]
Output: [0,0]
Explanation:
When we erase the brick at (1, 0), the brick at (1, 1) has already disappeared due to the last move. So each erasure will cause no bricks dropping.  Note that the erased brick (1, 0) will not be counted as a dropped brick.


Note:

The number of rows and columns in the grid will be in the range [1, 200].
The number of erasures will not exceed the area of the grid.
It is guaranteed that each erasure will be different from any other erasure, and located inside the grid.
An erasure may refer to a location with no brick - if it does, no bricks drop.

Approach #1: Reverse Time and Union-Find [Accepted]
Intuition

The problem is about knowing information about the connected components of a graph as we cut vertices. In particular, we'll like to know the size of the "roof" (component touching the top edge) between each cut. Here, a cut refers to the erasure of a vertex.

As we may know, a useful data structure for joining connected components is a disjoint set union structure. The key idea in this problem is that we can use this structure if we work in reverse: instead of looking at the graph as a series of sequential cuts, we'll look at the graph after all the cuts, and reverse each cut.

Algorithm

We'll modify our typical disjoint-set-union structure to include a dsu.size operation, that tells us the size of this component. The way we do this is whenever we make a component point to a new parent, we'll also send it's size to that parent.

We'll also include dsu.top, which tells us the size of the "roof", or the component connected to the top edge. We use an ephemeral "source" node with label R * C where all nodes on the top edge (with row number 0) are connected to the source node.

For more information on DSU, please look at Approach #2 in the article here.

Next, we'll introduce A, the grid after all the cuts have happened, and initialize our disjoint union structure on the graph induced by A (nodes are grid squares with a brick; edges between 4-directionally adjacent nodes).

After, if we get an cut at (r, c) but the original grid[r][c] was always 0, then we couldn't have had a meaningful cut - the number of dropped bricks is 0.

Otherwise, we'll look at the size of the new roof after adding this brick at (r, c), and compare them to find the number of dropped bricks.

Since we were working in reverse time order, we should reverse our working answer to arrive at our final answer.

Complexity Analysis

Time Complexity: O(N*Q*\alpha(N * Q))O(N∗Q∗α(N∗Q)), where N = R*CN=R∗C is the number of grid squares, QQ is the length of hits, and \alphaα is the Inverse-Ackermann function.

Space Complexity: O(N)O(N).
'''

class DSU:
    def __init__(self, R, C):
        #R * C is the source, and isn't a grid square
        self.par = range(R*C + 1)
        self.rnk = [0] * (R*C + 1)
        self.sz = [1] * (R*C + 1)

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr: return
        if self.rnk[xr] < self.rnk[yr]:
            xr, yr = yr, xr
        if self.rnk[xr] == self.rnk[yr]:
            self.rnk[xr] += 1

        self.par[yr] = xr
        self.sz[xr] += self.sz[yr]

    def size(self, x):
        return self.sz[self.find(x)]

    def top(self):
        # Size of component at ephemeral "source" node at index R*C,
        # minus 1 to not count the source itself in the size
        return self.size(len(self.sz) - 1) - 1

class Solution(object):
    def hitBricks(self, grid, hits):
        R, C = len(grid), len(grid[0])
        def index(r, c):
            return r * C + c

        def neighbors(r, c):
            for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        A = [row[:] for row in grid]
        for i, j in hits:
            A[i][j] = 0

        dsu = DSU(R, C)
        for r, row in enumerate(A):
            for c, val in enumerate(row):
                if val:
                    i = index(r, c)
                    if r == 0:
                        dsu.union(i, R*C)
                    if r and A[r-1][c]:
                        dsu.union(i, index(r-1, c))
                    if c and A[r][c-1]:
                        dsu.union(i, index(r, c-1))

        ans = []
        for r, c in reversed(hits):
            pre_roof = dsu.top()
            if grid[r][c] == 0:
                ans.append(0)
            else:
                i = index(r, c)
                for nr, nc in neighbors(r, c):
                    if A[nr][nc]:
                        dsu.union(i, index(nr, nc))
                if r == 0:
                    dsu.union(i, R*C)
                A[r][c] = 1
                ans.append(max(0, dsu.top() - pre_roof - 1))
        return ans[::-1]