# Time:  O(h)
# Space: O(1)

# 270
# Given a non-empty binary search tree and a target value, find the value in the BST that is
# closest to the target.
#
# Note:
# - Given target value is a floating point.
# - You are guaranteed to have only one unique value in the BST that is closest to the target.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        delta, ans = float('inf'), None
        while root:
            cur = abs(root.val - target)
            if cur < delta:
                delta, ans = cur, root.val
            if target == root.val:
                break
            elif target < root.val:
                root = root.left
            else:
                root = root.right
        return ans

r = TreeNode(4)
r.left, r.right = TreeNode(2), TreeNode(5)
r.left.left, r.left.right = TreeNode(1), TreeNode(3)
print(Solution().closestValue(r, 3.7)) # 4
print(Solution().closestValue(r, 3.2)) # 3
print(Solution().closestValue(r, 7.1)) # 5
print(Solution().closestValue(r, 1.2)) # 1
print(Solution().closestValue(r, -1.2)) # 1