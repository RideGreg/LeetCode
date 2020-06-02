# Time:  O(n)
# Space: O(1)

# 25
# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
#
# If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
#
# You may not alter the values in the nodes, only nodes itself may be changed.
#
# Only constant memory is allowed.
#
# For example,
# Given this linked list: 1->2->3->4->5
#
# For k = 2, you should return: 2->1->4->3->5
#
# For k = 3, you should return: 3->2->1->4->5
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))


# 本题目标清晰易懂，不涉及复杂的算法，但实现过程中需要考虑的细节较多，容易写出冗长的代码。主要考察面试者设计的能力。

# 我们把链表结点按照 k 个一组分组，可以使用一个指针 head 依次指向每组的头结点。这个指针每次向前移动 k 步找到tail指针，
# 直至链表结尾。对于每个分组，判断它的长度是否大于等于 k。若是，我们就翻转这部分链表，否则不需要翻转。

# 翻转一个分组内的子链表并不难，可以参考 206反转链表。但是对于一个子链表，除了翻转其本身之外，还需要将子链表的头部
# 与上一个子链表连接，以及子链表的尾部与下一个子链表连接。所以需要维护pre和nex结点。

class Solution: # USE THIS: revert sub linked list is very straightforward and easy to remember
    # 翻转子链表头尾之间所有结点的连接，并且返回新的头与尾
    def reverse(self, head: ListNode, tail: ListNode):
        prev, cur = head, head.next
        while prev != tail:
            next_cur = cur.next
            cur.next = prev # the only
            prev, cur = cur, next_cur
        return tail, head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        pre = dummy
        while head:
            # 确定tail，nex
            tail = pre
            for i in range(k): # 查看剩余部分长度是否大于等于 k
                tail = tail.next
                if not tail:
                    return dummy.next
            nex = tail.next

            # 翻转，并把子链表重新接回原链表 head and tail participate reverse
            # pre->head->......->tail->nex
            head, tail = self.reverse(head, tail)
            pre.next = head
            tail.next = nex

            # 确定新的pre，head
            pre, head = tail, tail.next

        return dummy.next


class Solution_kamyu:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        dummy = ListNode(-1)
        dummy.next = head
        orig_dummy = dummy
        cur = head
        length = 1

        while cur:
            next_cur = cur.next
            # suppose 1->2->3->4->5->6->7->8, cur is 1 (head) while length = 1
            # so when length = 0, cur is node 3,6...
            if length % k == 0:
                next_dummy = dummy.next
                self.reverse(dummy, cur.next)
                dummy = next_dummy # next_dummy already becomes the last node in the group just reverted

            cur = next_cur
            length += 1

        return orig_dummy.next

    # begin/end are boundaries, not participate reverse
    #          |---------->|
    # begin->first->cur->......->end
    #   |      |<___| |
    #   |____________>|
    def reverse(self, begin, end):
            first = begin.next
            cur = first.next

            while cur != end:
                first.next = cur.next
                cur.next = begin.next
                begin.next = cur
                cur = first.next


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print(Solution().reverseKGroup(head, 2))