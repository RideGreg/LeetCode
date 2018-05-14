# Time:  O(n)
# Space: O(h)
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
Given a binary tree, count the number of uni-value subtrees.
A Uni-value subtree means all nodes of the subtree have the same value.
For example:
Given binary tree,
              5
             / \
            1   5
           / \   \
          5   5   5
return 4.
'''

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def countUnivalSubtrees(self, root):
        [is_uni, count] = self.isUnivalSubtrees(root, 0);
        return count;

    def isUnivalSubtrees(self, root, count):
        if not root:
            return [True, count]

        [left, count] = self.isUnivalSubtrees(root.left, count)
        [right, count] = self.isUnivalSubtrees(root.right, count)
        if self.isSame(root, root.left, left) and \
           self.isSame(root, root.right, right):
                count += 1
                return [True, count]

        return [False, count]

    def isSame(self, root, child, is_uni):
        return not child or (is_uni and root.val == child.val)

class Solution_ming: # USE THIS, basically postorder to visit all nodes
    def countUnivalSubtrees(self, root):
        def isUnival(node, count):
            if not node:
                return True
            leftUnival = isUnival(node.left, count)
            rightUnival = isUnival(node.right, count)

            if not leftUnival or not rightUnival or \
                (node.left and node.left.val != node.val) or \
                (node.right and node.right.val != node.val):
                return False

            count[0] += 1
            return True


        count = [0]
        isUnival(root, count)
        return count[0]

root, root.left, root.right = TreeNode(5), TreeNode(1), TreeNode(5)
root.left.left, root.left.right, root.right.right = TreeNode(5), TreeNode(5), TreeNode(5)
print Solution_ming().countUnivalSubtrees(root) #4

root, root.left, root.right = TreeNode(2), TreeNode(2), TreeNode(2)
root.left.left, root.right.right = TreeNode(1), TreeNode(5)
print Solution_ming().countUnivalSubtrees(root) #2
