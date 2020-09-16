# Time:  O(n * h)
# Space: O(h)
# 257
# Given a binary tree, return all root-to-leaf paths.
#
# For example, given the following binary tree:
#
#   1
#  /   \
# 2     3
#  \
#   5
# All root-to-leaf paths are:
#
# ["1->2->5", "1->3"]
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        def dfs(node, path): # status: path not contain node's value yet.
            if not node: return

            path.append(str(node.val))

            if not node.left and not node.right:
                ans.append('->'.join(path))
            else:
                dfs(node.left, path)
                dfs(node.right, path)

            path.pop()

        ans = []
        dfs(root, [])
        return ans
