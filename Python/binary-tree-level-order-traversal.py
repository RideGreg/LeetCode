# Time:  O(n)
# Space: O(n)
# 102
# Given a binary tree, return the level order traversal of its nodes' values.
# (ie, from left to right, level by level).
#
# For example:
# Given binary tree {3,9,20,#,#,15,7},
#    3
#   / \
#  9  20
#    /  \
#   15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
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
    def levelOrder(self, root): # USE This: 维护每个节点的深度
        ans = []
        q = collections.deque([(root, 1)])
        while q:
            node, dep = q.popleft()
            if node:
                while dep > len(ans):
                    ans.append([])
                ans[dep-1].append(node.val)
                q.append((node.left, dep+1))
                q.append((node.right, dep+1))
        return ans

    # modified BFS: 每次迭代从queue中取k个元素，而不是1个元素。k是每一层的valid nodes
    # 无需维护深度
    def levelOrder2(self, root):
        ans = []
        if not root: return ans

        q = collections.deque([root])
        while q:
            sz = len(q)
            ans.append([])
            for _ in range(sz):
                cur = q.popleft()
                ans[-1].append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return ans


    def levelOrder_newList(self, root): # 费空间：每次分配一个新的数组
        if root is None:
            return []
        result, current = [], [root]
        while current:
            next_level, vals = [], []
            for node in current:
                vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current = next_level
            result.append(vals)
        return result
