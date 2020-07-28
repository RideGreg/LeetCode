# Time:  O(n + k)
# Space: O(1)

# Given a (singly) linked list with head node root,
# write a function to split the linked list into k consecutive linked list "parts".
#
# The length of each part should be as equal as possible:
# no two parts should have a size differing by more than 1.
# This may lead to some parts being null.
#
# The parts should be in order of occurrence in the input list,
# and parts occurring earlier should always have a size greater than or equal parts occurring later.
#
# Return a List of ListNode's representing the linked list parts that are formed.
#
# Examples 1->2->3->4, k = 5 // 5 equal parts [ [1], [2], [3], [4], null ]
# Example 1:
# Input:
# root = [1, 2, 3], k = 5
# Output: [[1],[2],[3],[],[]]
# Explanation:
# The input and each element of the output are ListNodes, not arrays.
# For example, the input root has root.val = 1, root.next.val = 2, \root.next.next.val = 3,
# and root.next.next.next = null.
# The first element output[0] has output[0].val = 1, output[0].next = null.
# The last element output[4] is null, but it's string representation as a ListNode is [].
#
# Example 2:
# Input:
# root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
# Output: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
# Explanation:
# The input has been split into consecutive parts with size difference at most 1,
# and earlier parts are a larger size than the later parts.
#
# Note:
# - The length of root will be in the range [0, 1000].
# - Each value of a node in the input will be an integer in the range [0, 999].
# - k will be an integer in the range [1, 50].
#
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        return "{}->{}".format(self.val, self.next)

class Solution(object):
    def splitListToParts(self, root, k): # USE THIS: append at the beginning
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        cur, size = root, 0
        while cur:
            size += 1
            cur = cur.next
        width, remainder = divmod(size, k)

        pre = ListNode(None)
        pre.next = root
        ans = [None] * k
        for i in range(k):
            if not pre: break

            ans[i] = pre.next
            pre.next, pre = None, ans[i]
            for _ in range(width - 1 + int(i < remainder)):
                if pre:
                    pre = pre.next
        return ans

    def splitListToParts_kamyu(self, root, k): # remember and append at the end
        n, curr = 0, root
        while curr:
            curr = curr.next
            n += 1
        width, remainder = divmod(n, k)

        result = []
        curr = root
        for i in xrange(k):
            head = curr
            for j in xrange(width-1+int(i < remainder)):
                if curr:
                    curr = curr.next
            if curr:
                curr.next, curr = None, curr.next
            result.append(head)
        return result

root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
print(Solution().splitListToParts(root, 5)) # [1,2,3,None, None]

dummy = cur = ListNode(None)
for i in range(1, 11):
    cur.next = ListNode(i)
    cur = cur.next
print(Solution().splitListToParts(dummy.next, 3)) # [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]