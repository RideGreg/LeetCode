# Time:  O(n)
# Space: O(h), h = logn for recursion

# 1022
# Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path represents a binary 
# number starting with the most significant bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, 
# then this could represent 01101 in binary, which is 13.
# 
# For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.
# 
# Return the sum of these numbers.


# Solution: decompose this problem into 2 sub-problem:
# 1. Find all path from root to leaves. DFS recursion should help do that.
# 2. Transform a path from base to base 10.
# You can do this separately, and it will be a O(N^2) solution.
# Combine them together is O(N)


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumRootToLeaf(self, root): # USE THIS
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root, val):
            if not root:
                return 0
            val = val*2 + root.val # KENG val<<1 + root.val is wrong, should be (val<<1) + root.val
            if not root.left and not root.right:
                return val
            return dfs(root.left, val) + dfs(root.right, val)
        
        return dfs(root, 0)

    def sumRootToLeaf_globalVar_noReturnAPI(self, root: TreeNode) -> int:
        def dfs(node, cur):
            if node:
                cur = cur * 2 + node.val
                if not node.left and not node.right:
                    self.ans += cur

                dfs(node.left, cur)
                dfs(node.right, cur)
        self.ans = 0
        dfs(root, 0)
        return self.ans

    # O(n^2) not good, just for a lessen: maintain the path and scan path at the end
    def sumRootToLeaf_n2_calcPath(self, root):
        self.ans = 0

        def preorder(r, path):
            if r:
                if not r.left and not r.right:
                    self.ans += int(''.join(map(str, path)), 2)
                preorder(r.left, path + [r.left.val])
                preorder(r.right, path + [r.right.val])

        preorder(root, [root.val])
        return self.ans

rt = TreeNode(1)
rt.left, rt.right = TreeNode(0), TreeNode(1)
rt.left.left, rt.left.right = TreeNode(0), TreeNode(1)
rt.right.left, rt.right.right = TreeNode(0), TreeNode(1)

print(Solution().sumRootToLeaf(rt)) # 22
