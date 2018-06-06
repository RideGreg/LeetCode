# Time:  O(n)
# Space: O(n)

# Given a binary tree, return all duplicate subtrees.
# For each kind of duplicate subtrees, you only need to return the root node of any one of them.
#
# Two trees are duplicate if they have the same structure with same node values.
#
# Example 1:
#         1
#        / \
#       2   3
#      /   / \
#     4   2   4
#        /
#       4
# The following are two duplicate subtrees:
#       2
#      /
#     4
# and
#     4
# Therefore, you need to return above trees' root in the form of a list.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections


class Solution(object):
    def findDuplicateSubtrees(self, root):
        trees = collections.defaultdict()
        trees.default_factory = trees.__len__
        count = collections.Counter()
        ans = []
        def lookup(node):
            if node:
                uid = trees[(node.val, lookup(node.left), lookup(node.right))]
                count[uid] += 1
                if count[uid] == 2:
                    ans.append(node)
                return uid

        lookup(root)
        return ans
    def findDuplicateSubtrees_2(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        def getid(root, lookup, trees):
            if root:
                node_id = lookup[root.val, \
                                 getid(root.left, lookup, trees), \
                                 getid(root.right, lookup, trees)]
                trees[node_id].append(root)
                return node_id
        trees = collections.defaultdict(list)
        lookup = collections.defaultdict()
        lookup.default_factory = lookup.__len__
        getid(root, lookup, trees)
        return [roots[0] for roots in trees.values() if len(roots) > 1]


# Time:  O(n * h)
# Space: O(n * h)
class Solution2(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        def postOrderTraversal(node, lookup, result):
            if not node:
                return ""
            s = "(" + postOrderTraversal(node.left, lookup, result) + \
                str(node.val) + \
                postOrderTraversal(node.right, lookup, result) + \
                ")"
            if lookup[s] == 1:
                result.append(node)
            lookup[s] += 1
            return s

        lookup = collections.defaultdict(int)
        result = []
        postOrderTraversal(root, lookup, result)
        return result

class Solution3(object):     # USE THIS
    def findDuplicateSubtrees(self, root):
        import collections
        def preOrder(node):
            if not node:
                return '#'
            serial = '{},{},{}'.format(node.val, preOrder(node.left), preOrder(node.right))
            map[serial] += 1
            if map[serial] == 2:
                ans.append(node)

            return serial

        ans, map = [], collections.Counter()
        preOrder(root)
        return ans


root = TreeNode(1)
root.left, root.right = TreeNode(2), TreeNode(3)
root.left.left, root.right.left, root.right.right = TreeNode(4), TreeNode(2), TreeNode(4)
root.right.left.left = TreeNode(4)

root2 = TreeNode(1)
root2.left, root2.right = TreeNode(2), TreeNode(3)
root2.right.left = TreeNode(2)

print Solution().findDuplicateSubtrees(root2)