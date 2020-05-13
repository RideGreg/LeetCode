# Time:  O(h)
# Space: O(1)

# 998
# We are given the root node of a maximum tree: a tree where every node has a value greater than
# any other value in its subtree.
#
# Just as in the previous problem, the given tree was constructed from an list A (root = Construct(A))
# recursively with the following Construct(A) routine:
#
# If A is empty, return null.
# Otherwise, let A[i] be the largest element of A.  Create a root node with value A[i].
# The left child of root will be Construct([A[0], A[1], ..., A[i-1]])
# The right child of root will be Construct([A[i+1], A[i+2], ..., A[A.length - 1]])
# Return root.
# Note that we were not given A directly, only a root node root = Construct(A).
#
# Suppose B is a copy of A with the value val appended to it.  It is guaranteed that B has unique values.
#
# Return Construct(B).

# Input: root = [4,1,3,null,null,2], val = 5
# Output: [5,4,null,1,3,null,null,2]
# Explanation: A = [1,4,2,3], B = [1,4,2,3,5]

# Input: root = [5,2,4,null,1], val = 3
# Output: [5,2,4,null,1,null,3]
# Explanation: A = [2,1,5,4], B = [2,1,5,4,3]

# Input: root = [5,2,3,null,1], val = 4
# Output: [5,2,4,null,1,3]
# Explanation: A = [2,1,5,3], B = [2,1,5,3,4]

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # 扫描右子树的所有根节点，找到插入位置
    # Search on the right, find the node that cur.val > val > cur.right.val
    # put old cur.right as node.left, put node as new cur.right.

    # use only 1 pointer curr, use dummy node for edge case
    def insertIntoMaxTree(self, root, val): # USE THIS
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        dummy = TreeNode(float('inf'))
        dummy.right = root
        curr = dummy
        while curr.right and curr.right.val > val:
            curr = curr.right

        node = TreeNode(val)
        node.left = curr.right
        curr.right = node
        return dummy.right

    # use 2 pointers cur, par; but don't need special handle edge case
    def insertIntoMaxTree2(self, root, val):
        node = TreeNode(val)
        cur, par = root, None
        while cur and cur.val > val:
            par = cur
            cur = cur.right

        node.left = cur
        if par:
            par.right = node
            return root
        else:
            return node

    # recursion: Time O(h), Space O(h)
    # If root.val > val, recusion on the right.
    # Else, put right subtree on the left of new node TreeNode(val)
    def insertIntoMaxTree_recursion(self, root, val):
        if root and root.val > val:
            root.right = self.insertIntoMaxTree(root.right, val)
            return root
        node = TreeNode(val)
        node.left = root
        return node