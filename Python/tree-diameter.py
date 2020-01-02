# Time:  O(|V| + |E|)
# Space: O(|E|)

# 1244 biweekly contest 12 11/2/2019
#
# Given an undirected tree, return its diameter: the number of edges in a longest path in that tree.
#
# The tree is given as an array of edges where edges[i] = [u, v] is a bidirectional edge between nodes u and v.
# Each node has labels in the set {0, 1, ..., edges.length}.

import collections


class Solution(object):
    def treeDiameter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        graph, nodeCnt = collections.defaultdict(set), 0
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        curr_edges = {(None, u) for u, nei in graph.items() if len(nei) == 1}
        while curr_edges:
            nEdges = set()
            for prev, u in curr_edges:
                for v in graph[u]:
                    if v != prev:
                        nEdges.add((u, v))
            curr_edges = nEdges
            nodeCnt += 1
        return max(nodeCnt-1, 0)


# The following method seems not working
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.child = []
class Solution2:
    def treeDiameter(self, edges):
        import collections
        conn = collections.defaultdict(list)
        for x,y in edges:
            x,y = min(x,y), max(x,y)
            conn[x].append(y)

        _min = min(conn)
        root = TreeNode(_min)
        def build(root):
            for n in conn[root.val]:
                nnode = TreeNode(n)
                root.child.append(nnode)
                build(nnode)

        build(root)

        def depth(root, diameter):
            if not root: return 0, diameter
            a1, a2 = 0, 0
            for _nxt in root.child:
                v, d = depth(_nxt, diameter)
                a1 = max(a1, v)
                a2 += d
            left, diameter = depth(root.left, diameter)
            right, diameter = depth(root.right, diameter)
            return 1 + max(left, right), max(diameter, left + right)

        ans = depth(root, 0)[1]
        return ans


print(Solution().treeDiameter([[0,1],[1,2],[2,3],[1,4],[4,5]])) # 4
print(Solution().treeDiameter([[0,1],[0,2]])) # 2
