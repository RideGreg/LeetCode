# Time:  O(n)
# Space: O(h), h is height of binary tree
# 104
# Given a binary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
#

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root): # USE THIS: DFS recursion
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    def maxDepth_bfs(self, root): # BFS Time O(n) Space(n) queue size
        import collections
        q = collections.deque([root])
        ans = 0
        while q:
            sz = len(q)
            for _ in range(sz):
                cur = q.popleft()
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
            ans += 1
        return ans

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    print(Solution().maxDepth(root)) # 3
