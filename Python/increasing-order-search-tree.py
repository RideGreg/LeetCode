# Time:  O(n)
# Space: O(h)

# 897
# Given a binary search tree, rearrange the tree in "in-order" so that the leftmost node
# in the tree is now the root of the tree, and every node has no left child and only 1 right child.
#
# Example 1:
# Input: [5,3,6,2,4,null,8,1,null,null,null,7,9]
#
#        5
#       / \
#     3    6
#    / \    \
#   2   4    8
#  /        / \ 
# 1        7   9
#
# Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
#
#  1
#   \
#    2
#     \
#      3
#       \
#        4
#         \
#          5
#           \
#            6
#             \
#              7
#               \
#                8
#                 \
#                  9  
# Note:
# - The number of nodes in the given tree will be between 1 and 100.
# - Each node will have a unique integer value from 0 to 1000.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def increasingBST(self, root): # USE THIS
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def inorder(node):
            if node:
                inorder(node.left)

                self.cur.right = node
                self.cur = self.cur.right
                node.left = None #left visited and no longer needed. If don't disconnect left, cycle is formed

                inorder(node.right)

        self.cur = head = TreeNode(-1)
        inorder(root)
        return head.right

    # yield not take new space, but create many new nodes
    def increasingBST_yield(self, root):
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)

        ans = cur = TreeNode(None)
        for v in inorder(root):
            cur.right = TreeNode(v)
            cur = cur.right
        return ans.right


    # hard to understand: result is obtained, then continue to modify the tree.
    def increasingBST_kamyu(self, root):
        def increasingBSTHelper(root, tail):
            if not root:
                return tail
            result = increasingBSTHelper(root.left, root)
            root.left = None
            root.right = increasingBSTHelper(root.right, tail)
            return result
        return increasingBSTHelper(root, None)

root=TreeNode(5)
root.left, root.right = TreeNode(3), TreeNode(6)
root.left.right = TreeNode(4)
print(Solution().increasingBST(root))