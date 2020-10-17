# Time:  O(n)
# Space: O(1)

# 235
# Given a binary search tree (BST), find the lowest common ancestor (LCA)
# of two given nodes in the BST.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor
# is defined between two nodes v and w as the lowest node in T that has both v
# and w as descendants (where we allow a node to be a descendant of itself).”
#
#         _______6______
#       /              \
#     ___2__          ___8__
#   /      \        /      \
#   0      _4       7       9
#          /  \
#          3   5
# For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6.
# Another example is LCA of nodes 2 and 4 is 2, since a node can be a
# descendant of itself according to the LCA definition.
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):  # USE THIS
        while (root.val - p.val) * (root.val - q.val) > 0:
            if root.val > p.val:
                root = root.left
            else:
                root = root.right
        # s <= root.val <= b.
        return root


    def lowestCommonAncestor_kamyu(self, root, p, q):
        s, b = min(p.val, q.val), max(p.val, q.val)
        while not s <= root.val <= b:
            # Keep searching since root is outside of [s, b].
            if root.val > b:
                root = root.left
            else:
                root = root.right
        # s <= root.val <= b.
        return root


    def lowestCommonAncestor_recursion(self, root, p, q):
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        return root