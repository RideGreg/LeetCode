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
    # TRAVERSE ONCE, SEGMENT ALL NODES
    def verticalTraversal(self, root): # USE THIS: 2 sorting: x, (y, val). Put y, val in tuple, one sort can do both.
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def dfs(node, x, y):
            if node:
                lookup[x].append((y, node.val))
                dfs(node.left, x - 1, y + 1)
                dfs(node.right, x + 1, y + 1)

        lookup = collections.defaultdict(list)
        dfs(root, 0, 0)
        ans = []
        for x in sorted(lookup):
            ans.append([v for _, v in sorted(lookup[x])])
        return ans

    # 3 sorting needed: x, y, val. The results from sorting y & val still need to be assembled.
    def verticalTraversal_LeetcodeOfficial(self, root):
        def dfs(node, x, y):
            if node:
                lookup[x][y].append(node.val)
                dfs(node.left, x-1, y+1)
                dfs(node.right, x+1, y+1)
                
        lookup = collections.defaultdict(lambda: collections.defaultdict(list))
        dfs(root, 0, 0)

        result = []
        for x in sorted(lookup):
            report = []
            for y in sorted(lookup[x]):
                report.extend(sorted(lookup[x][y]))
            result.append(report)
        return result

    # best space complexity, no need temporary list for middle values. Need multiple traversal.
    # Maybe better time complexity, minimal sorting required.
    # Note: actually not really need to know the number of each column.
    def verticalTraversal2(self, root):
        # preorder traversal to get min/max column ids
        def getMinMaxCol(node, c):
            if node:
                minmax[0] = min(minmax[0], c)
                minmax[1] = max(minmax[1], c)
                getMinMaxCol(node.left, c-1)
                getMinMaxCol(node.right, c+1)
        minmax = [float('inf'), float('-inf')]
        getMinMaxCol(root, 0)
        ans = [[] for _ in range(minmax[0], minmax[1]+1)]

        # level order traversal: save the sort of row numbers.
        level = [(root, -minmax[0])]
        while level:
            tmp, level2 = collections.defaultdict(list), []
            for node, c in level:
                tmp[c].append(node.val)
                if node.left:
                    level2.append((node.left, c-1))
                if node.right:
                    level2.append((node.right, c+1))
            for c in tmp:
                ans[c].extend(sorted(tmp[c]))
            level = level2
        return ans

r = TreeNode(3)
r.left, r.right = TreeNode(9), TreeNode(20)
r.right.left, r.right.right = TreeNode(15), TreeNode(7)
print(Solution().verticalTraversal(r)) # [[9],[3,15],[20],[7]]