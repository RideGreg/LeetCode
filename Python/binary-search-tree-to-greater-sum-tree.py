# Time:  O(n)
# Space: O(h)

# 1038
# Given the root of a binary search tree with distinct values, modify it so that every node has a
# new value equal to the sum of the values of the original tree that are greater than or equal to node.val.
#
# As a reminder, a binary search tree is a tree that satisfies these constraints:
#
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Example:
#       4                       30
#   1       6       =>     36        21
# 0  2    5  7           36 35     26  15
#     3       8              33          8
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def bstToGst(self, root): # USE THIS
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def postOrder(n, summ):
            if not n:
                return summ
            nsm = postOrder(n.right, summ)
            n.val += nsm
            return postOrder(n.left, n.val)

        postOrder(root, 0)
        return root

    def bstToGst_globalVar(self, root):
        def bstToGstHelper(root):
            if not root:
                return root
            bstToGstHelper(root.right)
            self.prev = root.val = root.val + self.prev
            bstToGstHelper(root.left)
            return root
        
        self.prev = 0
        return bstToGstHelper(root)


root=TreeNode(4)
root.left, root.right = TreeNode(1), TreeNode(6)
root.left.left, root.left.right = TreeNode(0), TreeNode(2)
root.right.left, root.right.right = TreeNode(5), TreeNode(7)
root = Solution().bstToGst(root)
print(root.val) # 22