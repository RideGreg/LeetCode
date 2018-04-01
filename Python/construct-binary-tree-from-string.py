# Time:  O(n)
# Space: O(h)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        def str2treeHelper(s, i):
            start = i
            while i < len(s) and s[i] not in ['(', ')']: i += 1
            node = TreeNode(int(s[start:i]))
            if i < len(s) and s[i] == '(':
                i += 1 # go over '('
                node.left, i = str2treeHelper(s, i)
                i += 1 # go over ')'
            if i < len(s) and s[i] == '(':
                i += 1
                node.right, i = str2treeHelper(s, i)
                i += 1
            return node, i

        return str2treeHelper(s, 0)[0] if s else None

    def str2tree_bookshadow(self, s): # skill to get string for left/right subtree.
        if not s: return None
        n = ''
        while s and s[0] not in ('(', ')'):
            n += s[0]
            s = s[1:]
        node = TreeNode(int(n))
        left, right = self.divide(s)
        node.left = self.str2tree_bookshadow(left[1:-1])
        node.right = self.str2tree_bookshadow(right[1:-1])
        return node

    def divide(self, s):
        part, deg = '', 0
        while s:
            deg += {'(' : 1, ')' : -1}.get(s[0], 0)
            part += s[0]
            s = s[1:]
            if deg == 0: break
        return part, s

    def str2tree_ming(self, s):
        if not s: return None
        i, j = 0, 1
        while j < len(s) and s[j] not in ('(', ')'):
            j += 1
        node = TreeNode(int(s[i:j]))
        if j < len(s):
            leftStr, rightStr = self.parse(s[j:])
            node.left = self.str2tree_ming(leftStr[1:-1])
            node.right = self.str2tree_ming(rightStr[1:-1])
        return node

    def parse(self, s):
        deg = 0
        for i in xrange(len(s)):
            deg += {'(' : 1, ')' : -1}.get(s[i], 0)
            if deg == 0: break
        return s[:i+1], s[i+1:]

n = Solution().str2tree_ming("4(2(3)(1))(-6(5))")
print n