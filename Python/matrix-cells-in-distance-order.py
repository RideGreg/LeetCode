# Time:  O(m * n)
# Space: O(1)

# 1030
# We are given a matrix with R rows and C columns has cells with integer coordinates (r, c), where 0 <= r < R and 0 <= c < C.
#
# Additionally, we are given a cell in that matrix with coordinates (r0, c0).
#
# Return the coordinates of all cells in the matrix, sorted by their distance from (r0, c0) from smallest
# distance to largest distance.  Here, the distance between two cells (r1, c1) and (r2, c2) is the Manhattan distance,
#  |r1 - r2| + |c1 - c2|.  (You may return the answer in any order that satisfies this condition.)

# Note: 1 <= R <= 100, 1 <= C <= 100, 0 <= r0 < R, 0 <= c0 < C

# Input: R = 2, C = 3, r0 = 1, c0 = 2
# Output: [[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]]
# Explanation: The distances from (r0, c0) to other cells are: [0,1,1,2,2,3]
# There are other answers that would also be accepted as correct, such as [[1,2],[1,1],[0,2],[1,0],[0,1],[0,0]].

from typing import List

class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        def append(x, y):
            if 0<=x<R and 0<=y<C:
                ans.append([x,y])

        ans = [[r0, c0]]
        maxd = max(r0+c0, R-1-r0+c0, r0+C-1-c0, R-1-r0+C-1-c0)
        for d in range(1, maxd+1):
            # dx is in [-d, d]
            append(r0-d, c0)
            for dx in range(-d+1, d):
                dy = d - abs(dx)
                append(r0+dx, c0+dy)
                append(r0+dx, c0-dy)
            append(r0+d, c0)
        return ans

    # bfs, need extra space for queue
    def allCellsDistOrder_bfs(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        import collections
        seen = set()
        ans = []
        q = collections.deque([(r0, c0)])
        seen.add((r0, c0))
        while q:
            r,c = q.popleft()
            ans.append([r,c])
            for nr, nc in [(r-1,c), (r+1,c),(r,c-1),(r,c+1)]:
                if 0<=nr<R and 0<=nc<C and (nr, nc) not in seen:
                    q.append((nr,nc))
                    seen.add((nr, nc))
        return ans

    # sort, time O((m*n*log(m*n))
    def allCellsDistOrder_sort(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        ans = []
        for i in range(R):
            for j in range(C):
                ans.append([i,j])
        return sorted(ans, key= lambda p: abs(p[0]-r0)+abs(p[1]-c0))

print(Solution().allCellsDistOrder(2,2,0,1)) # [[0,1],[0,0],[1,1],[1,0]]