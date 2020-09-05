# Time:  O(n)
# Space: O(h), h is height of binary tree
#
# Given a binary tree, find the maximum path sum.
#
# The path may start and end at any node in the tree.
#
# For example:
# Given the below binary tree,
#
#        1
#       / \
#      2   3
# Return 6.
#


# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    maxSum = float('-inf')

    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        self.dfs(root)
        return self.maxSum

    def dfs(self, root):
        if root is None:
            return 0
        left = max(0, self.dfs(root.left))
        right = max(0, self.dfs(root.right))
        self.maxSum = max(self.maxSum, root.val + left + right)
        return root.val + max(left, right)

# not use global var, pass/update the var in recursion
class Solution_passReturnVal(object):
    def maxPathSum(self, root):
        def getMax(node, ans):
            if not node: return (ans, 0)
            ans, leftM = getMax(node.left, ans)
            ans, rightM = getMax(node.right, ans)
            cur = node.val + max(0, leftM) + max(0, rightM)
            ans = max(ans, cur)
            return (ans, node.val + max(0, leftM, rightM))
        
        return getMax(root, float('-inf'))[0] if root else 0


class Solution_iterator(object):
    def maxPathSum(self, root):
        def iter_dfs(node):
            result = float("-inf")
            max_sum = [0]
            stk = [(1, [node, max_sum])]
            while stk:
                step, params = stk.pop()
                if step == 1:
                    node, ret = params
                    if not node:
                        continue
                    ret1, ret2 = [0], [0]
                    stk.append((2, [node, ret1, ret2, ret]))
                    stk.append((1, [node.right, ret2]))
                    stk.append((1, [node.left, ret1]))
                elif step == 2:
                    node, ret1, ret2, ret = params
                    result = max(result, node.val+max(ret1[0], 0)+max(ret2[0], 0))
                    ret[0] = node.val+max(ret1[0], ret2[0], 0)
            return result
        
        return iter_dfs(root)


# Time:  O(n)
# Space: O(h), h is height of binary tree
class Solution2(object):
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        def dfs(node):
            if not node:
                return (float("-inf"), 0)
            max_left, curr_left = dfs(node.left)
            max_right, curr_right = dfs(node.right)
            return (max(max_left, max_right, node.val+max(curr_left, 0)+max(curr_right,0)),
                    node.val+max(curr_left, curr_right, 0))
        
        return dfs(root)[0]


root = TreeNode(-10)
root.left, root.right = TreeNode(9), TreeNode(20)
root.right.left, root.right.right = TreeNode(15), TreeNode(7)
print(Solution().maxPathSum(root)) # 42
