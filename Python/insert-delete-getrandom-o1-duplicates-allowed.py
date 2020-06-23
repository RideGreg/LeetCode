# Time:  O(1)
# Space: O(n)

# 381
# Design a data structure that supports all following operations in average O(1) time.
#
# Note: Duplicate elements are allowed.
# insert(val): Inserts an item val to the collection.
# remove(val): Removes an item val from the collection if present.
# getRandom: Returns a random element from current collection of elements.
# The probability of each element being returned is linearly related to
# the number of same value the collection contains.
# Example:
#
# // Init an empty collection.
# RandomizedCollection collection = new RandomizedCollection();
#
# // Inserts 1 to the collection. Returns true as the collection did not contain 1.
# collection.insert(1);
#
# // Inserts another 1 to the collection. Returns false as the collection contained 1. Collection now contains [1,1].
# collection.insert(1);
#
# // Inserts 2 to the collection, returns true. Collection now contains [1,1,2].
# collection.insert(2);
#
# // getRandom should return 1 with the probability 2/3, and returns 2 with the probability 1/3.
# collection.getRandom();
#
# // Removes 1 from the collection, returns true. Collection now contains [1,2].
# collection.remove(1);
#
# // getRandom should return 1 and 2 both equally likely.
# collection.getRandom();

# 动态数组 + 哈希表：简单的解决方案将所有值包括重复值存储在一个数组中，牺牲空间换时间。

import random, bisect, collections

class RandomizedCollection(object): # USE THIS

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__list = []
        self.__v2ids = collections.defaultdict(set)


    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.__v2ids[val].add(len(self.__list))
        self.__list.append(val)

        return len(self.__v2ids[val]) == 1


    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.__v2ids or not self.__v2ids[val]:
            return False

        pos = self.__v2ids[val].pop() # pop an arbitrary elem from set
        self.__v2ids[self.__list[-1]].add(pos) # add MUST done before discard, otherwise wrong for single item!!
        self.__v2ids[self.__list[-1]].discard(len(self.__list)-1)

        self.__list[-1], self.__list[pos] = self.__list[pos], self.__list[-1]
        self.__list.pop()

        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return random.choice(self.__list)
        # OR return self.__list[randint(0, len(self.__list)-1)]


class RandomizedCollection__CDF: # Cumulative Density Function: getRandom not O(1)

    def __init__(self):
        self.d = {}

    def insert(self, val: int) -> bool:
        if val not in self.d:
            self.d[val] = 1
            return True
        self.d[val] += 1
        return False

    def remove(self, val: int) -> bool:
        if val not in self.d:
            return False
        self.d[val] -= 1
        if self.d[val] == 0:
            self.d.pop(val)
        return True

    def getRandom(self) -> int:
        psum = list(self.d.values())
        for i in range(1, len(psum)):
            psum[i] += psum[i - 1]
        id = random.randint(1, psum[-1])
        keys = list(self.d.keys())
        return keys[bisect.bisect_left(psum, id)]

# Your RandomizedCollection object will be instantiated and called as such:
obj = RandomizedCollection()
print(obj.insert(1)) # True
print(obj.remove(1)) # True
print(obj.insert(3)) # True
print(obj.insert(1)) # True **
print(obj.insert(2)) # True
print(obj.insert(2)) # False
print(obj.insert(2)) # False

print(obj.remove(1)) # True
print(obj.remove(1)) # False **
print(obj.remove(3)) # True
print(obj.getRandom()) # 2
print(obj.remove(2)) # True
print(obj.insert(1)) # True
print(obj.remove(2)) # True
