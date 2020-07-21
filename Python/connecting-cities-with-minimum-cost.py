# Time:  O(nlogn)
# Space: O(n)

# 1135
# There are N cities numbered from 1 to N.
#
# You are given connections, where each connections[i] = [city1, city2, cost] represents the cost to
# connect city1 and city2 together.  (A connection is bidirectional: connecting city1 and city2 is
# the same as connecting city2 and city1.)
#
# Return the minimum cost so that for every pair of cities, there exists a path of connections
# (possibly of length 1) that connects those two cities together.  The cost is the sum of the
# connection costs used. If the task is impossible, return -1.

class UnionFind(object):
    def __init__(self, n):
        self.set = list(range(n))
        self.count = n

    def find_set(self, x):
        if self.set[x] != x:
            self.set[x] = self.find_set(self.set[x])  # path compression.
        return self.set[x]

    def union_set(self, x, y):
        x_root, y_root = map(self.find_set, (x, y))
        if x_root == y_root:
            return False
        self.set[min(x_root, y_root)] = max(x_root, y_root)
        self.count -= 1
        return True


class Solution(object):
    def minimumCost(self, N, connections):
        """
        :type N: int
        :type connections: List[List[int]]
        :rtype: int
        """
        connections.sort(key = lambda x: x[2])
        union_find = UnionFind(N)
        result = 0
        for u, v, val in connections:
            if union_find.union_set(u-1, v-1):
                result += val
        return result if union_find.count == 1 else -1
