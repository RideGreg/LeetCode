# Time:  O(n)
# Space: O(1)
#
# Reverse a singly linked list.
#
# click to show more hints.
#
# Hint:
# A linked list can be reversed either iteratively or recursively. Could you implement both?
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))

# Iterative solution.
# 遍历列表，将当前节点的next指针改为指向前一个元素。由于节点没有引用其上一个节点，因此须事先
# 存储其前一个元素。在更改引用之前，还需要另一个指针来存储下一个节点。记住在最后返回新的头引用！
#
class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head): # USE THIS: no extra space
        prev, cur = None, head
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev

    # Time:  O(n)
    # Space: O(n), calling stack
    # Recursive solution. Another way to save all nodes in a stack.
    def reverseList_recur(self, head):
        def revert(node):
            if not node or not node.next: # not node is for edge case input is None
                return node, node

            h, tail = revert(node.next)
            node.next = None   # KENG: if don't cut node->tail, it is a dead loop!!
            tail.next = node
            return h, node

        return revert(head)[0]

    def reverseList_recur2(self, head): # very concise, but not easy to follow
        if not head or not head.next:
            return head

        newHead = self.reverseList_recur(head.next)
        head.next.next = head
        head.next = None
        return newHead


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print(Solution().reverseList(head)) # 5->4->3->2->1->None