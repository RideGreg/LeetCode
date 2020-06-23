# Time:  O(n)
# Space: O(1)
# 24
# Given a linked list, swap every two adjacent nodes and return its head.
#
# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.
#
# Your algorithm should use only constant space.
# You may not modify the values in the list, only nodes itself can be changed.
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)

class Solution:
    # 把链表分为两部分，即奇数节点和偶数节点，first和second分别指交换节点中的前节点和后节点。
    # 除了完成它们的交换，还得用 pre 记录 first 的前驱节点。
    def swapPairs(self, head): # USE THIS
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        while head and head.next:
            first, second = head, head.next
            # swap
            pre.next = second
            first.next = second.next
            second.next = first
            # move forward
            pre, head = first, first.next
        return dummy.next

    def swapPairs_recur(self, head):
        if not head or not head.next:
            return head

        # Nodes to be swapped
        first, second = head, head.next
        # Swapping
        first.next = self.swapPairs(second.next)
        second.next = first

        return second

if __name__ == "__main__":
    head = ListNode(1)
    head.next, head.next.next, head.next.next.next = ListNode(2), ListNode(3), ListNode(4)
    print(Solution().swapPairs(head)) # 2-1-4-3
