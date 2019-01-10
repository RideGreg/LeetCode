# Time:  O(nlog*n) ~= O(n), n is the length of the positions
# Space: O(n)

# 685 有向图去环去多重父节点
# In this problem, a rooted tree is a directed graph such that,
# there is exactly one node (the root) for
# which all other nodes are descendants of this node, plus every node has exactly one parent,
# except for the root node which has no parents.
#
# The given input is a directed graph that started as a rooted tree with N nodes
# (with distinct values 1, 2, ..., N), with one additional directed edge added.
# The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.
#
# The resulting graph is given as a 2D-array of edges.
# Each element of edges is a pair [u, v] that represents a directed edge connecting nodes u and v,
# where u is a parent of child v.
#
# Return an edge that can be removed so that the resulting graph is a rooted tree of N nodes.
# If there are multiple answers, return the answer that occurs last in the given 2D-array.
#
# Example 1:
# Input: [[1,2], [1,3], [2,3]]
# Output: [2,3]
# Explanation: The given directed graph will be like this:
#   1
#  / \
# v   v
# 2-->3
# Example 2:
# Input: [[1,2], [2,3], [3,4], [4,1], [1,5]]
# Output: [4,1]
# Explanation: The given directed graph will be like this:
# 5 <- 1 -> 2
#      ^    |
#      |    v
#      4 <- 3
# Note:
# The size of the input 2D-array will be between 3 and 1000.
# Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.

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

# let's enumerate the possibilities for the "redundant" edge.
# - If there is no loop, then one vertex must have two parents: should return 2nd edge.
# - If there is a loop, then:
#   - either one vertex has two parents: don't use 2nd edge in loop testing, then the redundant must be 1st edge;
#   - or every vertex has one parent: return the last edge formed the cycle.

class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        cand1, cand2 = [], []
        parent = {}
        for edge in edges:
            if edge[1] not in parent:
                parent[edge[1]] = edge[0]
            else:
                # record multi-parents
                cand1 = [parent[edge[1]], edge[1]]
                cand2 = edge

        union_find = UnionFind(len(edges)+1)
        for edge in edges:
            if edge == cand2: # skip cand2 in testing loop, otherwise fail for [[1,2],[1,3],[2,3]], expect [2,3]
                continue
            if not union_find.union_set(*edge):
                if cand2:
                    # has both multi parents and loop, return 1st edge in multi parents, since cand2 is not used to test loop
                    return cand1
                else:
                    # no multi parents, return the last edge in loop
                    return edge
        return cand2 # no loop, return 2nd edge in multi parents

    # LeetCode official solution
    def findRedundantDirectedConnection_dfs(self, edges):
        N = len(edges)
        parent = {}
        candidates = []
        for u, v in edges:
            if v in parent:
                candidates.append((parent[v], v))
                candidates.append((u, v))
            else:
                parent[v] = u

        def orbit(node):
            seen = set()
            while node in parent and node not in seen:
                seen.add(node)
                node = parent[node]
            return node, seen

        root = orbit(1)[0]

        if not candidates:
            cycle = orbit(root)[1]
            for u, v in edges:
                if u in cycle and v in cycle:
                    ans = u, v
            return ans

        children = collections.defaultdict(list)
        for v in parent:
            children[parent[v]].append(v)

        seen = [True] + [False] * N
        stack = [root]
        while stack:
            node = stack.pop()
            if not seen[node]:
                seen[node] = True
                stack.extend(children[node])

        return candidates[all(seen)]

