# Time:  O(m + n)
# Space: O(m + n)

# 445
# You are given two linked lists representing two non-negative numbers.
# The most significant digit comes first and each of their nodes contain
# a single digit.
# Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero,
# except the number 0 itself.
#
# Follow up:
# What if you cannot modify the input lists? In other words,
# reversing the lists is not allowed.
#
# Example:
#
# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7

# 本题的主要难点在于链表中数位的顺序与我们做加法的顺序是相反的，为了*逆序*处理所有数位，
# 我们可以使用栈：把所有数字压入栈中，再依次取出相加。

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x = 0, next = None):
        self.val = x
        self.next = next
    def __repr__(self):
        return "{}->{}".format(self.val, self.next)

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        stk1, stk2 = [], []
        while l1:
            stk1.append(l1.val)
            l1 = l1.next
        while l2:
            stk2.append(l2.val)
            l2 = l2.next

        head, carry = None, 0
        while stk1 or stk2 or carry:
            if stk1:
                carry += stk1.pop()
            if stk2:
                carry += stk2.pop()

            carry, v = divmod(carry, 10)
            cur = ListNode(v, head)
            head = cur
        return head


    # result list can be built from back to front, not need final reverse.
    def addTwoNumbers_reverseInput(self, l1, l2):
        def reverse(l):
            prev = None
            while l:
                l.next, prev, l = prev, l, l.next
            return prev

        l1r, l2r = reverse(l1), reverse(l2)
        head, c = None, 0
        while l1r or l2r or c:
            if l1r:
                c += l1r.val
                l1r = l1r.next
            if l2r:
                c += l2r.val
                l2r = l2r.next
            
            c, v = divmod(c, 10)
            cur = ListNode(v, head)
            head = cur
        return head


l1 = ListNode(7)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l1.next.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

ans = Solution().addTwoNumbers(l1, l2)
print(ans) # 7 -> 8 -> 0 -> 7
