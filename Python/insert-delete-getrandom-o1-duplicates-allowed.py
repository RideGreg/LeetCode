# Time:  O(1)
# Space: O(n)

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

from random import randint
from collections import defaultdict

class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__list = []
        self.__used = defaultdict(list)


    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        has = val in self.__used

        self.__list += val,
        self.__used[val] += len(self.__list)-1,

        return not has


    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.__used or not self.__used[val]:
            return False

        if val != self.__list[-1]:
            end = len(self.__list) - 1
            pos = self.__used[val].pop()
            self.__used[val].append(end)
            self.__used[self.__list[-1]].remove(end)
            self.__used[self.__list[-1]].append(pos)

            self.__list[-1], self.__list[pos] = self.__list[pos], self.__list[-1]

        self.__used[val].remove(len(self.__list) - 1)
        self.__list.pop()

        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return self.__list[randint(0, len(self.__list)-1)]


# Your RandomizedCollection object will be instantiated and called as such:
obj = RandomizedCollection()
print obj.insert(1)
print obj.insert(1)
print obj.insert(2)
print obj.insert(2)
print obj.insert(2)

print obj.remove(1)
print obj.remove(1)
print obj.remove(2)

print obj.insert(1)

print obj.remove(2)
