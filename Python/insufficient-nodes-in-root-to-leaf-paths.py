# Time:  O(n)
# Space: O(h)

# 1080
# Given the root of a binary tree, consider all root to leaf paths.
#
# A node is insufficient if every such root to leaf path intersecting this node
# has sum strictly less than limit.
#
# Delete all insufficient nodes simultaneously, and return the root of the resulting binary tree.

# 二叉树中的一个结点要被删除，有两种办法：
# 1. 自己删除自己；
# 2. 告诉父亲结点，自己需要从二叉树中被删除。父亲结点收到孩子结点这个信号以后，只要把对孩子结点的引用切断即可。

# 二叉树的问题一定离不开遍历，遍历有 DFS 和 BFS，根据题目中的描述 “考虑它所有从根到叶的路径”，
# 就知道不能用 BFS 了，那么 DFS 又有 3 种, 本题要先考虑两个子结点，明显使用 “后序遍历”（从下到上）。

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sufficientSubset(self, root, limit):
        """
        :type root: TreeNode
        :type limit: int
        :rtype: TreeNode
        """
        # terminal condition
        if not root:
            return None
        if not root.left and not root.right:
            return None if root.val < limit else root

        # postorder
        root.left = self.sufficientSubset(root.left, limit-root.val)
        root.right = self.sufficientSubset(root.right, limit-root.val)
        if not root.left and not root.right:
            return None
        return root

rt = TreeNode(1)
rt.left, rt.right = TreeNode(2), TreeNode(-3)
rt.left.left, rt.right.left = TreeNode(-5), TreeNode(4)
print(Solution().sufficientSubset(rt, -1)) # [1, None, -3, 4]

