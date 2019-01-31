# Time:  O(n)
# Space: O(h)

# 965
# A binary tree is univalued if every node in the tree has the same value.
# Return true if and only if the given tree is univalued.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        s = [root]
        while s:
            node = s.pop()
            if not node:
                continue
            if node.val != root.val:
                return False
            s.append(node.left)
            s.append(node.right)
        return True

    # A tree is univalued if both its children are univalued, plus the root node has the same value as the child nodes.
    def isUnivalTree_ming(self, root):
        def preorder(root, v):
            if not root:
                return True
            return root.val == v and preorder(root.left, v) and preorder(root.right, v)

        return preorder(root, root.val)

# Time:  O(n)
# Space: O(h)
class Solution2(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return (not root.left or (root.left.val == root.val and self.isUnivalTree(root.left))) and \
               (not root.right or (root.right.val == root.val and self.isUnivalTree(root.right)))
