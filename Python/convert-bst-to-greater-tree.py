# Time:  O(n)
# Space: O(h)

# 538
# Given a Binary Search Tree (BST),
# convert it to a Greater Tree such that every key of
# the original BST is changed to the original key plus sum of
# all keys greater than the original key in BST.
#
# Example:
#
# Input: The root of a Binary Search Tree like this:
#               5
#             /   \
#           2     13
#
# Output: The root of a Greater Tree like this:
#              18
#             /   \
#           20     13

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def convertBST(self, root): # USE THIS
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def recur(root, addon):
            if not root:
                return addon

            addon = recur(root.right, addon)
            root.val += addon
            addon = recur(root.left, root.val)
            return addon

        recur(root, 0)
        return root

    def convertBST_globalVar(self, root):
        def traverse(node):
            if node:
                traverse(node.right)
                node.val += self.delta
                self.delta = node.val
                traverse(node.left)

        self.delta = 0
        traverse(root)
        return root

rt = TreeNode(5)
rt.left, rt.right = TreeNode(2), TreeNode(13)
ans = Solution().convertBST(rt)
print(ans)