# Time:  O(n)
# Space: O(1)

# 328
# Given a singly linked list, group all odd nodes
# together followed by the even nodes.
# Please note here we are talking about the node number
# and not the value in the nodes.
#
# You should try to do it in place. The program should run
# in O(1) space complexity and O(nodes) time complexity.
#
# Example:
# Given 1->2->3->4->5->NULL,
# return 1->3->5->2->4->NULL.
#
# Note:
# The relative order inside both the even and odd groups
# should remain as it was in the input.
# The first node is considered odd, the second node even
# and so on ...

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# 直觉: 奇节点放在一个链表里，偶节点放在另一个链表里，然后连接。
# 一个 LinkedList 需要一个头指针和一个尾指针来支持双端操作。我们用变量 head 和 odd(迭代) 保存奇链表的头和尾指针。
# evenHead 和 even(迭代) 保存偶链表的头和尾指针。

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head:
            odd = head
            even = even_head = head.next

            while even and even.next:
                odd.next = even.next
                odd = odd.next
                even.next = odd.next
                even = even.next

            odd.next = even_head
        return head

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
print(Solution().oddEvenList(head)) # 1 3 2

head.next.next.next = ListNode(4)
print(Solution().oddEvenList(head)) # 1 3 2 4

head.next.next.next.next = ListNode(5)
print(Solution().oddEvenList(head)) # 1 3 5 2 4

head.next.next.next.next.next = ListNode(6)
print(Solution().oddEvenList(head)) # 1 3 5 2 4 6