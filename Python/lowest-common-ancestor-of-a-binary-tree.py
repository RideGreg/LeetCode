# Time:  O(n)
# Space: O(h)
# 236
# Given a binary tree, find the lowest common ancestor (LCA)
# of two given nodes in the tree.
#
# According to the definition of LCA on Wikipedia: “The lowest
# common ancestor is defined between two nodes v and w as the
# lowest node in T that has both v and w as descendants (where we
# allow a node to be a descendant of itself).”
#
#         _______3______
#       /              \
#     ___5__          ___1__
#   /      \        /      \
#   6      _2       0       8
#          /  \
#          7   4
# For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3.
# Another example is LCA of nodes 5 and 4 is 5, since a node can be a
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
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None
        if root in (p, q): # 不可能走更低拿LCA
            return root

        # 1. If the left and right subtrees contain p and q separately,
        #    return current node as LCA.
        # 2. If only one subtree contains p or q, return that subtree.
        # 3. If neither subtree, return None.
        l, r = self.lowestCommonAncestor(root.left, p, q), \
               self.lowestCommonAncestor(root.right, p, q)
        if l and r:
            return root
        return l or r

    # 用哈希表存储父节点。从p向上移，记录经过的节点。再从q向上移，第一个共同点即为返回值。
    def lowestCommonAncestor2(self, root, p, q):
        def dfs(n, p):
            if n:
                par[n] = p
                dfs(n.left, n)
                dfs(n.right, n)

        par, visited = {}, set()
        dfs(root, None)
        while p in par:
            visited.add(p)
            p = par[p]
        while q not in visited:
            q = par[q]
        return q


