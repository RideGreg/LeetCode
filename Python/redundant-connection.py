# -*- encoding=utf-8 -*-

# Time:  O(nα(n)) ~= O(n), where n is # of vertices (also # of edges) in the graph, and \alphaα is the Inverse-Ackermann function.
# We make up to n queries of dsu.union, which takes (amortized) O(α(N)) time. Outside the scope of this article, it can be shown
# why dsu.union has O(\alpha(N))O(α(N)) complexity, what the Inverse-Ackermann function is, and why O(\alpha(N))O(α(N)) is approximately O(1).
# Space: O(n), construction of parent array.

# 684 无向图去环
# In this problem, a tree is an undirected graph that is connected and has no cycles.
#
# The given input is a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N), with one additional edge added. The 
# added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.
#
# The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] with u < v, that represents an 
# undirected edge connecting nodes u and v.
#
# Return an edge that can be removed so that the resulting graph is a tree of N nodes. If there are multiple answers, return the answer 
# that occurs last in the given 2D-array. The answer edge [u, v] should be in the same format, with u < v.
#
# Example 1:
# Input: [[1,2], [1,3], [2,3]]
# Output: [2,3]
# Explanation: Original tree will be like this:
#   1
#  / \
# 2 - 3
#
# Example 2:
# Input: [[1,2], [2,3], [3,4], [1,4], [1,5]]
# Output: [1,4]
# Explanation: Original tree will be like this:
# 5 - 1 - 2
#     |   |
#     4 - 3

# Note:
# The size of the input 2D-array will be between 3 and 1000.
# Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.

# A Disjoint Set Union (DSU) data structure can be used to maintain knowledge of the connected components of a graph,
# and query for them quickly. In particular, we would like to support two operations:
# - dsu.find(node x), which outputs a unique id so that two nodes have the same id if and only if they are in the same connected component.
# - dsu.union(node x, node y), which connects the components with id find(x) and find(y) together.

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
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        union_find = UnionFind(len(edges)+1)
        for edge in edges:
            if not union_find.union_set(*edge):
                return edge
        return []



    # DFS in graph: 1. how to build graph: defaultdict(set);
    #               2. how to dfs: traverse neighbor, filter visited (don't go back), use 'any' when traversing neighbors
    #
    # Time: O(n^2), where n is # of vertices (also # of edges) in the graph. In the worst case, for every edge we include,
    #               we have to search every previously-occurring edge of the graph.
    # Space: O(n), The current construction of the graph has at most n nodes.
    def findRedundantConnection_dfs(self, edges):
        import collections
        graph = collections.defaultdict(set)

        def dfs(source, target):
            if source in seen:
                return False
            seen.add(source)
            if source == target: return True
            return any(dfs(nei, target) for nei in graph[source])

        for u, v in edges:
            seen = set() # reset seen for each new edge
            if u in graph and v in graph and dfs(u, v):
                return u, v
            graph[u].add(v)
            graph[v].add(u)

print(Solution().findRedundantConnection([[1,2], [1,3], [2,3]])) # [2,3]
print(Solution().findRedundantConnection([[1,2], [2,3], [3,4], [1,4], [1,5]])) # [1,4]