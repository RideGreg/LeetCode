# Time:  O(n)
# Space: O(1)
#
# Given a list, rotate the list to the right by k places, where k is non-negative.
#
# For example:
# Given 1->2->3->4->5->NULL and k = 2,
# return 4->5->1->2->3->NULL.
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))

class Solution(object):
    def rotateRight(self, head, k): # USE THIS: fast+slow pointers
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head: return None
        cur, sz = head, 0
        while cur:
            cur = cur.next
            sz += 1

        k %= sz
        if k != 0:
            slow, fast = head, head
            for _ in range(k):
                fast = fast.next

            while fast.next:
                fast = fast.next
                slow = slow.next
            fast.next = head
            head = slow.next
            slow.next = None
        return head


    def rotateRight2(self, head, k): # get and use tail
        if not head or not head.next:
            return head

        n, tail = 1, head
        while tail.next:
            tail = tail.next
            n += 1
        if k % n == 0:
            return head

        tail.next = head
        cur = head
        for _ in xrange(n - k % n):
            tail = cur
            cur = cur.next
        tail.next = None

        return cur


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print Solution().rotateRight(head, 2)
