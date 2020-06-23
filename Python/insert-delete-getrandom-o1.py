# Time:  O(1)
# Space: O(n)

# 380
# Design a data structure that supports all following operations in O(1) time.
#
# insert(val): Inserts an item val to the set if not already present.
# remove(val): Removes an item val from the set if present.
# getRandom: Returns a random element from current set of elements.
# Each element must have the same probability of being returned.
#
# Example:
#
# // Init an empty set.
# RandomizedSet randomSet = new RandomizedSet();
#
# // Inserts 1 to the set. Returns true as 1 was inserted successfully.
# randomSet.insert(1);
#
# // Returns false as 2 does not exist in the set.
# randomSet.remove(2);
#
# // Inserts 2 to the set, returns true. Set now contains [1,2].
# randomSet.insert(2);
#
# // getRandom should return either 1 or 2 randomly.
# randomSet.getRandom();
#
# // Removes 1 from the set, returns true. Set now contains [2].
# randomSet.remove(1);
#
# // 2 was already in the set, so return false.
# randomSet.insert(2);
#
# // Since 1 is the only number in the set, getRandom always return 1.
# randomSet.getRandom();


# 哈希表+动态数组：RandomizedSet要求在O(1)实现insert, delete, getRandom
# For insert, 哈希表dict/set和动态数组list是O(1)。哈希表没有索引，不能获得真正的随机值。
# 只能用数组。数组可以常数insert/getRandom，但是删除需要线性时间，要优化到常数时间，
# 解决方案是将待删元素和最后一个元素交换并删除最后一个元素，因此需要一个哈希表来存储数值到索引的映射。

import random

class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__set = []
        self.__val2index = {}


    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.__val2index:
            self.__val2index[val] = len(self.__set)
            self.__set.append(val)
            return True
        return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.__val2index:
            '''pop HAS TO BE done AFTER re-assign, because for single entry, pop->re-assign will
               add the entry back. insert(0), remove(0), insert(0) is wrong for following code
            pos = self.__val2index.pop(val)
            self.__val2index[self.__set[-1]] = pos
            '''
            self.__val2index[self.__set[-1]] = self.__val2index[val]
            pos = self.__val2index.pop(val)

            self.__set[pos], self.__set[-1] = self.__set[-1], self.__set[pos]
            self.__set.pop()
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        if not self.__set: return None
        return random.choice(self.__set)
        # simpler than: return self.__set[random.randint(0, len(self.__set)-1)]

obj = RandomizedSet()
print(obj.insert(0)) # True
print(obj.insert(1)) # True
print(obj.remove(0)) # True
print(obj.insert(2)) # True
print(obj.remove(1)) # True
print(obj.getRandom())  # 2

obj = RandomizedSet()
print(obj.insert(0)) # True
print(obj.getRandom())  # 0
print(obj.remove(0)) # True
print(obj.getRandom())  # None
print(obj.insert(0)) # True
