# Time:  O(n)
# Space: O(h)

# 1339
# Given a binary tree root. Split the binary tree into two subtrees by removing 1 edge such that
# the product of the sums of the subtrees are maximized.
#
# Since the answer may be too large, return it modulo 10^9 + 7.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections
def ArrayToTree(a):
    if not a: return None
    root = TreeNode(a[0])
    q = collections.deque([root])
    i = 1
    while i < len(a):
        p = q.popleft()
        if a[i]:
            node = TreeNode(a[i])
            p.left = node
            q.append(node)
        i += 1
        if i >= len(a): break
        if a[i]:
            node = TreeNode(a[i])
            p.right = node
            q.append(node)
        i += 1
    return root

# 做两次后序遍历，第一次求出树中所有之和，第二次计算每个子树的节点和
class Solution(object):
    def maxProduct(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        MOD = 10**9 + 7
        def dfs(root):
            if not root:
                return 0

            subtotal = dfs(root.left) + dfs(root.right) + root.val
            if self.getAns:
                # 不能在此对10^9+7取模，因为原先较大的数，取模之后不一定仍然较大
                # 如要防溢出，利用均值不等式选较靠近total一半值的subtotal
                result[0] = max(result[0], subtotal*(total-subtotal) )
            return subtotal

        result = [float('-inf')]
        self.getAns = False
        total = dfs(root)
        self.getAns = True
        dfs(root)
        return result[0] % MOD

print(Solution().maxProduct(ArrayToTree([1,2,3,4,5,6]))) # 110
print(Solution().maxProduct(ArrayToTree([1,None,2,3,4,None,None,5,6]))) # 90
print(Solution().maxProduct(ArrayToTree([2,3,9,10,7,8,6,5,4,11,1]))) # 1025
print(Solution().maxProduct(ArrayToTree([1,1]))) # 1