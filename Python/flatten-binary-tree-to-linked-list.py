# Time:  O(n)
# Space: O(h), h is height of binary tree

# 114
# Given a binary tree, flatten it to a linked list in-place.
#
# (Flatten a binary tree to a fake "linked list" in pre-order traversal.
# Here we use the right pointer in TreeNode as the next pointer in ListNode.)
#
# For example,
# Given
#
#          1
#         / \
#        2   5
#       / \   \
#      3   4   6
# The flattened tree should look like:
#    1
#     \
#      2
#       \
#        3
#         \
#          4
#           \
#            5
#             \
#              6
#

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        self.flattenRecu(root, None)

    def flattenRecu(self, root, list_head):
        if root:
            list_head = self.flattenRecu(root.right, list_head)
            list_head = self.flattenRecu(root.left, list_head)
            root.right = list_head
            root.left = None
            return root
        else:
            return list_head

# modified postOrder (right->left->parent), maintain the 'tail' var (always update tail as current processed node)
class Solution2: # USE THIS
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        def postOrder(node):
            if node:
                postOrder(node.right)
                postOrder(node.left)
                node.right = self.tail
                node.left = None
                self.tail = node

        self.tail = None
        postOrder(root)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right = TreeNode(5)
    root.right.right = TreeNode(6)
    result = Solution().flatten(root)
    print result.val
    print result.right.val
    print result.right.right.val
    print result.right.right.right.val
    print result.right.right.right.right.val
    print result.right.right.right.right.right.val
