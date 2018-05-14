# Time:  O(n)
# Space: O(1)
#
# Given a binary tree, return the preorder traversal of its nodes' values.
#
# For example:
# Given binary tree {1,#,2,3},
#    1
#     \
#      2
#     /
#    3
# return [1,2,3].
#
# Note: Recursive solution is trivial, could you do it iteratively?
#


# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Morris Traversal Solution
class Solution(object):
    def preorderTraversal_morris(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result, curr = [], root
        while curr:
            if curr.left is None:
                result.append(curr.val)
                curr = curr.right
            else:
                node = curr.left
                while node.right and node.right != curr:
                    node = node.right

                if node.right is None:
                    result.append(curr.val)
                    node.right = curr
                    curr = curr.left
                else:
                    node.right = None
                    curr = curr.right

        return result


# Time:  O(n)
# Space: O(h)
# Stack Solution
class Solution2(object):
    def preorderTraversal(self, root): # USE THIS
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result, stack = [], [(root, False)]
        while stack:
            root, is_visited = stack.pop()
            if root is None:
                continue
            if is_visited:
                result.append(root.val)
            else:
                stack.append((root.right, False))
                stack.append((root.left, False))
                stack.append((root, True))
        return result

    def preorderTraversal_stack_ming(self, root):
        ans, stk = [], []
        while root or stk:
            if not root:
                root = stk.pop()
            ans.append(root.val)
            if root.right:
                stk.append(root.right)
            root = root.left
        return ans

    def preorderTraversal_recursive(self, root):
        def re(root, ans):
            if root:
                ans.append(root.val)
                ans = re(root.left, ans)
                ans = re(root.right, ans)
            return ans

        return re(root, [])


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.right.right = TreeNode(6)
print Solution().preorderTraversal(root) #1 2 4 5 6 3
