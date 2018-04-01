# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDiffInBST(self, root):
        self.ans = float("inf")

        def helper(root, prev):
            if not root:
                return prev
            prev = helper(root.left, prev)
            if abs(prev - root.val) < self.ans:
                self.ans = abs(prev - root.val)
            prev = root.val
            prev = helper(root.right, prev)
            return prev

        helper(root, float('inf'))
        return self.ans

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

print Solution().minDiffInBST(root)