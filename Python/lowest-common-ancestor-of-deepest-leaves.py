# Time:  O(n)
# Space: O(h)

# 1123
# Given a rooted binary tree, return the lowest common ancestor of its deepest leaves.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 后序遍历，先子后父
class Solution(object):
    def lcaDeepestLeaves(self, root): # USE THIS: depth 0 is at leaf
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def dfs(root):
            if not root:
                return 0, None

            d1, lca1 = dfs(root.left)
            d2, lca2 = dfs(root.right)
            if d1 > d2: return d1+1, lca1
            elif d1 < d2: return d2+1, lca2
            else: return d1+1, root

        return dfs(root)[1]

    # depth 0 is at root, has to pass depth as a param
    def lcaDeepestLeaves2(self, root: TreeNode) -> TreeNode:
        def dfs(node, dep):
            if not node: return dep - 1, None

            ld, ln = dfs(node.left, dep+1)
            rd, rn = dfs(node.right, dep+1)
            if ld == rd: return ld, node
            elif ld > rd: return ld, ln
            else: return rd, rn
        return dfs(root, 0)[1]

root = TreeNode(1)
root.left, root.right = TreeNode(2), TreeNode(3)
print(Solution().lcaDeepestLeaves(root).val) # 1

root.left.left = TreeNode(4)
print(Solution().lcaDeepestLeaves(root).val) # 4

root.left.right = TreeNode(5)
print(Solution().lcaDeepestLeaves(root).val) # 2
