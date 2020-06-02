# Time:  O(n)
# Space: O(w)

# 1430
# Given a binary tree where each path going from the root to any leaf form a valid sequence, check if
# a given string is a valid sequence in such binary tree.
#
# We get the given string from the concatenation of an array of integers "arr" and the concatenation of
# all values of the nodes along a path results in a sequence in the given binary tree.

# Each node’s value is between [0 – 9]

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    # dfs solution with recursion
    def isValidSequence(self, root, arr):  # USE THIS: preorder, top-down
        """
        :type root: TreeNode
        :type arr: List[int]
        :rtype: bool
        """
        def dfs(node, depth):
            if not node or depth == len(arr) or node.val != arr[depth]:
                return False
            if depth == len(arr) - 1 and node.left == node.right:
                return True
            return dfs(node.left, depth+1) or dfs(node.right, depth+1)

        return dfs(root, 0)


    # dfs solution with stack
    def isValidSequence2(self, root, arr):
        s = [(root, 0)]
        while s:
            node, depth = s.pop()
            if not node or depth == len(arr) or node.val != arr[depth]:
                continue
            if depth+1 == len(arr) and node.left == node.right:
                return True
            s.append((node.right, depth+1))
            s.append((node.left, depth+1))
        return False


    # bfs solution
    def isValidSequence_bfs(self, root, arr):
        q = [root]
        for depth in range(len(arr)):
            new_q = []
            while q:
                node = q.pop()
                if not node or node.val != arr[depth]:
                    continue
                if depth+1 == len(arr) and node.left == node.right:
                    return True
                new_q.extend(child for child in (node.left, node.right))
            q = new_q
        return False


import collections
def ArrayToTree(a):
    if not a: return None
    root = TreeNode(a[0])
    q = collections.deque([root])
    i = 1
    while i < len(a):
        p = q.popleft()
        if a[i] is not None:
            node = TreeNode(a[i])
            p.left = node
            q.append(node)
        i += 1
        if i >= len(a): break
        if a[i] is not None:
            node = TreeNode(a[i])
            p.right = node
            q.append(node)
        i += 1
    return root

#         0
#     1      0
#   0  1   0 None
# N 1 0 0

print(Solution().isValidSequence(ArrayToTree([0,1,0,0,1,0,None,None,1,0,0]), [0,1,0,1])) # True
print(Solution().isValidSequence(ArrayToTree([0,1,0,0,1,0,None,None,1,0,0]), [0,0,1])) # False
print(Solution().isValidSequence(ArrayToTree([0,1,0,0,1,0,None,None,1,0,0]), [0,1,1])) # False