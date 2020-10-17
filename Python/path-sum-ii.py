# Time:  O(n)
# Space: O(h), h is height of binary tree
# 113
# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
#
# For example:
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# return
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]


from typing import List

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:  # USE THIS
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def dfs(node, cur, total):
            if node:
                if not node.left and not node.right:
                    if total + node.val == sum:
                        ans.append(cur + [node.val])
                else:
                    cur.append(node.val)
                    dfs(node.left, cur, total + node.val)
                    dfs(node.right, cur, total + node.val)
                    cur.pop()
        ans = []
        dfs(root, [], 0)
        return ans


class Solution_kamyu:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        return self.pathSumRecu([], [], root, sum)


    def pathSumRecu(self, result, cur, root, sum):
        if root:
            if root.left is None and root.right is None:
                if root.val == sum:
                    result.append(cur + [root.val])
            else:
                cur.append(root.val)
                self.pathSumRecu(result, cur, root.left, sum - root.val)
                self.pathSumRecu(result, cur, root.right, sum - root.val)
                cur.pop()
        return result


if __name__ == "__main__":
    root = TreeNode(5)

    print(Solution().pathSum(root, 5))
