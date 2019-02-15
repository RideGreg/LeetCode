# Time:  O(n * 4^n / n^(3/2)) ~= sum of Catalan numbers from 1 .. N
# Space: O(n * 4^n / n^(3/2)) ~= sum of Catalan numbers from 1 .. N

# 894
# A full binary tree is a binary tree where each node has exactly 0 or 2 children.
#
# Return a list of all possible full binary trees with N nodes.
# Each element of the answer is the root node of one possible tree.
#
# Each node of each tree in the answer must have node.val = 0.
#
# You may return the final list of trees in any order.
#
# Example 1:
#
# Input: 7
# Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],
#          [0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
# Explanation:
#
# Note:
# - 1 <= N <= 20

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.__memo = {1: [TreeNode(0)]}
    
    def allPossibleFBT(self, N): # 120 ms
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        if N % 2 == 0:
            return []

        if N not in self.__memo:
            result = []
            for i in xrange(N):
                for left in self.allPossibleFBT(i):
                    for right in self.allPossibleFBT(N-1-i):
                        node = TreeNode(0)
                        node.left = left
                        node.right = right
                        result.append(node)
            self.__memo[N] = result

        return self.__memo[N]

    # have to use clone if passing the root in recursion. 360 ms
    def allPossibleFBT_dfs(self, N):
        def encode(root):
            if not root: return ''
            return str(root.val) + '(' + encode(root.left) + ')' \
                   + '(' + encode(root.right) + ')'

        def clone(root):
            copy = TreeNode(0)
            if root.left:
                copy.left = clone(root.left)
            if root.right:
                copy.right = clone(root.right)
            return copy

        def dfs(root, cands, n):
            if n == 0:
                ss = encode(root)
                if ss not in lookup:
                    lookup.add(ss)
                    ans.append(clone(root)) #KENG: return original tree if not copy
                return

            for i in xrange(len(cands)):
                cands[i].left = TreeNode(0)
                cands[i].right = TreeNode(0)
                dfs(root, cands[i+1:] + [cands[i].left, cands[i].right], n - 2)
                cands[i].left = cands[i].right = None

        if N % 2 == 0: return []
        root = TreeNode(0)
        ans, lookup = [], set()
        dfs(root, [root], N - 1)
        return ans


#r=Solution().allPossibleFBT(1)
#r=Solution().allPossibleFBT(3)
r=Solution().allPossibleFBT(5)
r=Solution().allPossibleFBT(7)

