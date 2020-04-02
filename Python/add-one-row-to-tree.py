# Time:  O(n)
# Space: O(h)

# Given the root of a binary tree, then value v and depth d,
# you need to add a row of nodes with value v at the given depth d.
# The root node is at depth 1.
#
# The adding rule is: given a positive integer depth d,
# for each NOT null tree nodes N in depth d-1, create two tree nodes
# with value v as N's left subtree root and right subtree root.
# And N's original left subtree should be the left subtree of
# the new left subtree root,
# its original right subtree should be the right subtree of
# the new right subtree root.
# If depth d is 1 that means there is no depth d-1 at all,
# then create a tree node with value v as the new root of
# the whole original tree,
# and the original tree is the new root's left subtree.
#
# Example 1:
# Input:
# A binary tree as following:
#        4
#      /   \
#     2     6
#    / \   /
#   3   1 5
#
# v = 1
#
# d = 2
#
# Output:
#        4
#       / \
#      1   1
#     /     \
#    2       6
#   / \     /
#  3   1   5
#
# Example 2:
# Input:
# A binary tree as following:
#       4
#      /
#     2
#    / \
#   3   1
#
# v = 1
#
# d = 3
#
# Output:
#       4
#      /
#     2
#    / \
#   1   1
#  /     \
# 3       1
# Note:
# 1. The given d is in range [1, maximum depth of the given tree + 1].
# 2. The given binary tree has at least one tree node.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def addOneRow(self, root, v, d): # USE THIS: tricky, good space complexity
        def preOrder(root, d, dir):
            if d == 1:
                node = TreeNode(v)
                if dir == 'l':
                    node.left = root
                else:
                    node.right = root
                return node

            if root: # None node directly return None for parent node
                root.left = preOrder(root.left, d-1, 'l')
                root.right = preOrder(root.right, d-1, 'r')
            return root

        return preOrder(root, d, 'l')

    def addOneRow_badSpaceComplexity(self, root, v, d): # easy to understand, bad space complexity O(2^h)
        if d == 1:
            ans = TreeNode(v)
            ans.left = root
            return ans

        nodes, dep = [root], 1
        while dep < d-1:
            nodes = [y for x in nodes for y in (x.left, x.right) if y]
            dep += 1
        for x in nodes:
            l, r = x.left, x.right
            x.left, x.right = TreeNode(v), TreeNode(v)
            x.left.left = l
            x.right.right = r
        return root