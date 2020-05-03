# Time:  ctor: O(k)
#        add: O(1)
#        showFirstUnique: O(1)
# Space: O(n)

# 1429
# You have a queue of integers, you need to retrieve the first unique integer in the queue.
#
# Implement the FirstUnique class:
#   FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
#   int showFirstUnique() returns the value of the first unique integer of the queue, and returns -1 if there is no such integer.
#   void add(int value) insert value to the queue.

from typing import List
import collections


class FirstUnique(object): # USE THIS: use OrderedDict to controll order, actually only need OrderedSet (a special case of OrderedDict)

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.__unique = collections.OrderedDict()
        self.__dup = set()
        for num in nums:
            self.add(num)

    def showFirstUnique(self):
        """
        :rtype: int
        """
        if self.__unique:
            return next(iter(self.__unique))
        return -1
    

    def add(self, value):
        """
        :type value: int
        :rtype: None
        """
        if value not in self.__dup and value not in self.__unique:
            self.__unique[value] = None # only need to save key, value can be None or 1 or anything
            return
        if value in self.__unique:
            self.__unique.pop(value) # same effect as del self.__unique[value]
            self.__dup.add(value)


class FirstUnique2: # similar to method 1, but inferior by storing both unique and dup in Counter
    def __init__(self, nums: List[int]):
        self.unique = collections.OrderedDict()
        self.cnt = collections.Counter([])
        for n in nums:
            self.add(n)

    def showFirstUnique(self) -> int:
        return next(iter(self.unique)) if self.unique else -1

    def add(self, value: int) -> None:
        self.cnt[value] += 1
        if self.cnt[value] == 1:
            self.unique[value] = 1
        elif value in self.unique:
            del self.unique[value]


# doubly linked list to store nodes with unique numbers. dict to store the mapping
# from value to: None (repeating value), list node (unique value), not in dict (value not seen).
class DDLNode(object):
    def __init__(self, x):
        self.v = x
        self.prev = None
        self.next = None
class FirstUnique3:
    def __init__(self, nums: List[int]):
        self.head = self.tail = None
        self.lookup = {}
        for n in nums:
            self.add(n)

    def showFirstUnique(self) -> int:
        return self.head.v if self.head else -1

    def add(self, value: int) -> None:
        if value not in self.lookup:
            # insert node
            node = DDLNode(value)
            if self.head:
                node.prev = self.tail
                self.tail.next = node
            else:
                self.head = node

            self.tail = node
            self.lookup[value] = node
        elif self.lookup[value]:
            node = self.lookup[value]
            # delete node
            if node.prev:
                node.prev.next = node.next
            else:
                self.head = node.next
            if node.next:
                node.next.prev = node.prev
            else:
                self.tail = node.prev
            del node
            self.lookup[value] = None


obj = FirstUnique([2,3,5])
print(obj.showFirstUnique()) # 2
obj.add(5); print(obj.showFirstUnique()) # 2
obj.add(2); print(obj.showFirstUnique()) # 3
obj.add(3); print(obj.showFirstUnique()) # -1

print("\n")
obj = FirstUnique([7,7,7,7,7,7])
print(obj.showFirstUnique()) # -1
obj.add(3); obj.add(3); obj.add(17); print(obj.showFirstUnique()) # 17

print("\n")
obj = FirstUnique([809])
print(obj.showFirstUnique()) # 809
obj.add(809); print(obj.showFirstUnique()) # -1
=======


>>>>>>> d9628635... Create first-unique-number.py
