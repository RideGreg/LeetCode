# Time:  O(m + n), m is the number of G, n is the number of nodes
# Space: O(m)

# We are given head, the head node of a linked list
# containing unique integer values.
#
# We are also given the list G, a subset of the values in the linked list.
#
# Return the number of connected components in G,
# where two values are connected if they appear consecutively
# in the linked list.
#
# Example 1:
#
# Input:
# head: 0->1->2->3
# G = [0, 1, 3]
# Output: 2
# Explanation:
# 0 and 1 are connected, so [0, 1] and [3] are the two connected components.
# Example 2:
#
# Input:
# head: 0->1->2->3->4
# G = [0, 3, 1, 4]
# Output: 2
# Explanation:
# 0 and 1 are connected, 3 and 4 are connected, so [0, 1] and [3, 4] are
# the two connected components.
# Note:
# - If N is the length of the linked list given by head, 1 <= N <= 10000.
# - The value of each node in the linked list will be in the range [0, N - 1].
# - 1 <= G.length <= 10000.
# - G is a subset of all values in the linked list.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        lookup = set(G)
        dummy = ListNode(-1)
        dummy.next = head
        curr = dummy
        result = 0
        while curr and curr.next:
            if curr.val not in lookup and curr.next.val in lookup:
                result += 1
            curr = curr.next
        return result


    # Compress into groups.
    def numComponents_ming(self, head, G): # USE THIS
        gset = set(G)
        ans = len(G)
        while head and head.next:
            if head.val in gset and head.next.val in gset:
                ans -= 1
            head = head.next
        return ans


    # Set + Two Pointers: two pointers (pre, head) traverse linked list, while pre not in G and head in G, increment counters.
    def numComponents_bookshadow(self, head, G):
        gs = set(G)
        ans = 0
        pre = ListNode(None)
        while head:
            ans += pre.val not in gs and head.val in gs
            pre = head
            head = head.next
        return ans


    # Union_find: working but not necessary.
    class UnionFind(object):
        def __init__(self, cnt, n):
            self.count = cnt
            self.id = range(n)

        def union(self, x, y):
            xRoot, yRoot = map(self.find, (x, y))
            if xRoot != yRoot:
                self.id[min(xRoot, yRoot)] = max(xRoot, yRoot)
                self.count -= 1

        def find(self, x):
            if self.id[x] != x:
                self.id[x] = self.find(self.id[x])
            return self.id[x]

    def numComponents_unionfind(self, head, G):
        gset = set(G)
        uf = UnionFind(len(G), max(G)+1)

        while head and head.next:
            if head.val in gset and head.next.val in gset:
                uf.union(head.val, head.next.val)
            head = head.next

        return uf.count

head = ListNode(0)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
print Solution().numComponents(head, [0,2,4])