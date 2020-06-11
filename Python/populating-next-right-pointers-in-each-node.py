# Time:  O(n)
# Space: O(1)
# 116
# You are given a PERFECT BINARY TREE where all leaves are on the same level, and every parent has two children.
# The binary tree has the following definition:
#     struct TreeLinkNode {
#       TreeLinkNode *left;
#       TreeLinkNode *right;
#       TreeLinkNode *next;
#     }
# Populate each next pointer to point to its next right node. If there is no next right node,
# the next pointer should be set to NULL.
#
# Initially, all next pointers are set to NULL.
#
# Note:
#
# You may only use constant extra space.
# Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
#
# For example,
# Given the following perfect binary tree,
#          1
#        /  \
#       2    3
#      / \  / \
#     4  5  6  7
# After calling your function, the tree should look like:
#          1 -> NULL
#        /  \
#       2 -> 3 -> NULL
#      / \  / \
#     4->5->6->7 -> NULL

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

    def __repr__(self):
        if self is None:
            return "Nil"
        else:
            return "{} -> {}".format(self.val, repr(self.next))

class Solution:
    # @param root, a tree node
    # @return nothing

    # 使用已建立的 next 指针
    def connect(self, root): # USE THIS
        head = root
        while head:
            cur = head
            while cur and cur.left:
                cur.left.next = cur.right
                if cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next   # iterate right
            head = head.left     # iterate down

    # level order traverse works. dfs with depth info works. But both take extra space.
    # 层序遍历 Time O(n) Space O(n)

    # 树和图的两种基本遍历方法。一种是深度优先方法，例如：每次只遍历一个分支；另外一种是广度优先方法，例如：先遍历完这一层
    # 再进入下一层。树的深度优先遍历又可以分为preorder、inorder 和postorder。树的广度优先遍历基于节点的层级 level 概念。
    # 使用队列queue可以通过多种方式实现层序遍历，尤其是在在识别特定节点的时候：
    # 1. 在队列中以 (node,level) 的形式存储节点，同时存储其子节点为(node.left, parent_level+1) 和 (node.right, parent_level+1)。
    # 这种方法节点多了一个层级属性，需要创建一个新的数据结构，*效率很低*。
    # 2. 使用一个标记分离不同层级之间的节点。通常在队列中插入一个 NULL 元素，标记当前层级结束，下一层级开始。
    # 但是这种方法会创建与层级数量相同个数的 NULL 元素，造成过多内存消耗。
    # 3. 使用嵌套循环结构，避免了方法二中的 NULL 元素。该方法每一步都需要记录当前队列中全部元素数量，对应树中一个层级
    # 元素的数量。然后从队列中处理对应数量的元素。完成后，这一层级所有的节点都被访问，队列包含下一层级的全部 节点 - GOOD！

    def connect_level(self, root: 'Node') -> 'Node':
        if not root:
            return root

        Q = collections.deque([root])
        while Q:
            size = len(Q)
            for i in range(size):
                node = Q.popleft()
                if i < size - 1:
                    node.next = Q[0]

                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
        return root

    def connect_levelOrder2(self, root: 'Node') -> 'Node': # not good, each level allocate a new list
        if not root: return root
        level = [root]
        while level:
            nxt = []
            for i in range(len(level)):
                if level[i].left:
                    nxt.append(level[i].left)
                if level[i].right:
                    nxt.append(level[i].right)
                if i > 0:
                    level[i-1].next = level[i]
            level = nxt
        return root

# Time:  O(n)
# Space: O(logn)
# recusion
class Solution2:
    # @param root, a tree node
    # @return nothing
    def connect(self, root): #top-down recursion
        if root is None:
            return
        if root.left:
            root.left.next = root.right
        if root.right and root.next:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)

if __name__ == "__main__":
    root, root.left, root.right = TreeNode(1), TreeNode(2), TreeNode(3)
    root.left.left, root.left.right, root.right.left, root.right.right = TreeNode(4), TreeNode(5), TreeNode(6), TreeNode(7)
    Solution().connect(root)
    print root
    print root.left
    print root.left.left

