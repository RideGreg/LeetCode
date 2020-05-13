# Time:  O(n)
# Space: O(h)

# 1261
# Given a binary tree with the following rules:
# 1. root.val == 0
# 2. If treeNode.val == x and treeNode.left != null, then treeNode.left.val == 2 * x + 1
# 3. If treeNode.val == x and treeNode.right != null, then treeNode.right.val == 2 * x + 2
#
# Now the binary tree is contaminated, which means all treeNode.val have been changed to -1.
#
# You need to first recover the binary tree and then implement the FindElements class:
# - FindElements(TreeNode* root) Initializes the object with a contamined binary tree, you need to recover it first.
# - bool find(int target) Return if the target value exists in the recovered binary tree.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class FindElements(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        def dfs(node, v):
            if node:
                self.lookup.add(v)
                dfs(node.left, 2*v+1)
                dfs(node.right, 2*v+2)

        self.lookup = set()
        dfs(root, 0)

    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        return target in self.lookup
