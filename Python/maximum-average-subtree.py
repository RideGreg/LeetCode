# Time:  O(n)
# Space: O(h)

# 1120
# Given the root of a binary tree, find the maximum average value of any subtree of that tree.
#
# (The average value of a tree is the sum of its values, divided by the number of nodes.)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maximumAverageSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: float
        """
        def postorder(root):
            if not root:
                return [0.0, 0]
            s1, n1 = postorder(root.left)
            s2, n2 = postorder(root.right)
            s = s1+s2+root.val
            n = n1+n2+1
            result[0] = max(result[0], s / n)
            return [s, n]

        result = [0]
        postorder(root)
        return result[0]

root = TreeNode(25)
root.left, root.right = TreeNode(6), TreeNode(1)
print(Solution().maximumAverageSubtree(root)) # 10.666
