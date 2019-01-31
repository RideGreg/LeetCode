# Time:  O(n)
# Space: O(n)

# 947
# On a 2D plane, we place stones at some integer coordinate points.  Each coordinate point may have at most one stone.
#
# Now, a move consists of removing a stone that shares a column or row with another stone on the grid.
#
# What is the largest possible number of moves we can make?

# 1 <= stones.length <= 1000
# 0 <= stones[i][j] < 10000

class UnionFind(object):
    def __init__(self, n):
        self.set = range(n)

    def find_set(self, x):
        if self.set[x] != x:
            self.set[x] = self.find_set(self.set[x])  # path compression.
        return self.set[x]

    def union_set(self, x, y):
        x_root, y_root = map(self.find_set, (x, y))
        if x_root == y_root:
            return False
        self.set[min(x_root, y_root)] = max(x_root, y_root)
        return True


class Solution(object):
    def removeStones(self, stones): # 230 ms
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        MAX_ROW = 10000
        union_find = UnionFind(2*MAX_ROW)
        for r, c in stones:
            union_find.union_set(r, c+MAX_ROW)
        return len(stones) - len({union_find.find_set(r) for r, _ in stones})

    # Time: O(n^2), 1600 ms
    def removeStones_regularUnionFind(self, stones):
        def find(x):
            if map[x] != x:
                map[x] = find(map[x])
            return map[x]

        def union(x, y):
            fx, fy = find(x), find(y)
            if fx != fy:
                map[fx] = fy
                self.count -= 1

        N = len(stones)
        map = range(N)
        self.count = N
        for i in range(N):
            for j in range(i + 1, N):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    union(i, j)
        return N - self.count


print(Solution().removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]])) # 5
print(Solution().removeStones([[0,0],[0,2],[1,1],[2,0],[2,2]])) # 3
print(Solution().removeStones([[0,0]])) # 0