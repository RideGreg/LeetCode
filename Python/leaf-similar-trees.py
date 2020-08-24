# Time:  O(n)
# Space: O(h)

# 872
# Consider all the leaves of a binary tree.
# From left to right order,
# the values of those leaves form a leaf value sequence.
#
# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
# Two binary trees are considered leaf-similar if their leaf value sequence is the same.
# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
#
# Note:
# - Both of the given trees will have between 1 and 100 nodes.

import itertools


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # build tree1 from left to right, check tree2 from right to left, so no need to 
    # maintain the index in leaves sequence.
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool: # USE THIS
        def build(root):
            if root:
                if not root.left and not root.right:
                    leaves.append(root.val)
                else:
                    build(root.left)
                    build(root.right)

        def check(root):
            if root:
                if not root.left and not root.right:
                    if not leaves or root.val != leaves[-1]:
                        return False
                    leaves.pop()
                else:
                    if not check(root.right) or not check(root.left):
                        return False
            return True

        leaves = []
        build(root1)
        return check(root2)


class Solution2(object):
    def leafSimilar(self, root1, root2): # have to produce both full leaves sequence
        def getLeaf(root, seq):
            if not root: return seq
            if not root.left and not root.right:
                seq.append(root.val)
                return seq

            seq = getLeaf(root.left, seq)
            seq = getLeaf(root.right, seq)
            return seq

        return getLeaf(root1, []) == getLeaf(root2, [])

    def leafSimilar_LeetCodeOfficial(self, root1, root2): # USE iterator
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def dfs(node):
            if node:
                if not node.left and not node.right:
                    yield node.val
                for i in dfs(node.left):
                    yield i
                for i in dfs(node.right):
                    yield i
        return all(a == b for a, b in
                   itertools.izip_longest(dfs(root1), dfs(root2)))
        # or return list(dfs(root1)) == list(dfs(root2))
