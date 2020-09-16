from typing import List
# Design a queue with limited size of array. Queue should be able to hold unlimited items.

# Solution:
# 1. Nested array, where each array has the last item to store the next array.
# Maintain headList/tailList, headPos/tailPos for fast operation. Assume fixed array size is 3:
# [0, 1,
#    [2, 3,
#       [4]
#    ]
# ]
#
# 2. 自己创建ListNode 里面包含limied size的array: this uses additional data structure ListNode.
class QueueWithFixedArray(object):
    def __init__(self, size):
        self.sz = size
        self.headList = self.tailList = []
        self.headPos = self.tailPos = 0 # tailPos: position to insert new item
        self.count = 0

    def isEmpty(self):
        return self.count == 0

    def enqueue(self, x: int):
        if self.tailPos == self.sz - 1: # create a new list if tailPos points to the last item
            self.tailList.append([])
            self.tailList, self.tailPos = self.tailList[-1], 0

        self.tailList.append(x)
        self.tailPos += 1
        self.count += 1

    def dequeue(self) -> int:
        if self.isEmpty():
            return None

        if self.headPos == self.sz - 1: # get the next list if headPos points to the last item
            tmpList = self.headList[self.headPos]
            del self.headList
            self.headList, self.headPos = tmpList, 0

        ans = self.headList[self.headPos]
        self.headPos += 1
        self.count -= 1
        return ans

obj = QueueWithFixedArray(3)
obj.enqueue(0)
print(obj.dequeue()) # 0
for i in range(1, 6):
    obj.enqueue(i)
print(obj.headList)

for i in range(1, 6):
    print(obj.dequeue()) # 1..5
print(obj.headList)

for i in range(6, 9):
    obj.enqueue(i)
print(obj.headList)

for i in range(6, 9):
    print(obj.dequeue()) # 6..8
print(obj.headList)


# Goal is to implement class called Iterator with interface:
# has_next: Boolean - returns true if there is another Int in the structure.
# next: Int - returns the next integer in the structure.
# remove: Unit - removes the last integer returned by next(), can only be called after calling next and only once per call to next.

class Iterator(object):
    def __init__(self, mx: List[List[int]]):
        super().__init__()
        self.mx = mx
        self.r = self.c = 0
        self.adjustItor()

    def adjustItor(self): # col iter reaches the end of current row
        while self.r != len(self.mx) and self.c == len(self.mx[self.r]):
            self.r += 1
            self.c = 0

    def has_next(self):
        return self.r != len(self.mx) and self.c != len(self.mx[self.r])

    # return next value, move forward itor
    def nxt(self):
        ans = self.mx[self.r][self.c]
        self.c += 1
        self.adjustItor()
        return ans

    def remove(self): # determine lastRow/lastCol
        if self.c == 0:
            lastRow = self.r - 1
            while lastRow >= 0 and len(self.mx[lastRow]) == 0:
                lastRow -= 1
            lastCol = len(self.mx[lastRow]) - 1
        else:
            lastRow, lastCol = self.r, self.c - 1
            self.c -= 1

        self.mx[lastRow].pop(lastCol)

# This implementation flattens data to a 1-D array. Remove only modifies the copied data structure, not the original
# matrix. Don't work for test3 (remove then iterate again).
class Iterator2(object):
    def __init__(self, mx):
        self.d = []
        for row in mx:
            for v in row:
                self.d.append(v)
        self.it = 0
    def has_next(self):
        return self.it != len(self.d)
    def nxt(self):
        ans = self.d[self.it]
        self.it += 1
        return ans
    def remove(self):
        self.it -= 1
        self.d.pop(self.it)

def sample_data():
    return [[], [1, 2, 3], [4, 5], [], [], [6], [7, 8], [], [9], [10], []]

def test1():
    i = Iterator(sample_data())
    while i.has_next():
        print(i.nxt()) # 1 2 3 4 5 6 7 8 9 10

def test2():
    i = Iterator(sample_data())
    for _ in range(4):
        print(i.nxt()) # 1 2 3 4

def test3():
    d = sample_data()
    i = Iterator(d)
    while i.has_next():
        if i.nxt() % 2 == 0:
            i.remove()
    i = Iterator(d)
    while i.has_next():
        print(i.nxt()) # 1 3 5 7 9

test1()
test2()
test3()
