# Time:  O(n)
# Space: O(h)

# 437
# You are given a binary tree in which each node contains an integer value.
#
# Find the number of paths that sum to a given value.
#
# The path does not need to start or end at the root or a leaf,
# but it must go downwards (traveling only from parent nodes to child nodes).
#
# The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.
#
# Example:
#
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
#
#       10
#      /  \
#     5   -3
#   / \    \
#   3   2   11
#  / \   \
# 3  -2   1
#
# Return 3. The paths that sum to 8 are:
#
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3. -3 -> 11

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections


class Solution(object):
    def pathSum(self, root, sum): # USE THIS: ok to use a version using global var instead of return value
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def dfs(node, curr):
            if node is None:
                return 0
            curr += node.val
            result = lookup[curr-sum]
            lookup[curr] += 1
            result += dfs(node.left, curr) + dfs(node.right, curr)
            lookup[curr] -= 1
            return result

        lookup = collections.defaultdict(int)
        lookup[0] = 1
        return dfs(root, 0)


# Time:  O(n^2)
# Space: O(h)
class Solution2(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def pathSumHelper(root, prev, sum):
            if root is None:
                return 0

            curr = prev + root.val
            return int(curr == sum) + \
                   pathSumHelper(root.left, curr, sum) + \
                   pathSumHelper(root.right, curr, sum)

        if root is None:
            return 0

        return pathSumHelper(root, 0, sum) + \
               self.pathSum(root.left, sum) + \
               self.pathSum(root.right, sum)

it = iter([10,5,3,3,None,None,-2,None,None,2,None,1,None,None,-3,None,11,None,None])
def build():
    v = next(it)
    if v is None:
        return None
    node = TreeNode(v)
    node.left = build()
    node.right = build()
    return node

root = build()
print(Solution().pathSum(root, 8)) # 3