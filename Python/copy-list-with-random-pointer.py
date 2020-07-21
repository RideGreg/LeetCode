# Time:  O(n)
# Space: O(1)
# 138
# A linked list is given such that each node contains an additional random pointer
# which could point to any node in the list or null.
#
# Return a deep copy of the list.
#

# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head): # although best space, too complex to make mistakes
        # copy and combine copied list with original list
        current = head
        while current:
            copied = RandomListNode(current.label)
            copied.next = current.next
            current.next = copied
            current = copied.next

        # update random node in copied list
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next

        # split copied list from combined one
        dummy = RandomListNode(0)
        copied_current, current = dummy, head
        while current:
            copied_current.next = current.next
            current.next = current.next.next
            copied_current, current = copied_current.next, current.next
        return dummy.next

# Time:  O(n)
# Space: O(n)
class Solution2:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):  # USE THIS: two steps, maintain mapping
        dummy = nhead = RandomListNode(-1)
        mapping = {}

        # copy a normal list without random pointer
        tmp = head
        while head:
            node = RandomListNode(head.val)
            mapping[head] = node
            nhead.next = node
            nhead, head = nhead.next, head.next

        head = tmp
        while head:
            if head.random:
                mapping[head].random = mapping[head.random]
            head = head.next
        return dummy.next

# time: O(n)
# space: O(n)
from collections import defaultdict

class Solution3(object):
    def copyRandomList(self, head): # very smart
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        clone = defaultdict(lambda: RandomListNode(0))
        clone[None] = None
        cur = head

        while cur:
            clone[cur].label = cur.label
            clone[cur].next = clone[cur.next]
            clone[cur].random = clone[cur.random]
            cur = cur.next

        return clone[head]

if __name__ == "__main__":
    head = RandomListNode(1)
    head.next = RandomListNode(2)
    head.random = head.next
    result = Solution().copyRandomList(head)
    print result.label
    print result.next.label
    print result.random.label


