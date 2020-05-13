# Time:  O(n)
# Space: O(h)

# 814
# We are given the head node root of a binary tree,
# where additionally every node's value is either a 0 or a 1.
#
# Return the same tree where every subtree (of the given tree)
# not containing a 1 has been removed.
#
# (Recall that the subtree of a node X is X,
#  plus every node that is a descendant of X.)
#
# Example 1:
# Input: [1,null,0,0,1]
# Output: [1,null,0,null,1]
#
# Explanation:
# Only the red nodes satisfy the property "every subtree not containing a 1".
# The diagram on the right represents the answer.
#
# Example 2:
# Input: [1,0,1,0,0,0,1]
# Output: [1,null,1,null,1]
#
# Example 3:
# Input: [1,1,0,1,1,0,1,0]
# Output: [1,1,0,1,1,null,1]
#
# Note:
# - The binary tree will have at most 100 nodes.
# - The value of each node will only be 0 or 1.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __repr__(self):
        return "{} {} {}".format(self.val, self.left, self.right) \
            if self.left or self.right else "{}".format(self.val)


class Solution(object):
    def pruneTree(self, root): # USE THIS
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if not root.left and not root.right and root.val == 0:
            return None
        return root

    def pruneTree_ming(self, root: TreeNode) -> TreeNode: # bad/tedious: return True/Node/None, then set children
        def dfs(node):
            if not node:
                return None
            l, r = dfs(node.left), dfs(node.right)
            if not l: node.left = None
            if not r: node.right = None
            return node.val == 1 or l or r # return True, Node or None

        dfs(root)
        return root

root = TreeNode(1)
root.right = TreeNode(0)
root.right.left, root.right.right = TreeNode(0), TreeNode(1)
print(Solution().pruneTree(root))