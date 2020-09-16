# Time:  O(h)
# Space: O(h)

# 450
# Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.
#
# Basically, the deletion can be divided into two stages:
#
# Search for a node to remove.
# If the node is found, delete the node.
# Note: Time complexity should be O(height of tree).

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __repr__(self):
        return "{}->{}->{}".format(self.val, self.left, self.right)

class Solution(object):
    def deleteNode(self, root, key): # USE THIS: best, in some cases, just shift the sub-tree, no need to swap value
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root: return root

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                right = root.right
                del root
                return right
            elif not root.right:
                left = root.left
                del root
                return left
            else:
                # find successor
                successor = root.right
                while successor.left:
                    successor = successor.left

                root.val = successor.val # swap
                root.right = self.deleteNode(root.right, successor.val)

        return root

class Solution:
    def successor(self, root):
        # One step right and then always left
        root = root.right
        while root.left:
            root = root.left
        return root.val

    def predecessor(self, root):
        # One step left and then always right
        root = root.left
        while root.right:
            root = root.right
        return root.val

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root: return None

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            # the node is a leaf
            if not (root.left or root.right):
                root = None
            elif root.right:
                root.val = self.successor(root) # swap
                root.right = self.deleteNode(root.right, root.val)
            else:
                root.val = self.predecessor(root) # swap
                root.left = self.deleteNode(root.left, root.val)

        return root


rt = TreeNode(1)
rt.right = TreeNode(2)
print(Solution().deleteNode(rt, 2)) # 1->None->None
#       10
#    5     15
#  2   7
#   4 6

rt = TreeNode(10)
rt.left, rt.right = TreeNode(5), TreeNode(15)
rt.left.left, rt.left.right = TreeNode(2), TreeNode(7)
rt.left.left.right = TreeNode(4)
rt.left.right.left = TreeNode(6)
print(Solution().deleteNode(rt, 2)) # 10->5->4->None->None->7->6->None->None->None->15->None->None

rt = TreeNode(10)
rt.left, rt.right = TreeNode(5), TreeNode(15)
rt.left.left, rt.left.right = TreeNode(2), TreeNode(7)
rt.left.left.right = TreeNode(4)
rt.left.right.left = TreeNode(6)
print(Solution().deleteNode(rt, 7)) # 10->5->2->None->4->None->None->6->None->None->15->None->None
