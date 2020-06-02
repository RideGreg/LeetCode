# Time:  O(max(h, k))
# Space: O(h)

# 230
# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
#
# Note:
# You may assume k is always valid, 1 <= k <= BST's total elements.
#
# Follow up:
# What if the BST is modified (insert/delete operations) often and
# you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
#

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} k
    # @return {integer}
    def kthSmallest(self, root, k): # USE THIS, inOrder_clean
        stack = [(root, False)]
        while stack:
            cur, visited = stack.pop()
            if cur:
                if visited:
                    k -= 1
                    if k == 0:
                        return cur.val
                else:
                    stack.append((cur.right, False))
                    stack.append((cur, True))
                    stack.append((cur.left, False))

    def kthSmallest_recur_woGlobalVar(self, root, k): # pass k and node as param
        def dfs(node, k):
            if node is None:
                return None, k
            # left subtree
            retVal, k = dfs(node.left, k)
            if retVal is not None:
                return retVal, k
            # process one node, decrement k
            if k == 1:
                return node.val, 0
            k -= 1
            # right subtree
            retVal, k = dfs(node.right, k)
            if retVal is not None:
                return retVal, k

            return None, k

        return dfs(root, k)[0]

    def kthSmallest_recur(self, root, k):
        self.ans = -1
        self.k = k

        def inorder(root):
            if not root: return

            inorder(root.left)
            self.k -= 1
            if self.k == 0:
                self.ans = root.val
            inorder(root.right)

        inorder(root)
        return self.ans

    def kthSmallest3(self, root, k):
        def pushLeft(node):
            while node:
                stack.append(node)
                node = node.left

        stack = []
        pushLeft(root)
        while stack and k > 0:
            node = stack.pop()
            k -= 1
            pushLeft(node.right)
        return node.val


    def kthSmallest4(self, root, k):
        s, cur, rank = [], root, 0

        while s or cur:
            if cur:
                s.append(cur)
                cur = cur.left
            else:
                cur = s.pop()
                rank += 1
                if rank == k:
                    return cur.val
                cur = cur.right

        return float("-inf")

root = TreeNode(3)
root.left, root.right = TreeNode(1), TreeNode(4)
root.left.right = TreeNode(2)
print(Solution().kthSmallest(root, 1))
