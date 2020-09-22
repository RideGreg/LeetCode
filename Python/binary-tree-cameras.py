# Time:  O(n)
# Space: O(h)

# 968
# Given a binary tree, we install cameras on the nodes of the tree.
# Each camera at a node can monitor its parent, itself, and its immediate children.
# Calculate the minimum number of cameras needed to monitor all nodes of the tree.

# Example:
# Input: [0,1,null,2,3]
# Output: 1
# Explanation: One camera at node 1 is enough to monitor all nodes.

# Input: [0,1,null,2,null,3,null,null,4]
# Output: 2
# Explanation: At least two cameras (node 1 and node 3) are needed to monitor all nodes of the tree.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Tree Dynamic Programming:
# min # of camera needed for current node depends on the min # of subtree. The key part is to find a proper State Transfer Function.
# Then we find we need 3 states for each node: camera at the node (state 2); when camera at the node, child node can be
# either being monitored by itself/underneath (state 1), or not being monitored by itself/underneath but by this node (state 0)

# [State 2] Placed camera: All the nodes below and including this node are covered, and there is a camera
# here (which may cover nodes above this node).
# [State 1] Normal subtree: All the nodes below and including this node are covered, but there is no camera here.
# [State 0] Strict subtree: All the nodes below this node are covered, but not this node.

# Find the min # of cameras for 3 states on children node, then use them to calculate for parent node.
# The State Transfer function is:
# - To cover a strict subtree, the children of this node must be in state 1.
# - To cover a normal subtree without placing a camera here, the children of this node must be in
# states 1 or 2, and at least 1 child must be in state 2.
# - To cover the subtree when placing a camera here, the children can be in any state.

class Solution(object):
    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dp(node):
            if node is None:
                return 0, 0, float('inf')

            left, right = dp(node.left), dp(node.right)

            dp0 = left[1] + right[1]
            dp1 = min(left[1] + right[2], left[2] + right[1], left[2] + right[2])
            dp2 = 1 + min(left) + min(right)

            return dp0, dp1, dp2

        return min(dp(root)[1:])

    def minCameraCover_kamyu(self, root):  # hard to understand
        UNCOVERED, COVERED, CAMERA = range(3)
        def dfs(root, result):
            left = dfs(root.left, result) if root.left else COVERED
            right = dfs(root.right, result) if root.right else COVERED
            if left == UNCOVERED or right == UNCOVERED:
                result[0] += 1
                return CAMERA
            if left == CAMERA or right == CAMERA:
                return COVERED
            return UNCOVERED
        
        result = [0]
        if dfs(root, result) == UNCOVERED:
            result[0] += 1
        return result[0]

# Greedy
# Have to traverse all tree nodes; choose from top down or bottom up. WHY BOTTOM UP IS BETTER THAN TOP DOWN?
# It is impossible to decide whether we should place a camera at root node; but easy to conclude that never
# place camera at leaf nodes, leaf nodes' parents are better to minimize total cameras as no need to cover
# leaf's children which are None.

# Start with the deepest nodes and working our way up the tree, placing a camera only when necessary.
# The *necessary* conditions are:
# 1. if a node has children that are not covered, then we must place a camera here.
# 2. if a node is not covered and has no parent, we must place a camera here.

# In the contrast, some *unnecessary* conditions are:
# 1. If a node has its children covered and has a parent, no need to place camera at this node because
# it is strictly better to place the camera at this node's parent.
# 2. Never place a camera at leaf nodes, left's parents is better places.

class Solution2(object):              # USE THIS
    def minCameraCover(self, root):
        self.ans = 0
        # Treat 'None' node as covered, so leaf node has its children covered.
        # set literal is faster than set constructor, only works for non-empty set
        # https://stackoverflow.com/questions/36674083/why-is-it-possible-to-replace-sometimes-set-with
        covered = {None}

        def dfs(node, par):
            if node:
                dfs(node.left, node)
                dfs(node.right, node)

                if node.left not in covered or \
                    node.right not in covered or \
                    (node not in covered and par is None):  # need this, otherwise wrong for 0->1->2->3 tree with all right nodes
                    self.ans += 1          # put a camera at node, which covers node and par and node's children
                    covered.update({node, par, node.left, node.right})

        dfs(root, None)
        return self.ans

r1 = TreeNode(0)
r1.left = TreeNode(1)
r1.left.left, r1.left.right = TreeNode(2), TreeNode(3)
print(Solution2().minCameraCover(r1)) # 1: place camera at node 1

r1 = TreeNode(0)
r1.left = TreeNode(1)
r1.left.left = TreeNode(2)
r1.left.left.left = TreeNode(3)
r1.left.left.left.left = TreeNode(4)
r1.left.left.left.left.left = TreeNode(5)
print(Solution2().minCameraCover(r1)) # 2: place camera at node 1 and node 4

# if we don't place camera when (node not in covered and par is None), will be a bug
# where camera at node 2 covered 1/2/3, but node 0 is not covered.
r1 = TreeNode(0)
r1.right = TreeNode(1)
r1.right.right = TreeNode(2)
r1.right.right.right = TreeNode(3)
print(Solution2().minCameraCover(r1)) # 2: place camera at node 0 and node 2