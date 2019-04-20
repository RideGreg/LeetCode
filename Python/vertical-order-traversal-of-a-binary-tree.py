# Time:  O(nlogn)
# Space: O(n)

# 987
# Given a binary tree, return the vertical order traversal of its nodes values.
#
# For each node at position (X, Y), its left and right children respectively will be at positions
# (X-1, Y-1) and (X+1, Y-1).
#
# Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line touches
# some nodes, we report the values of the nodes in order from top to bottom (decreasing Y coordinates).
#
# If two nodes have the same position, then the value of the node that is reported first is the value
# that is smaller.
#
# Return an list of non-empty reports in order of X coordinate.  Every report will have a list of
# values of nodes.

import collections


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def verticalTraversal(self, root): # USE THIS: 2 sorting: x, (y, val)
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def dfs(node, x, y):
            if node:
                v[x].append((y, node.val))
                dfs(node.left, x - 1, y + 1)
                dfs(node.right, x + 1, y + 1)

        import collections
        v = collections.defaultdict(list)
        dfs(root, 0, 0)
        ans = []
        for x, nodes in sorted(v.items()):
            ans.append([n[1] for n in sorted(nodes)])
        return ans

    # 3 sorting needed: x, y, val. The results from sorting y & val still need to be assembled.
    def verticalTraversal_LeetcodeOfficial(self, root):
        def dfs(node, x, y):
            if node:
                lookup[x][y].append(node)
                dfs(node.left, x-1, y+1)
                dfs(node.right, x+1, y+1)
                
        lookup = collections.defaultdict(lambda: collections.defaultdict(list))
        dfs(root, 0, 0)

        result = []
        for x in sorted(lookup):
            report = []
            for y in sorted(lookup[x]):
                report.extend(sorted(node.val for node in lookup[x][y]))
            result.append(report)
        return result
