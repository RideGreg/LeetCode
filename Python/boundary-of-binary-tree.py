# Time:  O(n)
# Space: O(h)

# 545
# Given a binary tree, return the values of its boundary in anti-clockwise direction
# starting from root. Boundary includes left boundary, leaves, and right boundary
# in order without duplicate nodes.
#
# Left boundary is defined as the path from root to the left-most node. Right boundary
# is defined as the path from root to the right-most node. If the root doesn't have left
# subtree or right subtree, then the root itself is left boundary or right boundary.
# Note this definition only applies to the input binary tree, and not applies to any subtrees.
#
# The left-most node is defined as a leaf node you could reach when you always firstly
# travel to the left subtree if exists. If not, travel to the right subtree. Repeat until
# you reach a leaf node.
#
# The right-most node is also defined by the same way with left and right exchanged.

# Input:
#   1
#    \
#     2
#    / \
#   3   4
#
# Ouput:
# [1, 3, 4, 2]
#
# Explanation:
# The root doesn't have left subtree, so the root itself is left boundary.
# The leaves are node 3 and 4.
# The right boundary are node 1,2,4. Note the anti-clockwise direction means you should output reversed right boundary.
# So order them in anti-clockwise without duplicates and we have [1,3,4,2].
#
# Input:
#     ____1_____
#    /          \
#   2            3
#  / \          /
# 4   5        6
#    / \      / \
#   7   8    9  10
#
# Ouput:
# [1,2,4,7,8,9,10,6,3]
#
# Explanation:
# The left boundary are node 1,2,4. (4 is the left-most node according to definition)
# The leaves are node 4,7,8,9,10.
# The right boundary are node 1,3,6,10. (10 is the right-most node).
# So order them in anti-clockwise without duplicate nodes we have [1,2,4,7,8,9,10,6,3].

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def leftBoundary(root, nodes):
            # don't process leaf node, leaving to leaves() method
            if root and (root.left or root.right):
                nodes.append(root.val)
                if not root.left:         # only do 1 branch
                    leftBoundary(root.right, nodes)
                else:
                    leftBoundary(root.left, nodes)

        def rightBoundary(root, nodes):
            if root and (root.left or root.right):
                if not root.right:
                    rightBoundary(root.left, nodes)
                else:
                    rightBoundary(root.right, nodes)
                nodes.append(root.val)
    
        def leaves(root, nodes): # preorder
            if root:
                if not root.left and not root.right:
                    nodes.append(root.val)
                    return
                leaves(root.left, nodes)
                leaves(root.right, nodes)

        if not root:
            return []

        nodes = [root.val]
        leftBoundary(root.left, nodes)
        leaves(root.left, nodes)
        leaves(root.right, nodes)
        rightBoundary(root.right, nodes)
        return nodes

r = TreeNode(1)
r.left, r.right = TreeNode(2), TreeNode(3)
r.left.left, r.left.right = TreeNode(4), TreeNode(5)
r.left.right.left, r.left.right.right = TreeNode(7), TreeNode(8)
r.right.left = TreeNode(6)
r.right.left.left, r.right.left.right = TreeNode(9), TreeNode(10)
print(Solution().boundaryOfBinaryTree(r))