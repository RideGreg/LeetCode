# Time:  O(n)
# Space: O(n)

# We are given a binary tree (with root node root), a target node,
# and an integer value `K`.
#
# Return a list of the values of all nodes that have a distance K
# from the target node.  The answer can be returned in any order.
#
# Example 1:
#
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
# Output: [7,4,1]
# Explanation:
# The nodes that are a distance 2 from the target node (with value 5)
# have values 7, 4, and 1.
#
# Note that the inputs "root" and "target" are actually TreeNodes.
# The descriptions of the inputs above are
# just serializations of these objects.
#
# Note:
# - The given tree is non-empty.
# - Each node in the tree has unique values 0 <= node.val <= 500.
# - The target node is a node in the tree.
# - 0 <= K <= 1000.
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections

try:
    xrange          # Python 2
except NameError:
    xrange = range  # Python 3


class Solution(object):
    def distanceK_kamyu(self, root, target, K): # Space not good: extra space neighbors
                                                # ok to use node value since values are unique
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        def dfs(parent, node):
            if node:
                if parent:
                    neighbors[parent.val].append(node.val)
                    neighbors[node.val].append(parent.val)
                dfs(node, node.left)
                dfs(node, node.right)

        neighbors = collections.defaultdict(list)
        dfs(None, root)
        bfs = [target.val]
        lookup = set(bfs)
        for _ in xrange(K):
            bfs = [nei for node in bfs
                   for nei in neighbors[node]
                   if nei not in lookup]
            lookup |= set(bfs)
        return bfs

    def distanceK(self, root, target, K): # USE THIS
        def dfs(node, par):
            if node:
                parent[node] = par
                dfs(node.left, node)
                dfs(node.right, node)

        parent = {}
        dfs(root, None)
        bfs, seen = [target], {target}
        for _ in xrange(K):
            bfs = [nei for n in bfs for nei in (n.left, n.right, parent[n]) if nei and nei not in seen]
            seen |= set(bfs)
        return [n.val for n in bfs]

root = TreeNode(3)
root.left, root.right = TreeNode(5), TreeNode(1)
root.left.left, root.left.right = TreeNode(6), TreeNode(2)
root.left.right.left, root.left.right.right = TreeNode(7), TreeNode(4)
root.right.left, root.right.right = TreeNode(0), TreeNode(8)

print(Solution().distanceK(root, root.left, 0))
print(Solution().distanceK(root, root.left, 1))
print(Solution().distanceK(root, root.left, 2))
print(Solution().distanceK(root, root.left, 3))
print(Solution().distanceK(root, root.left, 4))
print(Solution().distanceK(root, root.left, 50))
