# Time:  O(m * n)
# Space: O(g)

# 286
# You are given a m x n 2D grid initialized with these three possible values.
# -1 - A wall or an obstacle.
# 0 - A gate.
# INF - Infinity means an empty room. We use the value 2^31 - 1 = 2147483647 to represent INF as
# you may assume that the distance to a gate is less than 2147483647.
# Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate,
# it should be filled with INF.


# Better start from 0 (gate) and populate; for empty rooms which cannot be reached, just stay inf.
# If start from inf (empty room), it may not reach a gate and just waste.
from collections import deque

class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        INF = 2**31-1
        m, n = len(rooms), len(rooms[0])
        q = deque((i, j) for i in range(m) for j in range(n) if rooms[i][j] == 0)
        while q:
            i, j = q.popleft()
            for ni, nj in ((i+1, j), (i-1, j), (i, j-1), (i, j+1)):
                if 0<=ni<m and 0<=nj<n and rooms[ni][nj] == INF:
                    rooms[ni][nj] = rooms[i][j] + 1
                    q.append((ni, nj))

mtx = [
    [2147483647, -1,         0,          2147483647],
    [2147483647, 2147483647, 2147483647, -1],
    [2147483647, -1,         2147483647, -1],
    [0,          -1,         2147483647, 2147483647]
]
Solution().wallsAndGates(mtx)
print(mtx)
#   3  -1   0   1
#   2   2   1  -1
#   1  -1   2  -1
#   0  -1   3   4