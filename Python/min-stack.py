# Time:  O(n)
# Space: O(1)
#
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
#

class MinStack:
    def __init__(self):
        self.min = None
        self.stack = []

    # @param x, an integer
    # @return an integer
    def push(self, x):
        if not self.stack:
            self.stack.append(0)
            self.min = x
        else:
            self.stack.append(x - self.min) #只存与"上一个min"的差值部分，如果差值为负（新数更小），要更新min
                                            #这是为了能recover"上一个min"。stack里可能有正数，零，负数。
            if x < self.min:
                self.min = x

    # @return nothing
    def pop(self):
        x = self.stack.pop()
        if x < 0:
            self.min = self.min - x        # recover"上一个min"

    # @return an integer
    def top(self):
        x = self.stack[-1]
        if x > 0:
            return x + self.min #存的是差值部分，要加回min
        else:
            return self.min #最新数最小，已存到min

    # @return an integer
    def getMin(self):
        return self.min

# Time:  O(1)
# Space: O(n)
class MinStack2:
    def __init__(self):
        self.stack, self.minStack = [], []
    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.stack.append(x)
        if not self.minStack or x < self.minStack[-1][0]:
            self.minStack.append([x, 1])  # [value, count]
        elif x == self.minStack[-1][0]:
            self.minStack[-1][1] += 1

    # @return nothing
    def pop(self):
        x = self.stack.pop()
        if x == self.minStack[-1][0]:
            self.minStack[-1][1] -= 1
            if self.minStack[-1][1] == 0:
                self.minStack.pop()

    # @return an integer
    def top(self):
        return self.stack[-1]

    # @return an integer
    def getMin(self):
        return self.minStack[-1][0]

# time: O(1)
# space: O(n) bad, store min for every item
class MinStack3(object):
    def __init__(self):
        self.stack = []

    def push(self, x):
        if self.stack:
            current_min = min(x, self.stack[-1][0])
            self.stack.append((current_min, x))  # bad, double the storage
        else:
            self.stack.append((x, x))

    def pop(self):
        return self.stack.pop()[1]

    def top(self):
        return self.stack[-1][1]

    def getMin(self):
        return self.stack[-1][0]

if __name__ == "__main__":
    stack = MinStack()
    stack.push(2)
    stack.push(6)
    stack.push(2)
    stack.push(10)
    stack.push(1)
    print(stack.top(), stack.getMin()) # 1, 1

    stack.pop()
    print(stack.top(), stack.getMin()) #, 10, 2

    stack.pop()
    print(stack.top(), stack.getMin()) #, 2, 2

    stack.pop()
    print(stack.top(), stack.getMin()) # 6, 2

    stack.pop()
    print(stack.top(), stack.getMin()) # 2, 2
