# Time:  O(1)
# Space: O(1)

# 251
# Implement an iterator to flatten a 2d vector.
#
# For example,
# Given 2d vector =
# [
#   [1,2],
#   [3],
#   [4,5,6]
# ]
#
#
# By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,2,3,4,5,6].
#
# Hint:
# 1 How many variables do you need to keep track?
# 2 Two variables is all you need. Try with x and y.
# 3 Beware of empty rows. It could be the first few rows.
# 4 To write correct code, think about the invariant to maintain. What is it?
# 5 The invariant is x and y must always point to a valid point in the 2d vector. Should you maintain your invariant ahead of time or right when you need it?
# 6 Not sure? Think about how you would implement hasNext(). Which is more complex?
# 7 Common logic in two different places should be refactored into a common method.

class Vector2D:
    x, y = 0, 0
    vec = None

    # Initialize your data structure here.
    # @param {integer[][]} vec2d
    def __init__(self, vec2d):
        self.vec = vec2d
        self.x = 0
        if self.x != len(self.vec):
            self.y = 0
            self.adjustNextIter()

    # @return {integer}
    def next(self):
        ret = self.vec[self.x][self.y]
        self.y += 1
        self.adjustNextIter()
        return ret

    # @return {boolean}
    def hasNext(self):
        return self.x != len(self.vec) and self.y != len(self.vec[self.x])

    def adjustNextIter(self):
        while self.x != len(self.vec) and self.y == len(self.vec[self.x]):
            self.x += 1
            if self.x != len(self.vec):
                self.y = 0

    # add a requirement to remove the element just outputted
    def remove(self):
        # case 1: if the element to remove is the last element of the row
        if self.y == 0:
            lastRow = self.x - 1
            while lastRow >= 0 and len(self.vec[lastRow]) == 0:
                lastRow -= 1
            lastCol = len(self.vec[lastRow]) - 1
        else:  # case 2: if the element to remove is not the last element
            lastCol = self.y - 1
            lastRow = self.x
            self.y -= 1

        # remove the element
        self.vec[lastRow].pop(lastCol)