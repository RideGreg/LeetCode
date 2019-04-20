# Time:  O(n + l * h), l is the number of leaves
# Space: O(h)

# 988
# Given the root of a binary tree, each node has a value from 0 to 25 representing the letters 'a' to 'z':
# a value of 0 represents 'a', a value of 1 represents 'b', and so on.
#
# Find the lexicographically smallest string that starts at a leaf of this tree and ends at the root.
#
# (As a reminder, any shorter prefix of a string is lexicographically smaller: for example, "ab" is
# lexicographically smaller than "aba".  A leaf of a node is a node that has no children.)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# NOTE:
# 1. String join is significantly faster then concatenation.
# https://stackoverflow.com/questions/3055477/how-slow-is-pythons-string-concatenation-vs-str-join

# 2. Modify a list in place is faster than creating new instances of list.

class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        def dfs(node, path):
            if node:
                path.append(chr(ord('a') + node.val))
                if not node.left and not node.right:
                    self.ans = min(self.ans, "".join(reversed(path))) # prefer string join
                dfs(node.left, path)    # prefer append/pop one list, rather than new lists
                dfs(node.right, path)
                path.pop()

        self.ans = "~"
        dfs(root, [])
        return self.ans

root = TreeNode(0)
root.left, root.right = TreeNode(1), TreeNode(2)
root.left.left, root.left.right = TreeNode(3), TreeNode(4)
root.right.left, root.right.right = TreeNode(3), TreeNode(4)
print(Solution().smallestFromLeaf(root)) # 'dba'