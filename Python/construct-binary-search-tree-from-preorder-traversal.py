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
    # solution 2 creates 'inorder' list which doesn't provide extra info but triggers O(nlogn), thus time
    # complexity can be further optimized.
    # Maintain a counter self.i to build node one by one in preorder traverse manner, maintain a pair
    # [leftBound, rightBound] to divert to left or right subtree.
    def bstFromPreorder_bound(self, preorder): # USE THIS: use BST bound, not easy to remember
        def rec(leftBound, rightBound):
            if self.i == len(preorder) or \
               preorder[self.i] < leftBound or preorder[self.i] > rightBound: # 值脱离预期范围，不可能建子树节点，回溯到父节点
                return None

            root = TreeNode(preorder[self.i])
            self.i += 1
            root.left = rec(leftBound, root.val)
            root.right = rec(root.val, rightBound)
            return root

        self.i = 0
        return rec(float("-inf"), float("inf"))

    # solution 2: inorder = sorted(preorder), build tree using preorder+inorder.
    # Time O(nlogn), where sorting nlogn, build tree O(n); Space O(n)


    # WRONG: bisect used bisection algorithm on a SORTED list! Apply bisect on unsorted 'preorder' is not
    # guaranteed if 'preorder' is not balanced!
    def bstFromPreorder(self, preorder):
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

    # WRONG: bisect used bisection algorithm on a SORTED list!
    def bstFromPreorder_newList(self, preorder):
        import bisect
        if not preorder:
            return None
        node = TreeNode(preorder[0])
        k = bisect.bisect(preorder, preorder[0])
        node.left = self.bstFromPreorder(preorder[1:k])
        node.right = self.bstFromPreorder(preorder[k:])
        return node
