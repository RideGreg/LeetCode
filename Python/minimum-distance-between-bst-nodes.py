# Time:  O(n)
# Space: O(h)

# 783
# Given a Binary Search Tree (BST) with the root node root,
# return the minimum difference between the values of any two different nodes in the tree.
#
# Example :
#
# Input: root = [4,2,6,1,3,null,null]
# Output: 1
# Explanation:
# Note that root is a TreeNode object, not an array.
#
# The given tree [4,2,6,1,3,null,null] is represented by the following diagram:
#
#           4
#         /   \
#       2      6
#      / \
#     1   3
#
# while the minimum difference in this tree is 1,
# it occurs between node 1 and node 2, also between node 3 and node 2.
#
# Note:
# - The size of the BST will be between 2 and 100.
# - The BST is always valid, each node's value is an integer, and each node's value is different.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDiffInBST(self, root):
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

