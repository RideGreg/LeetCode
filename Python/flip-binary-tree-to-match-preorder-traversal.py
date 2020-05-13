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
    # Context: 因为所有节点的值都不相同，那么至多只有一种可行的遍历路径供我们选择。
    # 进行深度优先遍历。如果遍历到某一个节点的时候，节点值不能与行程序列匹配，那么答案只能是 [-1]。
    # 如果当前节点match，当行程序列中的下一个期望数字 voyage[i] 与我们即将遍历的子节点的值不同的时候，
    # 只有另外一次机会翻转一下当前这个节点，看以后能否match。
    def flipMatchVoyage(self, root, voyage): # USE THIS
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        """
        def dfs(root):
            if not root: # default case, doesn't violate
                return True
            if root.val != voyage[self.i]:
                return False

            # next expected value
            self.i += 1
            if root.left and root.left.val != voyage[self.i]:
                ans.append(root.val)
                return dfs(root.right) and dfs(root.left)
            else:
                return dfs(root.left) and dfs(root.right)

        self.i = 0
        ans = []
        return ans if dfs(root) else [-1]

    # same to above, but recursive function signaure doesn't return bool.
    def flipMatchVoyage_leetcodeChinaOfficial(self, root, voyage):
        self.flipped = []
        self.i = 0

        def dfs(node):
            if node:
                if node.val != voyage[self.i]:
                    self.flipped = [-1]
                    return
                self.i += 1

                if (self.i < len(voyage) and
                        node.left and node.left.val != voyage[self.i]):
                    self.flipped.append(node.val)
                    dfs(node.right)
                    dfs(node.left)
                else:
                    dfs(node.left)
                    dfs(node.right)

        dfs(root)
        if self.flipped and self.flipped[0] == -1:
            self.flipped = [-1]
        return self.flipped

    def flipMatchVoyage_tooComplex(self, root, voyage):
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


root = TreeNode(1)
root.left, root.right = TreeNode(8), TreeNode(6)
root.left.left, root.left.right = TreeNode(7), TreeNode(3)
root.right.right = TreeNode(5)
print(Solution().flipMatchVoyage(root, [1,6,5,8,3,7])) # [1, 8]

root2=TreeNode(1)
root2.left, root2.right = TreeNode(2), TreeNode(3)
print(Solution().flipMatchVoyage(root2, [1,2,3])) # []
print(Solution().flipMatchVoyage(root2, [1,3,2])) # [1]
print(Solution().flipMatchVoyage(root2, [2,3,1])) # [-1]

