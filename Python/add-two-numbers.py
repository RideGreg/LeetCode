# Time:  O(n)
# Space: O(1)
# 2
# You are given two linked lists representing two non-negative numbers.
# The digits are stored in reverse order and each of their nodes contain
# a single digit.
# Add the two numbers and return it as a linked list.
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
#

# FOLLOW UP: what if lists are in forward order 2->6->3 + 5->7 = 3->2->0

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return "{}->{}".format(self.val, self.next)


class Solution(object):
    # reverse order: LSB is at head, add starting from head
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        tail = dummy = ListNode(0)

        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            carry, v = divmod(carry, 10)
            tail.next = ListNode(v)
            tail = tail.next
        return dummy.next

    # FOLLOW UP: what if lists are in forward order 2->6->3 + 5->7 = 3->2->0. See 445
    # SOLUTION: 1. store list in stack/queue, add starting from the end: BEST
    # 2. reverse both list, add LSB lists, reverse: this MODIFIES the input list
    # 3. NOT WORKING: recursion bad if list lengths are not same


l1, l2 = ListNode(2), ListNode(5)
l1.next, l2.next = ListNode(4), ListNode(6)
l1.next.next, l2.next.next = ListNode(3), ListNode(4)
print(Solution().addTwoNumbers(l1, l2)) # 7->0->8->None
