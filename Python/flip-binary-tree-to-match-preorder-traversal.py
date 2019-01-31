# Time:  O(n)
# Space: O(h)

# 971
# Given a binary tree with N nodes, each node has a different value from {1, ..., N}.
#
# A node in this binary tree can be flipped by swapping the left child and the right child of that node.
#
# Consider the sequence of N values reported by a preorder traversal starting from the root.  Call such a sequence of N values
# the voyage of the tree.
#
# Our goal is to flip the least number of nodes in the tree so that the voyage of the tree matches the voyage we are given.
#
# If we can do so, then return a list of the values of all nodes flipped.  You may return the answer in any order.
# If we cannot do so, then return the list [-1].


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

        
class Solution(object):
    def flipMatchVoyage(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        """
        def count(root):
            if not root: return 0
            ans = 1 + count(root.left) + count(root.right)
            counts[root] = ans
            return ans

        def match(root, seq):
            if not root and not seq: return True
            if not root or not seq: return False

            lCnt = counts[root.left] if root.left else 0
            rCnt = counts[root.right] if root.right else 0

            if root.val != seq[0] or 1 + lCnt + rCnt != len(seq):
                return False

            if match(root.left, seq[1:1 + lCnt]) and match(root.right, seq[1 + lCnt:]):
                return True
            if match(root.right, seq[1:1 + rCnt]) and match(root.left, seq[1 + rCnt:]):
                ans.append(root.val)
                return True
            return False

        counts = {}
        count(root)
        ans = []
        return ans if match(root, voyage) else [-1]


    # Not good: maintain a variable for index in voyage, increment the index in each iteration.
    def flipMatchVoyage_kamyu(self, root, voyage):
        def dfs(root, voyage, i, result):
            if not root:
                return True
            if root.val != voyage[i[0]]:
                return False
            i[0] += 1
            if root.left and root.left.val != voyage[i[0]]:
                result.append(root.val)
                return dfs(root.right, voyage, i, result) and \
                       dfs(root.left, voyage, i, result)
            return dfs(root.left, voyage, i, result) and \
                   dfs(root.right, voyage, i, result)
        
        result = []
        return result if dfs(root, voyage, [0], result) else [-1]

root2=TreeNode(1)
root2.left, root2.right = TreeNode(2), TreeNode(3)
print(Solution().flipMatchVoyage(root2, [1,2,3])) # []
print(Solution().flipMatchVoyage(root2, [1,3,2])) # [1]
print(Solution().flipMatchVoyage(root2, [2,3,1])) # [-1]