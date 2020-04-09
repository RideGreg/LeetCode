# Time:  O(n)
# Space: O(n)

# 663
# Given a binary tree with n nodes, your task is to check if it's possible to partition the tree to two trees
# which have the equal sum of values after removing exactly one edge on the original tree.
# - The range of tree node value is in the range of [-100000, 100000].

# Input:
#     5
#    / \
#   10 10
#     /  \
#    2   3
# Output: True. Explanation:
#  5
# /
# 10
#
#  10
# /  \
# 2   3
#
# Sum: 15

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections


class Solution(object):
    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def getSumHelper(node):
            if not node:
                return 0
            total = node.val + \
                    getSumHelper(node.left) + \
                    getSumHelper(node.right)
            lookup[total] += 1
            return total

        lookup = collections.defaultdict(int)
        total = getSumHelper(root)
        if total == 0:
            return lookup[total] > 1
        return total%2 == 0 and (total//2) in lookup
