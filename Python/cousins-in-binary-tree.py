# Time:  O(n)
# Space: O(h)

# 993
# In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
#
# Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
#
# We are given the root of a binary tree with unique values, and the values x and y of
# two different nodes in the tree.
# Return true if and only if the nodes corresponding to the values x and y are cousins.

# Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
# Output: true

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isCousins(self, root, x, y): # USE THIS: iteration DFS, early return
        stk = [(root, 0, None)]
        first = None
        while stk:
            cur, depth, par = stk.pop()
            if cur:
                if cur.val in (x, y):
                    if first is None:
                        first = (depth, par)
                    else:
                        return first[0] == depth and first[1] != par
                stk.append((cur.left, depth+1, cur))
                stk.append((cur.right, depth+1, cur))


    # DFS to annotate parent and depth. Recursion hard to early return.
    def isCousins_LeetcodeOfficial(self, root, x, y):
        parent = {}
        depth = {}
        def dfs(node, par):
            if node:
                depth[node.val] = 1 + depth[par.val] if par else 0
                parent[node.val] = par
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root, None)
        return depth[x] == depth[y] and parent[x] != parent[y]
                
        
