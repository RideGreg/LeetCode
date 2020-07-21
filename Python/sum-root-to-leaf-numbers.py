# Time:  O(n)
# Space: O(h), h is height of binary tree
# 129
# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
#
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
#
# Find the total sum of all root-to-leaf numbers.
#
# For example,
#
#     1
#    / \
#   2   3
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
#
# Return the sum = 12 + 13 = 25.
#

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root: TreeNode) -> int: # USE THIS
        ans = 0
        stack = [(root, 0)]
        while stack:
            node, v = stack.pop()
            if node:
                if not node.left and not node.right:
                    ans += v*10 + node.val
                else:
                    stack.append((node.right, v*10+node.val))
                    stack.append((node.left, v*10+node.val))
        return ans

    def sumNumbers_rec1(self, root):
        return self.recu(root, 0)

    def recu(self, root, num):
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return num * 10 + root.val

        return self.recu(root.left, num * 10 + root.val) + self.recu(root.right, num * 10 + root.val)

    # the following recursion is not very good (use global var, don't leverage return value)
    def sumNumbers_rec2(self, root: TreeNode) -> int:
        def dfs(node, v):
            if node:
                if not (node.left or node.right):
                    self.ans += v*10 + node.val
                    return
                dfs(node.left, v*10+node.val)
                dfs(node.right, v*10+node.val)

        self.ans = 0
        dfs(root, 0)
        return self.ans

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    print(Solution().sumNumbers(root)) # 137
