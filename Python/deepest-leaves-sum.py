# Time:  O(n)
# Space: O(w)

# 1302 biweekly contest 16 12/28/2019

# Given a binary tree, return the sum of values of its deepest leaves.

# Constraints:
# The number of nodes in the tree is between 1 and 10^4.
# The value of nodes is between 1 and 100.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        curr = [root]
        while curr:
            prev, curr = curr, [child for p in curr for child in [p.left, p.right] if child]
        return sum(node.val for node in prev)

print(Solution().deepestLeavesSum([1,2,3,4,5,null,6,7,null,null,null,null,8])) # 15