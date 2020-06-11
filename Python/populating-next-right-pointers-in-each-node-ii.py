# Time:  O(n)
# Space: O(1)
# 117
# Follow up for problem "Populating Next Right Pointers in Each Node".
#
# What if the given tree could be any binary tree? Would your previous solution still work?
#
# Note:
#
# You may only use constant extra space.
# For example,
# Given the following binary tree,
#          1
#        /  \
#       2    3
#      / \    \
#     4   5    7
# After calling your function, the tree should look like:
#          1 -> NULL
#        /  \
#       2 -> 3 -> NULL
#      / \    \
#     4-> 5 -> 7 -> NULL
#

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
    def connect(self, root): # USE THIS
        head = root
        while head:
            prev, cur, next_head = None, head, None
            while cur:
                #if next_head is None:
                #    next_head = cur.left if cur.left else cur.right # cur.right may be None, ok to set by next node

                for node in [cur.left, cur.right]:
                    if node:
                        if prev:
                            prev.next = node
                        else:
                            next_head = node # only called once in each level
                        prev = node
                cur = cur.next
            head = next_head


if __name__ == "__main__":
    root, root.left, root.right = TreeNode(1), TreeNode(2), TreeNode(3)
    root.left.left, root.left.right, root.right.right = TreeNode(4), TreeNode(5), TreeNode(7)
    Solution().connect(root)
    print root
    print root.left
    print root.left.left
