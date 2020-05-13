# Time:  O(n)
# Space: O(h)

# 1325 weekly contest 172 1/18/2020

# Given a binary tree root and an integer target, delete all the leaf nodes with value target.
#
# Note that once you delete a leaf node with value target, if it's parent node becomes a leaf node and has
# the value target, it should also be deleted (you need to continue doing that until you can't).

# 1 <= target <= 1000
# Each tree has at most 3000 nodes.
# Each node's value is between [1, 1000].

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def removeLeafNodes(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        """
        if not root:
            return None
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        return None if root.left == root.right and root.val == target else root
        # 技巧：root.left == root.right 等同于 not root.left and not root.right

    def removeLeafNodes_ming(self, root: TreeNode, target: int) -> TreeNode:
        def postorder(cur):
            if not cur:
                return None

            cur.left = postorder(cur.left)
            cur.right = postorder(cur.right)
            if not cur.left and not cur.right and cur.val == target:
                return None
            else:
                return cur

        return postorder(root)


r = TreeNode(1)
r.left, r.right = TreeNode(3), TreeNode(3)
r.left.left, r.left.right = TreeNode(3), TreeNode(2)
ans = Solution().removeLeafNodes(r, 3)

r = TreeNode(1)
r.left = TreeNode(2)
r.left.left = TreeNode(2)
r.left.left.left = TreeNode(2)

ans = Solution().removeLeafNodes(r, 2)

r = TreeNode(1)
r.left, r.right = TreeNode(1), TreeNode(1)
ans = Solution().removeLeafNodes(r, 1)

r = TreeNode(1)
r.left, r.right = TreeNode(2), TreeNode(3)
ans = Solution().removeLeafNodes(r, 1)