# Time:  O(n)
# Space: O(h)

# 637
# Given a non-empty binary tree,
# return the average value of the nodes on each level in the form of
# an array.
#
# Example 1:
# Input:
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Output: [3, 14.5, 11]
# Explanation:
# The average value of nodes on level 0 is 3,
# on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
#
# Note:
# The range of node's value is in the range of 32-bit signed integer.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

try:
    xrange          # Python 2
except NameError:
    xrange = range  # Python 3


class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        def preorder(node, dep):
            if node:
                if dep == len(levelsum):
                    levelsum.append(node.val)
                    cnt.append(1)
                else:
                    levelsum[dep] += node.val
                    cnt[dep] += 1
                preorder(node.left, dep+1)
                preorder(node.right, dep+1)

        levelsum, cnt = [], []
        preorder(root, 0)
        return [levelsum[i]/cnt[i] for i in range(len(cnt))]

    # level order: next_q may need 2^h space
    def averageOfLevels_kamyu(self, root):
        result = []
        q = [root]
        while q:
            total, count = 0, 0
            next_q = []
            for n in q:
                total += n.val
                count += 1
                if n.left:
                    next_q.append(n.left)
                if n.right:
                    next_q.append(n.right)
            q = next_q
            result.append(total / count)
        return result
