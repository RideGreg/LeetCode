# Time:  O(n)
# Space: O(n)

# 1171
# Given the head of a linked list, we repeatedly delete consecutive sequences of nodes
# that sum to 0 until there are no such sequences.
#
# After doing so, return the head of the final linked list.  You may return any such answer.
#
import collections


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        return "{}->{}".format(self.val, self.next)

class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = dummy = ListNode(0)
        dummy.next = head
        prefix = 0
        lookup = collections.OrderedDict() # dict which remembers insert order
                                           # used to delete entry by insert order
        while curr:
            prefix += curr.val
            node = lookup.get(prefix, curr)
            node.next = curr.next # skip all nodes between [node.next, curr]

            while prefix in lookup: # remove mapping for nodes skipped
                lookup.popitem()    # last default to True
            lookup[prefix] = node # insert correct node: first node making prefix

            curr = curr.next
        return dummy.next

    def removeZeroSumSublists2(self, head):
        curr = dummy = ListNode(0)
        dummy.next = head
        lookup = {}
        # first pass to build hash: prefix : LAST node making prefix value
        prefix = 0
        while curr:
            prefix += curr.val
            lookup[prefix] = curr
            curr = curr.next
        # second pass to skip nodes between same prefix
        prefix, curr = 0, dummy
        while curr:
            prefix += curr.val
            curr.next = lookup[prefix].next
            curr = curr.next
        return dummy.next

dummy = cur = ListNode(None)
for x in [1,3,2,-3,-2,5,5,-5,1]:
    cur.next = ListNode(x)
    cur = cur.next
print(Solution().removeZeroSumSublists(dummy.next)) # 1->5->1

dummy = cur = ListNode(None)
for x in [1,2,-3,3,1]:
    cur.next = ListNode(x)
    cur = cur.next
print(Solution().removeZeroSumSublists(dummy.next)) # 3->1

dummy = cur = ListNode(None)
for x in [1,2,3,-3,4]:
    cur.next = ListNode(x)
    cur = cur.next
print(Solution().removeZeroSumSublists(dummy.next)) # 1->2->4

dummy = cur = ListNode(None)
for x in [1,2,3,-3,-2]:
    cur.next = ListNode(x)
    cur = cur.next
print(Solution().removeZeroSumSublists(dummy.next)) # 1
