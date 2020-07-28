# Time:  O(n)
# Space: O(n) 主要的内存开销是双端队列。任何时刻，双端队列中最多只存储两层节点。因此双端队列的大小不超过 2⋅L，其中
# L 是一层的最大节点数。包含最多节点的层可能是完全二叉树的叶节点层，大约有 L = N / 2个节点。因此最坏情况下，空间复杂度为 N。
#
#
# 103
# Given a binary tree, return the zigzag level order traversal of
# its nodes' values. (ie, from left to right, then right to left
# for the next level and alternate between).
#
# For example:
# Given binary tree {3,9,20,#,#,15,7},
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:
# [
#   [3],
#   [20,9],
#   [15,7]
# ]
#


# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections
class Solution(object):
    # @param root, a tree node
    # @return a list of lists of integers

    # better time than use deque for each level, because each deque has to be converted to list O(n)
    def zigzagLevelOrder(self, root): # USE THIS
        if not root: return []
        q, ans = collections.deque([root]), []
        while q:
            sz = len(q)
            level = []
            for _ in range(sz):
                cur = q.popleft()
                level.append(cur.val)
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
            if len(ans) & 1:
                level = level[::-1]
            ans.append(level)
        return ans

    # not good as BFS, has to revert alternating levels before return.
    def zigzagLevelOrder_dfs(self, root):
        # if visiting a level first time, create list for the level
        def dfs(node, level):
            if level >= len(ans):
                ans.append([])
            ans[level].append(node.val)
            if node.left:
                dfs(node.left, level + 1)
            if node.right:
                dfs(node.right, level + 1)

        if not root: return []
        ans = []
        dfs(root, 0)
        for i in range(len(ans)):
            if i & 1:
                ans[i] = ans[i][::-1]
        return ans

    # More space needed: allocate new space for each next_level
    def zigzagLevelOrder_kamyu(self, root):
        if root is None:
            return []
        result, current, level = [], [root], 1
        while current:
            next_level, vals = [], []
            for node in current:
                vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if level % 2:
                result.append(vals)
            else:
                result.append(vals[::-1])
            level += 1
            current = next_level
        return result

rt = TreeNode(3)
rt.left, rt.right = TreeNode(9), TreeNode(20)
rt.right.left, rt.right.right = TreeNode(15), TreeNode(7)
rt.right.left.right = TreeNode(77)
print(Solution().zigzagLevelOrder(rt)) # [[3],[20,9],[15,7], [77]]