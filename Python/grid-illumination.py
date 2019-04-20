# Time:  O(l + q)
# Space: O(l)

# 1001
# On a N x N grid of cells, each cell (x, y) with 0 <= x < N and 0 <= y < N has a lamp.
#
# Initially, some number of lamps are on.  lamps[i] tells us the location of the i-th lamp that is on.
# Each lamp that is on illuminates every square on its x-axis, y-axis, and both diagonals (similar to
# a Queen in chess).
#
# For the i-th query queries[i] = (x, y), the answer to the query is 1 if the cell (x, y) is illuminated, else 0.
#
# After each query (x, y) [in the order given by queries], we turn off any lamps that are at cell (x, y)
# or are adjacent 8-directionally (ie., share a corner or edge with cell (x, y).)
#
# Return an array of answers.  Each value answer[i] should be equal to the answer of the i-th query queries[i].

# 1 <= N <= 10^9
# 0 <= lamps.length <= 20000
# 0 <= queries.length <= 20000
# lamps[i].length == queries[i].length == 2

import collections


class Solution(object):
    def gridIllumination(self, N, lamps, queries):
        """
        :type N: int
        :type lamps: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        lookup = set()
        row = collections.defaultdict(int)
        col = collections.defaultdict(int)
        diag = collections.defaultdict(int)
        anti = collections.defaultdict(int)
        
        for r, c in lamps:
            lookup.add((r, c)) # convert list to set, otherwise TLE
            row[r] += 1
            col[c] += 1
            diag[r-c] += 1
            anti[r+c] += 1
        
        result = []
        for r, c in queries:
            if row[r] or col[c] or diag[r-c] or anti[r+c]:
                result.append(1)
            else:
                result.append(0)

            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < N and 0 <= nc < N and (nr, nc) in lookup:
                        lookup.remove((nr, nc))
                        row[nr] -= 1
                        col[nc] -= 1
                        diag[nr-nc] -= 1
                        anti[nr+nc] -= 1
        return result

print(Solution().gridIllumination(5, [[0,0],[4,4]], [[1,1],[1,0]])) # [1, 0]