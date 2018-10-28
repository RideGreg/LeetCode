# Time:  O(n)
# Space: O(h), h is height of binary tree
#
# Given a binary tree, find the maximum path sum.
#
# The path may start and end at any node in the tree.
#
# For example:
# Given the below binary tree,
#
#        1
#       / \
#      2   3
# Return 6.
#


# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    maxSum = float("-inf")

    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        self.maxPathSumRecu(root)
        return self.maxSum

    def maxPathSumRecu(self, root):
        if root is None:
            return 0
        left = max(0, self.maxPathSumRecu(root.left))
        right = max(0, self.maxPathSumRecu(root.right))
        self.maxSum = max(self.maxSum, root.val + left + right)
        return root.val + max(left, right)

# not use global var, pass/update the var in recursion
class Solution_passReturnVal(object):
    def maxPathSum(self, root):
        def getMax(node, ans):
            if not node: return (ans, 0)
            ans, leftM = getMax(node.left, ans)
            ans, rightM = getMax(node.right, ans)
            cur = node.val + max(0, leftM) + max(0, rightM)
            ans = max(ans, cur)
            return (ans, node.val+max(0, leftM, rightM))
        
        return getMax(root, float('-inf'))[0] if root else 0