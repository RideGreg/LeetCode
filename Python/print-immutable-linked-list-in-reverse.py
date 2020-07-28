# Time:  O(n)
# Space: O(sqrt(n))

# 1265
# You are given an immutable linked list, print out all values of each node in reverse with the help of the following interface:
# - ImmutableListNode: An interface of immutable linked list, you are given the head of the list.
# You need to use the following functions to access the linked list (you can't access the ImmutableListNode directly):
# - ImmutableListNode.printValue(): Print value of the current node.
# - ImmutableListNode.getNext(): Return the next node. The input is only given to initialize the linked list internally. You must solve this problem without modifying the linked list. In other words, you must operate the linked list using only the mentioned APIs.
#
# Follow up:
# Could you solve this problem in:
# 1. Constant space complexity?
# 2. Linear time complexity and less than linear space complexity?

# The length of the linked list is between [1, 1000].
# The value of each node in the linked list is between [-1000, 1000].

import math

class ImmutableListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def getNext(self):
        return self.next
    def printValue(self):
        print(self.val)

class Solution(object):
    # Solution 2 is to put all nodes in 1 bucket, need a O(n) stack to print the nodes in bucket.
    # Solution 1 is to divide all nodes into sqrt(n) buckets, each bucket includes sqrt(n) nodes, need a O(sqrt(n)) stack to print.
    def printLinkedListInReverse(self, head):
        """
        :type head: ImmutableListNode
        :rtype: None
        """
        def print_nodes(head, count): # similar to the core function in solution 2, use stack to print
            nodes = []
            while head and len(nodes) != count:
                nodes.append(head)
                head = head.getNext()
            for node in reversed(nodes):
                node.printValue()

        # find sqrt(n)
        curr, count = head, 0
        while curr:
            curr = curr.getNext()
            count += 1
        bucket_count = math.ceil(count**0.5)
        
        curr, count, bucket_heads = head, 0, []
        while curr:
            if count % bucket_count == 0:
                bucket_heads.append(curr)
            curr = curr.getNext()
            count += 1
        for head in reversed(bucket_heads):
            print_nodes(head, bucket_count)
            
        
# Time:  O(n)
# Space: O(n)
class Solution2(object):
    def printLinkedListInReverse(self, head):
        """
        :type head: ImmutableListNode
        :rtype: None
        """
        nodes = []
        while head:
            nodes.append(head)
            head = head.getNext()
        for node in reversed(nodes):
            node.printValue()


# Time:  O(n^2)
# Space: O(1)
class Solution3(object):
    def printLinkedListInReverse(self, head):
        """
        :type head: ImmutableListNode
        :rtype: None
        """
        tail = None
        while head != tail:
            curr = head
            while curr.getNext() != tail:
                curr = curr.getNext()
            curr.printValue()
            tail = curr

dummy = cur = ImmutableListNode(None)
for x in range(10):
    cur.next = ImmutableListNode(x)
    cur = cur.next

print(Solution().printLinkedListInReverse(dummy.next)) #