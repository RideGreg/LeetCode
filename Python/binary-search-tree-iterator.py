# Time:  O(1)
# Space: O(h), h is height of binary tree
#
# Implement an iterator over a binary search tree (BST).
# Your iterator will be initialized with the root node of a BST.
#
# Calling next() will return the next smallest number in the BST.
#
# Note: next() and hasNext() should run in average O(1) time
# and uses O(h) memory, where h is the height of the tree.
#


# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 把所有节点按中序遍历放入栈需要O(n) space。我们使用自定义的栈，只存O(h)节点，按需要暂停和重启中序遍历。
class BSTIterator_bookshadow(object):   # USE THIS, very clean
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stack = []
        self.pushLeft(root)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return self.stack

    # @return an integer, the next smallest number
    def next(self):
        cur = self.stack.pop()
        self.pushLeft(cur.right)

    def pushLeft(self, node):
        while node:
            self.stack.append(node)
            node = node.left
        return cur.val


# Time O(h) Space O(1) same algorithm as in inorder-successor-in-bst.py
class BSTIterator_ming(object):
    def __init__(self, root):
        self.root = root

        while root and root.left:
            root = root.left
        self.cur = root

    def hasNext(self):
        return self.cur

    def next(self):
        ans = self.cur.val
        if self.cur.right:
            self.cur = self.cur.right
            while self.cur.left:
                self.cur = self.cur.left
            return ans

        nextNode, r = None, self.root
        while r and r != self.cur:
            if self.cur.val < r.val:
                nextNode = r
                r = r.left
            else:
                r = r.right
        self.cur = nextNode
        return ans