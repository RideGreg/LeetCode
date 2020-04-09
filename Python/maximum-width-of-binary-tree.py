# Time:  O(n)
# Space: O(h)

# 662
# Given a binary tree, write a function to get the maximum width of the given tree.
# The width of a tree is the maximum width among all levels. The binary tree has the same structure
# as a full binary tree, but some nodes are null.
#
# The width of one level is defined as the length between the end-nodes
# (the leftmost and right most non-null nodes in the level,
#  where the null nodes between the end-nodes are also counted into the length calculation.
#
# Example 1:
# Input:
#
#            1
#          /   \
#         3     2
#        / \     \
#       5   3     9
#
# Output: 4
# Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
# Example 2:
# Input:
#
#           1
#          /
#         3
#        / \
#       5   3
#
# Output: 2
# Explanation: The maximum width existing in the third level with the length 2 (5,3).
# Example 3:
# Input:
#
#           1
#          / \
#         3   2
#        /
#       5
#
# Output: 2
# Explanation: The maximum width existing in the second level with the length 2 (3,2).
# Example 4:
# Input:
#
#           1
#          / \
#         3   2
#        /     \
#       5       9
#      /         \
#     6           7
# Output: 8
# Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).
#
# Note: Answer will in the range of 32-bit signed integer.
#
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root): # USE THIS: don't need extra space to store nodes from each level
        """
        :type root: TreeNode
        :rtype: int
        """
        # All nodes have an id. DFS guarantee the id of leftmost node on each level are recorded.
        # Calculate max width for every node
        def dfs(node, id, depth):
            if node:
                if depth >= len(leftmosts):
                    leftmosts.append(id)
                self.ans = max(self.ans, id - leftmosts[depth] + 1)
                dfs(node.left, id * 2, depth + 1)
                dfs(node.right, id * 2 + 1, depth + 1)

        self.ans, leftmosts = 0, []
        dfs(root, 1, 0)
        return self.ans

    def widthOfBinaryTree2(self, root): # same as solution 1, not use global var
        # parent node will use max width of children nodes if it is larger.
        def dfs(node, i, depth):
            if not node:
                return 0
            if depth >= len(leftmosts):
                leftmosts.append(i)
            return max(i-leftmosts[depth]+1,
                       dfs(node.left, i*2, depth+1),
                       dfs(node.right, i*2+1, depth+1))

        leftmosts = []
        return dfs(root, 1, 0)

    # level order traversal
    def widthOfBinaryTree3(self, root: TreeNode) -> int:
        import collections
        cur, ans = collections.deque([root]), 0
        while cur:
            ans = max(ans, len(cur))
            nxt = []
            for n in cur:
                if n:
                    nxt.extend([n.left, n.right])
                else:
                    nxt.extend([None, None])
            cur = collections.deque(nxt)
            while cur and not cur[0]:
                cur.popleft()
            while cur and not cur[-1]:
                cur.pop()
        return ans

r = TreeNode(1)
r.left, r.right = TreeNode(3), TreeNode(2)
r.left.left, r.left.right = TreeNode(5), TreeNode(3)
r.right.right = TreeNode(9)
print(Solution().widthOfBinaryTree(r)) # 4
