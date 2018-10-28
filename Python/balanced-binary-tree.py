# Time:  O(n)
# Space: O(h), h is height of binary tree
#
# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as a binary
# tree
# in which the depth of the two subtrees of every node never differ by more
# than 1.
#


# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object): # USE THIS, but not easy to think
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        def getHeight(root):
            if root is None:
                return 0
            left_height, right_height = \
                getHeight(root.left), getHeight(root.right)
            if left_height < 0 or right_height < 0 or \
               abs(left_height - right_height) > 1:
                return -1
            return max(left_height, right_height) + 1
        return (getHeight(root) >= 0)

    def isBalanced_outputTwo(self, root): # USE THIS
        def getHeight(root):
            if not root: return (True, 0)
            leftOk, leftH = getHeight(root.left)
            rightOk, rightH = getHeight(root.right)
            if not leftOk or not rightOk or abs(leftH-rightH) > 1:
                return (False, 0)
            return (True, 1 + max(leftH, rightH))
            
        return getHeight(root)[0]

    def isBalanced_globalVar(self, root):
        def getHeight(root):
            if not root: return 0
            leftH = getHeight(root.left)
            rightH = getHeight(root.right)
            if abs(leftH-rightH) > 1:
                self.ans = False
            return 1 + max(leftH, rightH)
            
        self.ans = True
        getHeight(root)
        return self.ans


# Not good, two functions re-run the same iteration
class Solution_ming(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        leftD, rightD = self.getDepth(root.left), self.getDepth(root.right)
        return abs(leftD - rightD) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def getDepth(self, node):
        if not node:
            return 0
        return max(self.getDepth(node.left), self.getDepth(node.right)) + 1
