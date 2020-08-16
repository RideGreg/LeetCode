# Time:  O(n)
# Space: O(1)

# 1474
# Given a linked list and two integers M and N. Traverse the linked list such that you retain M nodes
# then delete next N nodes, continue the same till end of the linked list.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "{}->{}".format(self.val,self.next)

class Solution(object):
    def deleteNodes(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        head = dummy = ListNode(next=head)
        while head:
            for _ in range(m):
                if not head.next:
                    return dummy.next
                head = head.next
                '''OR
                head = head.next
                if not head:
                    return dummy.next'''

            prev = head
            for _ in range(n):
                if not head.next:
                    prev.next = None
                    return dummy.next
                head = head.next
                ''' OR
                head = head.next
                if not head:
                    prev.next = None
                    return dummy.next'''
            prev.next = head.next
        return dummy.next

dummy = cur = ListNode(0)
for x in range(1, 6):
    cur.next = ListNode(x)
    cur = cur.next
print(Solution().deleteNodes(dummy.next, 2, 2)) # 1->2->5

dummy = cur = ListNode(0)
for x in range(1, 10):
    cur.next = ListNode(x)
    cur = cur.next
print(Solution().deleteNodes(dummy.next, 3, 2)) # 1->2->3->6->7->8

dummy = cur = ListNode(0)
for x in range(1, 11):
    cur.next = ListNode(x)
    cur = cur.next
print(Solution().deleteNodes(dummy.next, 1, 1)) # 1->3->5->7->9
