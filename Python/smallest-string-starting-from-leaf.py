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

    # WRONG: try to get a optimal answer from subtree doesn't work and dangerous
    # the reuslted string may involve comparison of the parent node!!
    def smallestFromLeaf_wrong(self, root): # WRONG return 'abz'
        if not root: return ''

        c = chr(ord('a')+root.val)
        L, R = self.smallestFromLeaf(root.left), self.smallestFromLeaf(root.right)
        if not L and not R:
            return c
        elif not L or not R:
            return (L or R) + c
        else:
            return min(L+c, R+c)

root = TreeNode(25)
root.left, root.right = TreeNode(1), None
root.left.left, root.left.right = TreeNode(0), TreeNode(0)
root.left.left.left = TreeNode(1)
root.left.left.left.left = TreeNode(0)
print(Solution().smallestFromLeaf(root)) # 'ababz' easy to make mistake to return 'abz'
#                  z
#           b          None
#      a        a
#    b None  None None
#  a  None