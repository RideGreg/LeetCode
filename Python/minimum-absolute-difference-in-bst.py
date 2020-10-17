# Time:  O(n)
# Space: O(h)

# 530
# Given a binary search tree with non-negative values,
# find the minimum absolute difference between values of any two nodes.
#
# Example:
#
# Input:
#
#   1
#     \
#      3
#     /
#   2
#
# Output:
# 1
#
# Explanation:
# The minimum absolute difference is 1,
# which is the difference between 2 and 1 (or between 2 and 3).
# Note: There are at least two nodes in this BST.
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root): # USE THIS
        """
        :type root: TreeNode
        :rtype: int
        """
        stk, prev, ans = [(root, False)], float('-inf'), float('inf')
        while stk:
            node, visited = stk.pop()
            if node:
                if visited:
                    ans = min(ans, node.val - prev)
                    prev = node.val
                else:
                    stk.append((node.right, False))
                    stk.append((node, True))
                    stk.append((node.left, False))
        return ans


    # recursion
    def getMinimumDifference2(self, root): # use global variable
        def inorder(node):
            if node:
                inorder(node.left)
                self.result = min(self.result, node.val-self.prev)
                self.prev = node.val
                inorder(node.right)

        self.prev = float('-inf')
        self.result = float('inf')
        inorder(root)
        return self.result

    def getMinimumDifference3(self, root): # use parameter, hard to follow (need to change node)
        def inorderTraversal(root, prev, result):
            if not root:
                return (result, prev)

            result, prev = inorderTraversal(root.left, prev, result)
            result = min(result, root.val - prev)
            return inorderTraversal(root.right, root.val, result) # changed prev to root.val

        result, _ = inorderTraversal(root, float("-inf"), float("inf"))
        return result
