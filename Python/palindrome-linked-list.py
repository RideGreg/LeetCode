# Time:  O(n)
# Space: O(1)
# 234
# Given a singly linked list, determine if it is a palindrome.
#
# Follow up:
# Could you do it in O(n) time and O(1) space?
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {boolean}

    # 避免使用 O(n)额外空间的方法就是改变输入!完成后应将链表恢复原样，因为使用该函数不应该更改链表结构。
    # 唯一缺点：并发环境下，函数运行时需要锁定其他线程或进程对链表的访问，因为在函数执执行过程中链表暂时断开。
    def isPalindrome(self, head):
        # Reverse the first half part of the list.
        pre, fast = None, head
        while fast and fast.next:
            fast = fast.next.next
            head.next, pre, head = pre, head, head.next

        # If the number of the nodes is odd,
        # set the head of the second half to the next of the median node.
        head2 = head.next if fast else head

        # Compare the reversed first half list with the second half list.
        # And restore the reversed first half list.
        is_palindrome = True
        while pre:
            is_palindrome = is_palindrome and pre.val == head2.val
            pre.next, pre, head = head, pre.next, pre
            head2 = head2.next

        return is_palindrome

    # 复制到数组中后用双指针法 Time O(n) Space O(n)
    #

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(1)
print(Solution().isPalindrome(head)) # True

head.next = ListNode(5)
print(Solution().isPalindrome(head)) # False
