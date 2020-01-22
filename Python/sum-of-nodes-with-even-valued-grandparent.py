# Time:  O(n)
# Space: O(h)

# 1315 biweekly contest 17 1/11/2020

# Given a binary tree, return the sum of values of nodes with even-valued grandparent.  (A grandparent of a node
# is the parent of its parent, if it exists.)
#
# If there are no nodes with an even-valued grandparent, return 0.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def sumEvenGrandparentHelper(root, p, gp):
            return sumEvenGrandparentHelper(root.left, root.val, p) + \
                   sumEvenGrandparentHelper(root.right, root.val, p) + \
                   (root.val if gp is not None and gp % 2 == 0 else 0) if root else 0

        return sumEvenGrandparentHelper(root, None, None)

    def sumEvenGrandparent_ming(self, root: TreeNode) -> int:
        def dfs(node, p, pp):
            if not node:
                return 0
            ans = node.val if pp and pp % 2 == 0 else 0
            ans += dfs(node.left, node.val, p)
            ans += dfs(node.right, node.val, p)
            return ans

        return dfs(root, None, None)

r=TreeNode(6)
r.left, r.right = TreeNode(7), TreeNode(8)
r.left.left, r.left.right = TreeNode(2), TreeNode(7)
r.right.left, r.right.right = TreeNode(1), TreeNode(3)
print(Solution().sumEvenGrandparent(r))

