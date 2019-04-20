# Time:  O(n)
# Space: O(h)

# 979
# Given the root of a binary tree with N nodes, each node in the tree has node.val coins,
# and there are N coins total.
#
# In one move, we may choose two adjacent nodes and move one coin from one node to another.
# (The move may be from parent to child, or from child to parent.)
#
# Return the number of moves required to make every node have exactly one coin.

# Example: [3, 0, 0] => 2. [0, 3, 0] => 3. [1, 0, 2] => 2. [1, 0, 0, None, 3] => 4
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

        
class Solution(object):
    # For a leaf node, # of moved from the leaf node to or from its parent is
    # excess = abs(val-1), afterwords we never need to consider the leaf node.
    # So we let dfs(node) be the excess # of coins in the subtree at or below
    # this node.
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            if not root:
                return 0
            left, right = dfs(root.left), dfs(root.right)
            self.ans += abs(left) + abs(right) # number of moves from this node to its left/right children
            return root.val + left + right - 1 # excess number of coins at this node

        self.ans = 0
        dfs(root)
        return self.ans

    # USE THIS: bottom up:
    # for tree problem involves parent, recursive function usually contains parent node.
    # con: modify the original tree.
    def distributeCoins_ming(self, root):
        def dfs(root, p):
            if root is None: return
            dfs(root.left, root)
            dfs(root.right, root)

            if p:
                delta = root.val - 1
                if delta:
                    p.val += delta
                    self.ans += abs(delta)

        self.ans = 0
        dfs(root, None)
        return self.ans