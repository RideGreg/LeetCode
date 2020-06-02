# Time:  O(n)
# Space: O(1)

# 142
# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
#
# Follow up:
# Can you solve it without using extra space?
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        if self:
            return "{}".format(self.val)
        else:
            return None

class Solution:
    # @param head, a ListNode
    # @return a list node

    # Assume circle length = C, # of nodes before circle is F. Assume when slow pointer
    # arrives entry of circle, fast pointer is at h on the circle => 2F = F+nC+h => F = nC+h.
    # Let slow pointer proceeds C-h, fast pointer will be h+2(C-h), so they fist MEET at
    # a node C-h away to circle entry.
    # Move slow pointer back to head, let both proceed F at same speed; slow pointer arrvies
    # circle entry and fast pointer's distance to cicle entry is C-h + F= C-h + nC+h = nC,
    # so they now MEET at circle entry.
    def detectCycle(self, head): # USE THIS Floyd Algorithm
        fast, slow = head, head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
            if fast is slow:
                fast = head
                while fast is not slow:
                    fast, slow = fast.next, slow.next
                return fast
        return None

    # Hash Table: Time O(n), Space O(n)
    def detectCycle2(self, head):
        visited = set()
        node = head
        while node is not None:
            if node in visited:
                return node

            visited.add(node)
            node = node.next
        return None


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = head.next
    print Solution().detectCycle(head)