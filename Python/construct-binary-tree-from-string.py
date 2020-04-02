# Time:  O(n)
# Space: O(h)

# 536
# You need to construct a binary tree from a string consisting of parenthesis and integers.
#
# The whole input represents a binary tree. It contains an integer followed by zero, one or two
# pairs of parenthesis. The integer represents the root's value and a pair of parenthesis
# contains a child binary tree with the same structure.
#
# You always start to construct the left child node of the parent first if it exists.
# 1. There will only be '(', ')', '-' negative sign and '0' ~ '9' in the input string.
# 2. An empty tree is represented by "" instead of "()".

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def str2tree(self, s): # USE THIS, need to maintain index of current char
        """
        :type s: str
        :rtype: TreeNode
        """
        def str2treeHelper(s, i):
            start = i
            while i < len(s) and (s[i].isdigit() or s[i] == '-'): i += 1
            node = TreeNode(int(s[start:i]))
            # left subtree
            if i < len(s) and s[i] == '(':
                i += 1
                node.left, i = str2treeHelper(s, i)
                i += 1                     # closing parenthesis
            # right subtree
            if i < len(s) and s[i] == '(':
                i += 1
                node.right, i = str2treeHelper(s, i)
                i += 1                     # closing parenthesis
            return node, i

        return str2treeHelper(s, 0)[0] if s else None

    # stack solution: need to be careful about when to push/pop stack
    def str2tree_stack(self, s):
        stk, i = [], 0
        while i < len(s):
            start = i
            if i < len(s) and s[i] == ')':
                stk.pop()  # node at stack top has no child, pop from stack
                i += 1
            elif i < len(s) and s[i] == '(':
                i += 1
            else:
                while i < len(s) and ('0' <= s[i] <= '9' or s[i] == '-'):
                    i += 1
                node = TreeNode(int(s[start:i]))
                if stk:
                    p = stk[-1]
                    if not p.left:
                        p.left = node
                    else:
                        p.right = node
                stk.append(node)
        return stk[-1]

tr = Solution().str2tree("40(2(3)(1))(-6(5))")
print(Solution().str2tree("40(2(3)(1))(-6(5))"))
#     40
#   /   \
#  2    -6
# / \   /
# 3   1 5

print(Solution().str2tree("101"))
