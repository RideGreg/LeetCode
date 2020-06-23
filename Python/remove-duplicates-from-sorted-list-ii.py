# Time:  O(n)
# Space: O(1)
# 82
# Given a sorted linked list, delete all nodes that have duplicate numbers,
#  leaving only distinct numbers from the original list.
#
# For example,
# Given 1->2->3->3->4->4->5, return 1->2->5.
# Given 1->1->1->2->3, return 2->3.
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self is None:
            return "Nil"
        else:
            return "{} -> {}".format(self.val, repr(self.next))

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = pre = ListNode(0) # head may need to be removed
        while head:
            if head.next and head.next.val == head.val: # skip over all dups
                val = head.val
                while head and head.val == val:
                    head = head.next
                pre.next = head
            else: # do not remove anything
                pre.next = head
                pre, head = head, head.next
        return dummy.next

if __name__ == "__main__":
    head, head.next, head.next.next = ListNode(1), ListNode(2), ListNode(3)
    head.next.next.next, head.next.next.next.next = ListNode(3), ListNode(4)
    head.next.next.next.next.next, head.next.next.next.next.next.next = ListNode(4), ListNode(5)
    print(Solution().deleteDuplicates(head)) # 1-2-5

