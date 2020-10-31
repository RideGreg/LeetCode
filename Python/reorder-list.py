# Time:  O(n)
# Space: O(1)
#
# Given a singly linked list L: L0->L1->...->Ln-1->Ln,
# reorder it to: L0->Ln->L1->Ln-1->L2->Ln-2->...
#
# You must do this in-place without altering the nodes' values.
#
# For example,
# Given {1,2,3,4}, reorder it to {1,4,2,3}.
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))


# cut in middle, revert second half, concatenate two lists into one
class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if head == None or head.next == None:
            return head

        # slow is middle node (odd total) or start of 2nd half (even total)
        # prev is node before slow for cutting in middle
        fast = slow = head
        prev = None
        while fast and fast.next:
            fast, slow, prev = fast.next.next, slow.next, slow
        prev.next = None

        # revert second half: let curr point to prev, then going forward
        prev = None
        while slow:
            slow.next, prev, slow = prev, slow, slow.next

        # concatenate two lists
        tail = prev
        while head and tail:
            head.next, head = tail, head.next
            if head:
                tail.next, tail = head, tail.next
        ''' alternatively 
        l1, l2 = head, prev
        dummy = curr = ListNode(0)

        while l1 and l2:
            curr.next = l1
            curr, l1 = curr.next, l1.next
            curr.next = l2
            curr, l2 = curr.next, l2.next
        dummy.next = None
        del dummy'''

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    Solution().reorderList(head)
    print(head) # 1 -> 5 -> 2 -> 4 -> 3 -> None

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    Solution().reorderList(head)
    print(head) # 1 -> 6 -> 2 -> 5 -> 3 -> 4 -> None