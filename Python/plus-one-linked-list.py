# Time:  O(n)
# Space: O(1)

# 369
# Given a non-negative integer represented as non-empty a singly linked list of digits,
# plus one to the integer.
# You may assume the integer do not contain any leading zero, except the number 0 itself.
# The digits are stored such that the most significant digit is at the head of the list.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        return "{}->{}".format(self.val, self.next)

class Solution(object):
    def plusOne(self, head): # USE THIS: recursive (for iterative, use stack)
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def recur(node):
            if not node: return 1

            carry = recur(node.next)
            if carry:
                carry, node.val = divmod(node.val + carry, 10)
            return carry

        carry = recur(head)
        if carry:
            newNode = ListNode(1)
            newNode.next = head
            return newNode
        return head

    # reverse twice
    # Time:  O(n), Space: O(1)
    def plusOne2(self, head):
        def reverseList(head):
            pre = None
            while head:
                head.next, pre, head = pre, head, head.next
            return pre

        rev_head = reverseList(head)
        curr, carry = rev_head, 1
        while carry:
            carry, curr.val = divmod(curr.val + carry, 10)
            if carry and curr.next is None:
                curr.next = ListNode(1)
                break
            curr = curr.next

        return reverseList(rev_head)

    # Two pointers solution.
    def plusOne3(self, head): # hard to understand
        if not head:
            return None

        dummy = ListNode(0)
        dummy.next = head

        left, right = dummy, head
        while right.next:
            if right.val != 9:
                left = right
            right = right.next

        if right.val != 9:
            right.val += 1
        else:
            left.val += 1
            right = left.next
            while right:
                right.val = 0
                right = right.next

        return dummy if dummy.val else dummy.next


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
print(Solution().plusOne(head)) # 1->2->4->None

head = ListNode(9)
head.next = ListNode(9)
print(Solution().plusOne(head)) # 1->0->0->None