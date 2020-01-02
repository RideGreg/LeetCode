# Time:  O(n)
# Space: O(h + d), d is the number of to_delete

# 1110 weekly contest 144 7/6/2019
# Given the root of a binary tree, each node in the tree has a distinct value.
#
# After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).
#
# Return the roots of the trees in the remaining forest.  You may return the result in any order.
#
# The # of nodes in the given tree is at most 1000.
# Each node has a distinct value between 1 and 1000.
# to_delete.length <= 1000
# to_delete contains distinct values between 1 and 1000.

# Definition for a binary tree node.
from typing import List
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

        
class Solution(object):
    def delNodes(self, root, to_delete): # USE THIS: append current node
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        def preorder(cur, is_root):
            if not cur:
                return None
            is_deleted = cur.val in to_delete_set
            if is_root and not is_deleted:
                ans.append(cur)
            cur.left = preorder(cur.left, is_deleted)
            cur.right = preorder(cur.right, is_deleted)
            return None if is_deleted else cur
        
        ans = []
        to_delete_set = set(to_delete)
        preorder(root, True)
        return ans

    # solution 2: append children nodes, and set parent's child node link.
    def delNodes_ming(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        def preorder(cur, p, dir):
            if cur:
                if cur.val in delete:
                    if cur.left and cur.left.val not in delete:
                        ans.append(cur.left)
                    if cur.right and cur.right.val not in delete:
                        ans.append(cur.right)
                    if dir is 'l':
                        p.left = None
                    elif dir is 'r':
                        p.right = None

                preorder(cur.left, cur, 'l')
                preorder(cur.right, cur, 'r')

        delete = set(to_delete)
        ans = []
        if root.val not in delete:
            ans.append(root)
        preorder(root, None, None)
        return ans

for delete in ([3,5], [2,3], [5,6], [1], [1,2], [1,6]):
    r = TreeNode(1)
    r.left, r.right = TreeNode(2), TreeNode(3)
    r.left.left, r.left.right = TreeNode(4), TreeNode(5)
    r.right.left, r.right.right = TreeNode(6), TreeNode(7)

    print(Solution().delNodes(r, delete))
    # [[1,2,null,4], [6], [7]]
    #[[1], [4], [5], [6], [7]]
    #[[1,2,3,4,null,null,7]]
    #[[2,4,5], [3,6,7]]
    #[[3,6,7], [4], [5]]
    #[[2,4,5], [3,7]]