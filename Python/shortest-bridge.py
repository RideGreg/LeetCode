# Time:  O(n^2)
# Space: O(n^2)

# 934
# In a given 2D binary array A, there are two islands.  (An island is a 4-directionally connected group of 1s
# not connected to any other 1s.)
#
# Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.
#
# Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1.)

# Solution: DFS + BFS
# Conceptually, our method is very straightforward: use DFS to find both islands, then for one of the islands,
# use BFS to grow it by 1 until we touch the second island. The solution is verbose though.

import collections


class Solution(object):
    # USE THIS, change value of island 1, don't need to find 2 islands upfront.
    def shortestBridge(self, A):
        def dfs(): # iterative using stack, find the first island
            for i in xrange(m):
                for j in xrange(n):
                    if A[i][j] == 1:
                        A[i][j] = -1
                        stack = [(i,j)]
                        source.append(((i,j), 0))
                        while stack:
                            x,y = stack.pop()
                            for dx, dy in delta:
                                nx, ny = x + dx, y + dy
                                if 0 <= nx < m and 0 <= ny < n and A[nx][ny] == 1:
                                    A[nx][ny] = -1
                                    stack.append((nx,ny))
                                    source.append(((nx, ny), 0))
                        return

        def bfs():
            visited = set()
            while source:
                (x,y), step = source.popleft()
                for dx, dy in delta:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n:
                        if A[nx][ny] == 1: return step
                        if A[nx][ny] == 0 and (nx,ny) not in visited:
                            source.append(((nx, ny), step+1))
                            visited.add((nx,ny))
            return float('inf')

        m, n = len(A), len(A[0])
        delta = [(-1,0), (1,0), (0, -1), (0, 1)]
        source = collections.deque([])
        dfs()
        return bfs()


    def shortestBridge_LeetCodeOfficial(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def get_islands(A):
            islands = []
            done = set()
            for r, row in enumerate(A):
                for c, val in enumerate(row):
                    if val and (r, c) not in done:
                        s = [(r, c)]
                        visited = set(s)
                        while s:
                            x, y = s.pop()
                            for dx, dy in directions:
                                nx, ny = x+dx, y+dy
                                if 0 <= nx < len(A) and 0 <= ny < len(A[0]) and \
                                    (nx, ny) not in visited and A[nx][ny]:
                                    s.append((nx, ny))
                                    visited.add((nx, ny))
                        done |= visited
                        islands.append(visited)
                        if len(islands) == 2:
                            break
            return islands

        source, target = get_islands(A)
        q = collections.deque([(node, 0) for node in source])
        while q:
            node, dis = q.popleft()
            if node in target:
                return dis-1
            for dx, dy in directions:
                nx, ny = node[0]+dx, node[1]+dy
                if 0 <= nx < len(A) and 0 <= ny < len(A[0]) and (nx, ny) not in source:
                    q.append(((nx, ny), dis+1))
                    source.add((nx, ny))

print(Solution().shortestBridge([[0,1,0],[0,0,0],[0,0,1]])) # 2
print(Solution().shortestBridge([[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]])) # 1