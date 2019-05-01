# Time:  O(n)
# Space: O(h)

# 1026
# Given the root of a binary tree, find the maximum value V for which there exists
# different nodes A and B where V = |A.val - B.val| and A is an ancestor of B.
#
# (A node A is an ancestor of B if either: any child of A is equal to B, or any
# child of A is an ancestor of B.)

# Solution: We pass the minimum and maximum values to the children,
# At the leaf node, we calculate max - min.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
# Time:  O(n)
# Space: O(h)
# recursive solution
    def maxAncestorDiff(self, root): # USE THIS
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, minn, maxx):
            if not node: # an empty subtree
                return 0

            # update minn/maxx
            minn = min(minn, node.val)
            maxx = max(maxx, node.val)
            if not node.left and not node.right: # leaf
                return abs(maxx - minn)

            return max(dfs(node.left, minn, maxx),
                       dfs(node.right, minn, maxx))

        return dfs(root, float('inf'), float('-inf'))

    # iterative stack solution
    def maxAncestorDiff_iter(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = 0
        stack = [(root, 0, float("inf"))]
        while stack:
            node, mx, mn = stack.pop()
            if not node:
                continue
            result = max(result, mx-node.val, node.val-mn)
            mx = max(mx, node.val)
            mn = min(mn, node.val)
            stack.append((node.left, mx, mn))
            stack.append((node.right, mx, mn))
        return result

# use global var, no return from helper func.
class Solution2:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def dfs(node, minn, maxx):
            if node:
                minn = min(minn, node.val)
                maxx = max(maxx, node.val)
                dfs(node.left, minn, maxx)
                dfs(node.right, minn, maxx)
            else:
                self.ans = max(self.ans, abs(maxx - minn))

        self.ans = 0
        dfs(root, float('inf'), float('-inf'))
        return self.ans

    # The following way is worse maintaining a path, as in the end we need to traverse the path
    # to find min/max. Much better if pass min/max along the way.
    def maxAncestorDiff_maintainPath(self, root):
        def dfs(n, path):
            if n:
                path.append(n.val)
                if not n.left and not n.right:
                    self.ans = max(self.ans, max(path) - min(path))
                dfs(n.left, path)
                dfs(n.right, path)
                path.pop()

        self.ans = 0
        dfs(root, [])
        return self.ans

r = TreeNode(8)
r.left, r.right = TreeNode(3), TreeNode(10)
r.left.left, r.left.right = TreeNode(1), TreeNode(6)
r.left.right.left, r.left.right.right = TreeNode(4), TreeNode(7)
r.right.right = TreeNode(14)
r.right.right.left = TreeNode(13)

print(Solution2().maxAncestorDiff_recur(r)) # 7