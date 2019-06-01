# Time:  O(n)
# Space: O(h)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def bstToGstHelper(root):
            if not root:
                return root
            bstToGstHelper(root.right)
            self.prev = root.val = root.val + self.prev
            bstToGstHelper(root.left)
            return root
        
        self.prev = 0
        return bstToGstHelper(root)

    def bstToGst_noGlobalVar(self, root):
        def postOrder(n, sm):
            if not n:
                return sm
            nsm = postOrder(n.right, sm)
            n.val += nsm
            return postOrder(n.left, n.val)

        postOrder(root, 0)
        return root

root=TreeNode(4)
root.left, root.right = TreeNode(1), TreeNode(6)
root.left.left, root.left.right = TreeNode(0), TreeNode(2)
root.right.left, root.right.right = TreeNode(5), TreeNode(7)
root = Solution().bstToGst(root)
print(root.val)