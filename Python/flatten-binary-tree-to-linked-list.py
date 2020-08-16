# Time:  O(n)
# Space: O(1)

# 114
# Given a binary tree, flatten it to a linked list in-place.
#
# (Flatten a binary tree to a fake "linked list" in pre-order traversal.
# Here we use the right pointer in TreeNode as the next pointer in ListNode.)
#
# For example,
# Given
#
#          1
#         / \
#        2   5
#       / \   \
#      3   4   6
# The flattened tree should look like:
#    1
#     \
#      2
#       \
#        3
#         \
#          4
#           \
#            5
#             \
#              6
#

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __repr__(self): # print right child only
        return '{}->{}'.format(self.val, self.right)


# 寻找前驱节点 similar to Morris Algo
# 对于当前节点，如果其左子节点不为空，则在其左子树中找到最右边的节点，作为前驱节点，将当前节点的右子节点赋给前驱节点的右子节点，
# 然后将当前节点的左子节点改为当前节点的右子节点，并将当前节点的左子节点设为空。继续处理链表中的下一个节点，直到所有节点都处理结束。
class Solution:  # USE THIS
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        while root:
            if root.left:      # if left subtree is not empty, fold into right subtree. Repeat folding.
                pre = root.left
                while pre.right:
                    pre = pre.right

                pre.right = root.right
                root.right = root.left
                root.left = None
            root = root.right

# modified postOrder (right->left->parent), maintain the 'tail' var (always update tail as current processed node)
# preOrder NOT work for this problem, because when changing cur.right as cur.left, we lost the right subtree!
class Solution2: # also very good Time O(n) Space O(h)
    def flatten(self, root):
        def postOrder(node):
            if node:
                postOrder(node.right)
                postOrder(node.left)
                node.right = self.tail
                node.left = None
                self.tail = node

        self.tail = None
        postOrder(root)

class Solution3: # same to solution 2 but not use global var (passing param instead, not pretty, don't use)
    def flatten(self, root):
        self.flattenRecu(root, None)

    def flattenRecu(self, root, list_head):
        if root:
            list_head = self.flattenRecu(root.right, list_head)
            list_head = self.flattenRecu(root.left, list_head)
            root.right = list_head
            root.left = None
            return root
        else:
            return list_head

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right = TreeNode(5)
    root.right.right = TreeNode(6)

    Solution().flatten(root)
    print(root) # 1->2->3->4->5->6->None
