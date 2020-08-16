# Time:  O(n), n is the number of the integers.
# Space: O(h), h is the depth of the nested lists.

# 341
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
class NestedInteger(object):
    def __init__(self, x):
        self.x = x
    def isInteger(self):
        return type(self.x) == int
    def getInteger(self):
        return self.x if self.isInteger() else None
    def getList(self):
        return None if self.isInteger() else self.x

#将 NestedInteger结构体中的内容依次压栈，并保证栈顶为Integer即可
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        # 对于nestedList中的内容，我们需要从左往右遍历，
        # 但堆栈pop是从右端开始，所以我们压栈的时候需要将nestedList反转再压栈
        self.stack = nestedList[::-1]

    def next(self) -> int:
        # hasNext 函数中已经保证栈顶是integer，所以直接返回pop结果
        return self.stack.pop().getInteger()

    def hasNext(self) -> bool:
        # 对栈顶进行‘剥皮’，如果栈顶是List，把List反转再依次压栈，
        # 然后再看栈顶，依次循环直到栈顶为Integer。
        # 同时可以处理空的List，类似[[[]],[]]这种test case
        while self.stack and self.stack[-1].isInteger() is False:
            self.stack.extend(self.stack.pop().getList()[::-1])
        return len(self.stack) > 0

# Put the list and position (index) at the top of stack
class NestedIterator_kamyu(object):
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.__depth = [[nestedList, 0]]

    def next(self):
        """
        :rtype: int
        """
        nestedList, i = self.__depth[-1]
        self.__depth[-1][1] += 1
        return nestedList[i].getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.__depth:
            nestedList, i = self.__depth[-1]
            if i == len(nestedList):
                self.__depth.pop()
            elif nestedList[i].isInteger():
                    return True
            else:
                self.__depth[-1][1] += 1
                self.__depth.append([nestedList[i].getList(), 0])
        return False


list1 = [NestedInteger([NestedInteger(1), NestedInteger(1)]),
         NestedInteger(2),
         NestedInteger([NestedInteger(1), NestedInteger(1)])]
list2 = [NestedInteger(1),
         NestedInteger([NestedInteger(4),
                        NestedInteger([NestedInteger(6)])])]
list3 = [NestedInteger([NestedInteger([])]), NestedInteger([])]
for nestedList in (list1, list2, list3):
    i, v = NestedIterator(nestedList), []
    while i.hasNext():
        v.append(i.next())
    print(v)
