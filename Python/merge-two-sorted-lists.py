# Time:  O(m+n), m and n is the length of each linked list
# Space: O(1)

# 21
# Merge two sorted linked lists and return it as a new list.
# The new list should be made by splicing together the nodes of the first two lists.
#

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)


class Solution(object):
    # iteration Time O(m+n), Space O(1)
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = tail = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 or l2
        return head.next

    # recursion Time O(m+n), Space O(m+n) 递归调用函数时需要消耗栈空间，栈空间的大小取决于递归调用的深度
    def mergeTwoLists2(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists2(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists2(l1, l2.next)
            return l2


if __name__ == "__main__":
    l1 = ListNode(0)
    l1.next = ListNode(1)
    l2 = ListNode (2)
    l2.next = ListNode(3)
    print(Solution().mergeTwoLists(l1, l2))
