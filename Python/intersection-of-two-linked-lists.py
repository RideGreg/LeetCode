# Time:  O(m + n)
# Space: O(1)
#
# Write a program to find the node at which the intersection of two singly linked lists begins.
#
#
# For example, the following two linked lists:
#
# A:          a1 - a2
#                    \
#                      c1 - c2 - c3
#                    /
# B:     b1 - b2 - b3
# begin to intersect at node c1.
#
#
# Notes:
#
# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode

    # Brute Force: T:O(mn) S:O(1) for each node in A, scan B to check if there is a same node
    # Hash Table: T:O(m+n) S:O(m) store each node of A in hash table, then scan B.
    #  Two Pointers: T:O(m+n) S:O(1)
    def getIntersectionNode(self, headA, headB): # USE THIS
        curA, curB = headA, headB
        while curA != curB:    # will meet at shared node or null node
            curA = curA.next if curA else headB
            curB = curB.next if curB else headA
        return curA


    def getIntersectionNode2(self, headA, headB): # same idea, but more verbose
        curA, curB = headA, headB
        finishA = finishB = False

        # concatenate 2 linked lists. Will meet if they share the same node
        # a->c->e->f --连上-> b->'e'->f
        # b->e->f --连上-> a->c->'e'->f
        while curA and curB:
            if curA == curB:
                return curA

            if curA.next:
                curA = curA.next
            elif not finishA:
                finishA = True
                curA = headB
            else:
                break

            if curB.next:
                curB = curB.next
            elif not finishB:
                finishB = True
                curB = headA
            else:
                break

        return None



d = ListNode(5)
d.next = ListNode(10)

a = ListNode(1)
a.next = ListNode(2)
a.next.next = d

c = ListNode(100)
c.next = d
print(Solution().getIntersectionNode(a, c).val) # 5

aa = ListNode(11)
aa.next = ListNode(22)
cc = ListNode(111)
print(Solution().getIntersectionNode(aa, cc)) # None

print(Solution().getIntersectionNode(a, None)) # None