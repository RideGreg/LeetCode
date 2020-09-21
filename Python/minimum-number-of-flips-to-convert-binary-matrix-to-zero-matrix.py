# Time:  O((m * n) * 2^(m * n))，total 2^(m*n) states, in each state try to flip each of m*n positions.
# Space: O(2^(m * n)), queue to store total number of states.

# 1284 weekly contest 166 12/7/2019

# Given a m x n binary matrix mat. In one step, you can choose one cell and flip it and all the four neighbours
# of it if they exist (Flip is changing 1 to 0 and 0 to 1). A pair of cells are called neighboors if they share one edge.
#
# Return the minimum number of steps required to convert mat to a zero matrix or -1 if you cannot.
#
# Binary matrix is a matrix with all cells equal to 0 or 1 only.
#
# Zero matrix is a matrix with all cells equal to 0.

# Constraints: 1<=mat.length<=3, 1<=mat[0].length<=3, mat[i][j] is 0 or 1

import collections

# 求到达目的状态的最少翻转次数，自然想到使用广度优先搜索。
# 本题的状态表示是一个二维矩阵。如果将二维矩阵直接作为状态进行存储，会占用较多空间，并且不易判断其是否被搜索过：
# Python中可以使用 set() 存储和判断二维矩阵，但在 Java和C++ 中实现起来复杂。因此考虑将二维矩阵与语言的内置类型进行映射。
# 因为矩阵所有元素都是0或1，可把二维矩阵展开，看出一个二进制数，就得到了一种从二维矩阵到整数的映射方法。

class Solution(object):
    def minFlips(self, mat): # USE THIS: bit representation is a better way to record state
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        directions = [(0, 0), (0, 1), (1, 0), (0, -1), (-1, 0)]
        # bit presentation [[0,0], [0,1]] => 1000 = 8
        # total states are from 0 -> 1<<(m*n) - 1 or 2^(m*n)-1
        start = sum(val << r*len(mat[0])+c for r, row in enumerate(mat) for c, val in enumerate(row))
        q = collections.deque([(start, 0)])
        lookup = {start}
        while q:
            state, step = q.popleft()
            if state == 0:           # required destination, it can be any state.
                return step
            for r in range(len(mat)):
                for c in range(len(mat[0])):
                    new_state = state
                    for dr, dc in directions:
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < len(mat) and 0 <= nc < len(mat[0]):
                            new_state ^= 1 << nr*len(mat[0])+nc
                    if new_state not in lookup:
                        lookup.add(new_state)
                        q.append((new_state, step+1))
        return -1

    def minFlips_ming(self, mat): # same algorithm
        def compress(m):
            ans = [m[i][j] for i in range(len(m)) for j in range(len(m[0]))]
            return tuple(ans)

        def flip(ma, i, j):
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    ma[ni][nj] ^= 1

        m, n = len(mat), len(mat[0])
        dirs = [(0,0),(-1,0),(1,0),(0,-1),(0,1)]
        dp, ans = [mat], 0
        seen = {compress(mat)}
        while dp:
            ndp = []
            for ma in dp:
                if sum(map(sum, ma)) == 0: return ans
                for i in range(m):
                    for j in range(n):
                        flip(ma, i, j)
                        tt = compress(ma)
                        if tt not in seen:
                            nma = [r[:] for r in ma] # make a new list
                            ndp.append(nma)
                            seen.add(tt)
                        flip(ma, i, j)
            dp = ndp
            ans += 1
        return -1



print(Solution().minFlips([[0,0],[0,1]])) # 3
print(Solution().minFlips([[0]])) # 0
print(Solution().minFlips([[1,1,1],[1,0,1],[0,0,0]])) # 6
print(Solution().minFlips([[1,0,0],[1,0,0]])) # -1
