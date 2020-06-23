# Time:  O(nlogk)
# Space: O(1)

# Merge k sorted linked lists and return it as one sorted list.
# Analyze and describe its complexity.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):		
        if self:		
            return "{} -> {}".format(self.val, self.next)

    def __lt__(self, other):
        return True
    def __le__(self, other):
        return True

# Time:  O(knlogk) 优先队列中的元素不超过 k个，那么插入和删除的时间代价为O(logk)，最多有kn 个点，每个点都被插入删除各一次
# Space: O(k)
# Heap solution.
import heapq
class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists): # USE THIS
        dummy = ListNode(0)
        current = dummy

        heap = []
        for l in lists:
            if l:
                heapq.heappush(heap, (l.val, id(l), l))
                # Below triggers TypeError: '<' not supported between instances of 'ListNode' and 'ListNode'
                # so use the trick adding id(l) to avoid compare object, or implement __lt__ __le__ in obj class,
                # but that won't work in online judge where obj class is predefined.
                #heapq.heappush(heap, (l.val, l))

        while heap:
            smallest = heapq.heappop(heap)[-1]
            current.next = smallest
            current = current.next
            if smallest.next:
                heapq.heappush(heap, (smallest.next.val, id(smallest.next), smallest.next))
                #heapq.heappush(heap, (smallest.next.val, smallest.next))

        return dummy.next

    # similar to heap solution, but self made way to get minNode. Time not good O(k*kn)
    # each time take k to merge one node, total kn nodes.
    def mergeKLists_selfCompare(self, lists):
        prehead = tail = ListNode(0)
        while any(l for l in lists):
            mn, mn_id = float('inf'), None
            for i in range(len(lists)):
                if lists[i] and lists[i].val < mn:
                    mn, mn_id = lists[i].val, i
            tail.next = lists[mn_id]
            tail = tail.next
            lists[mn_id] = lists[mn_id].next
        return prehead.next


# Merge two solutions. Both are O(kkn) where n is 假设每个链表的最长长度是 n, k is # of lists.
class Solution3(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def mergeTwoLists(l1, l2):
            curr = dummy = ListNode(0)
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            curr.next = l1 or l2
            return dummy.next

        if not lists:
            return None
        left, right = 0, len(lists) - 1;
        while right > 0:
            if left >= right:
                left = 0
            else:
                lists[left] = mergeTwoLists(lists[left], lists[right])
                left += 1
                right -= 1
        return lists[0]

    def mergeKLists_timeNotGood(self, lists):
        dummy = cur = ListNode(-1)
        lists = [l for l in lists if l]
        while len(lists) > 1:
            minNode = min(lists, key = lambda n: n.val)
            cur.next = minNode
            cur = cur.next
            i = lists.index(minNode)
            if lists[i].next:
                lists[i] = lists[i].next
            else:
                lists.pop(i)
        if lists:
            cur.next = lists[0]
        return dummy.next

# Time:  O(nklogk)
# Space: O(logk)
# Divide and Conquer solution.
class Solution2:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        def mergeTwoLists(l1, l2):
            curr = dummy = ListNode(0)
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            curr.next = l1 or l2
            return dummy.next

        def mergeKListsHelper(lists, begin, end):
            if begin > end:
                return None
            if begin == end:
                return lists[begin]
            return mergeTwoLists(mergeKListsHelper(lists, begin, (begin + end) / 2), \
                                 mergeKListsHelper(lists, (begin + end) / 2 + 1, end))

        return mergeKListsHelper(lists, 0, len(lists) - 1)



if __name__ == "__main__":
    list1 = ListNode(1)
    list1.next = ListNode(3)
    list2 = ListNode(1)
    list2.next = ListNode(4)

    print(Solution().mergeKLists([list1, list2]))
