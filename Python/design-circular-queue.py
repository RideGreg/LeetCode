# Time:  O(1)
# Space: O(k)

# 622
# Design your implementation of the circular queue.
# The circular queue is a linear data structure in which
# the operations are performed based on FIFO (First In First Out)
# principle and the last position is connected back to
# the first position to make a circle. It is also called ‘Ring Buffer’.
# One of the Benefits of the circular queue is that
# we can make use of the spaces in front of the queue.
# In a normal queue, once the queue becomes full, 
# we can not insert the next element even if there is a space in front of the queue.
# But using the circular queue, we can use the space to store new values.
# Your implementation should support following operations:
#
# MyCircularQueue(k): Constructor, set the size of the queue to be k.
# Front: Get the front item from the queue. If the queue is empty, return -1.
# Rear: Get the last item from the queue. If the queue is empty, return -1.
# enQueue(value): Insert an element into the circular queue. Return true if the operation is successful.
# deQueue(): Delete an element from the circular queue. Return true if the operation is successful.
# isEmpty(): Checks whether the circular queue is empty or not.
# isFull(): Checks whether the circular queue is full or not.
# Example:
#
# MyCircularQueue circularQueue = new MycircularQueue(3); # set the size to be 3
# circularQueue.enQueue(1);  # return true
# circularQueue.enQueue(2);  # return true
# circularQueue.enQueue(3);  # return true
# circularQueue.enQueue(4);  # return false, the queue is full
# circularQueue.Rear();  # return 3
# circularQueue.isFull();  # return true
# circularQueue.deQueue();  # return true
# circularQueue.enQueue(4);  # return true
# circularQueue.Rear();  # return 4
#
# Note:
# - All values will be in the range of [1, 1000].
# - The number of operations will be in the range of [1, 1000].
# - Please do not use the built-in Queue library.


# 设计数据结构的关键是如何设计属性，好的设计属性数量更少。
# - 属性数量少说明属性之间冗余更低。
# - 属性冗余度越低，操作逻辑越简单，发生错误的可能性更低。
# - 属性数量少，使用的空间也少，操作性能更高。
#
# 但是，也不建议使用最少的属性。一定的冗余可以降低操作的时间复杂度，达到时间复杂度和空间复杂度的相对平衡。
#
# 根据以上原则，列举循环队列的每个属性，并解释其含义。
# queue：一个固定大小的数组，用于保存循环队列的元素。
# headIndex：一个整数，保存队首 head 的索引。
# count：循环队列中的元素数量。用hadIndex和count可计算出队尾元素的索引，因此不需要队尾属性。

# 方法一：数组
# 根据问题描述，需要一个首尾相连的环。
# 任何数据结构中都不存在环形结构，但是可以使用一维 数组 模拟，通过操作数组的索引构建一个虚拟的环。
# 很多复杂数据结构都可以通过数组实现。对于一个固定大小的数组，任何位置都可以是队首，另外要知道队列长度。
#
from threading import Lock # for thread safety

class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.start = 0
        self.cnt = 0
        self.q = [0] * k
        self.queueLock = Lock() # for thread safety

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        # automatically acquire the lock when entering the block
        with self.queueLock:
            if self.isFull():
                return False
            pos = (self.start+self.cnt) % len(self.q)
            self.q[pos] = value
            self.cnt += 1
        # automatically release the lock when leaving the block
        return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.start = (self.start+1) % len(self.q)
        self.cnt -= 1
        return True

    def Front(self):
        """ Get the front item from the queue.
        :rtype: int
        """
        return -1 if self.isEmpty() else self.q[self.start]

    def Rear(self):
        """ Get the last item from the queue.
        :rtype: int
        """
        return -1 if self.isEmpty() else self.q[(self.start+self.cnt-1) % len(self.q)]

    def isEmpty(self):
        """ Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.cnt == 0

    def isFull(self):
        """ Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return self.cnt == len(self.q)


# FOLLOW UP: 线程安全
# 从并发性来看，该循环队列是线程不安全的。举例race condition: 假设queue还差一个位置到full,
# thread 1 and thread 2 同时call enQueue(), both call pass the full check and write the empty slot
# and increment count, so the empty slot will be overwritten and count becomes larger than capacity.

#  Timeline     Thread 1      Thread 2
#  1            enQueue
#  2                          enQueue
#  3           if full: exit
#  4                          if full: exit
#  5           q[end] = v1
#  6           count += 1
#  7                          q[end] = v2   <-- overwritten
#  8                          count += 1    <-- exceed capacity


# 方法二：单链表  Time:  O(1), Space: O(k)
# 单链表与数组实现方法的时间和空间复杂度相同，但是单链表的效率更高，因为这种方法不会预分配内存。
class Node:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.next = nextNode

class MyCircularQueue2:
    def __init__(self, k: int):
        self.capacity = k
        self.head = None
        self.tail = None
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if self.count == self.capacity:
            return False

        if self.count == 0:
            self.head = self.tail = Node(value)
        else:
            newNode = Node(value)
            self.tail.next = newNode
            self.tail = newNode
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.count == 0:
            return False
        self.head = self.head.next
        self.count -= 1
        return True

    def Front(self) -> int:
        return self.head.value if self.count else -1

    def Rear(self) -> int:
        return self.tail.value if self.count else -1

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.capacity


obj = MyCircularQueue(3) # set the size to be 3
print(obj.enQueue(1))  # return true
print(obj.enQueue(2))  # return true
print(obj.enQueue(3))  # return true
print(obj.enQueue(4))  # return false, the queue is full
print(obj.Rear())  # return 3
print(obj.isFull())  # return true
print(obj.deQueue())  # return true
print(obj.enQueue(4))  # return true
print(obj.Rear())  # return 4