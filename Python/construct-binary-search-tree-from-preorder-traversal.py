# Time:  O(n)
# Space: O(h)

# 1008
# Return the root node of a binary search tree that matches the given preorder traversal.
#
# (Recall that a binary search tree is a binary tree where for every node, any descendant of
# node.left has a value < node.val, and any descendant of node.right has a value > node.val.
# Also recall that a preorder traversal displays the value of the node first, then traverses
# node.left, then traverses node.right.)

# Input: [8,5,1,7,10,12]
# Output: [8,5,10,1,7,null,12]

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def bstFromPreorder(self, preorder): # USE THIS: easy to remember Time: hlogn, worse nlogn
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        import bisect
        def build(i, j):
            if i >= j: return None
            node = TreeNode(preorder[i])
            k = bisect.bisect(preorder, preorder[i], i, j)
            node.left = build(i+1, k)
            node.right = build(k, j)
            return node
        return build(0, len(preorder))

    def bstFromPreorder_newList(self, preorder):
        import bisect
        if not preorder:
            return None
        node = TreeNode(preorder[0])
        k = bisect.bisect(preorder, preorder[0])
        node.left = self.bstFromPreorder(preorder[1:k])
        node.right = self.bstFromPreorder(preorder[k:])
        return node

    def bstFromPreorder_bound(self, preorder): # faster, use BST bound, not easy to remember
        def rec(leftBound, rightBound):
            if self.i == len(preorder) or \
               preorder[self.i] < leftBound or \
               preorder[self.i] > rightBound:
                return None

            root = TreeNode(preorder[self.i])
            self.i += 1
            root.left = rec(leftBound, root.val)
            root.right = rec(root.val, rightBound)
            return root

        self.i = 0
        return rec(float("-inf"), float("inf"))
