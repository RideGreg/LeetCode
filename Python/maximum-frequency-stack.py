# Time:  O(1)
# Space: O(n)

# 895
# Implement FreqStack,
# a class which simulates the operation of a stack-like data structure.
#
# FreqStack has two functions:
#
# push(int x), which pushes an integer x onto the stack.
# pop(), which removes and returns the most frequent element in the stack.
# If there is a tie for most frequent element,
# the element closest to the top of the stack is removed and returned.
#
# Example 1:
#
# Input: 
# ["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"],
# [[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
# Output: [null,null,null,null,null,null,null,5,7,5,4]
# Explanation:
# After making six .push operations, the stack is [5,7,5,7,4,5] from bottom to top.  Then:
#
# pop() -> returns 5, as 5 is the most frequent.
# The stack becomes [5,7,5,7,4].
#
# pop() -> returns 7, as 5 and 7 is the most frequent, but 7 is closest to the top.
# The stack becomes [5,7,5,4].
#
# pop() -> returns 5.
# The stack becomes [5,7,4].
#
# pop() -> returns 4.
# The stack becomes [5,7].
#
# Note:
# - Calls to FreqStack.push(int x) will be such that 0 <= x <= 10^9.
# - It is guaranteed that FreqStack.pop() won't be called if the stack has zero elements.
# - The total number of FreqStack.push calls will not exceed 10000 in a single test case.
# - The total number of FreqStack.pop calls will not exceed 10000 in a single test case.
# - The total number of FreqStack.push and
#   FreqStack.pop calls will not exceed 150000 across all test cases.

import collections

# Very good: 1. Multiple stacks: maintain a mapping from 'freq' key to STACK of values, the stack remembers insertion order.
# for example, push 5,7,5,7,4,5, we store
#   freq 1 : [5,7,4]
#   freq 2 : [5,7]
#   freq 3 : [5]
# 2. Also store maxFreq, so don't re-count on every pop.
# 3. Obviously maintain another mapping of value to freq which is basic for this problem.
class FreqStack(object):

    def __init__(self):
        self.__freq = collections.Counter()
        self.__group = collections.defaultdict(list) # list is treated as a stack to remember insertion order.
        self.__maxfreq = 0

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.__freq[x] += 1
        f = self.__freq[x]
        self.__maxfreq = max(self.__maxfreq, f)
        self.__group[f].append(x) # don't remove it from f-1 stack, otherwise in pop we need to insert back to f-1 stack

    def pop(self):
        """
        :rtype: int
        """
        x = self.__group[self.__maxfreq].pop() # list pop by index
        if not self.__group[self.__maxfreq]:
            # self.__group.pop(self.__maxfreq) # no need to cleanup, maintain maxfreq is enough
            self.__maxfreq -= 1
        self.__freq[x] -= 1
        return x

# Time bad: if not maintain maxFreq, then TLE due to calculate maxFreq every pop.
# Space bad: store every insert (ids for each x value)
class FreqStack_ming(object):

    def __init__(self):
        # self.h = []
        self.pos = collections.defaultdict(list)
        self.id = 0

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.id += 1
        self.pos[x].append(self.id)

    def pop(self):
        """
        :rtype: int
        """
        ans = max(self.pos, key=lambda x: (len(self.pos[x]), self.pos[x][-1]))
        self.pos[ans].pop()
        if not self.pos[ans]:
            del self.pos[ans]
        return ans



obj = FreqStack()
obj.push(4)
obj.push(0)
obj.push(9)
obj.push(3)
obj.push(4)
obj.push(2)
print(obj.pop()) # 4
obj.push(6)
print(obj.pop()) # 6
obj.push(1)
print(obj.pop()) # 1
obj.push(1)
print(obj.pop()) # 1
obj.push(4)
for _ in xrange(6):
    print(obj.pop()) # 4,2,3,9,0,4

obj = FreqStack()
obj.push(5)
obj.push(7)
obj.push(5)
obj.push(7)
obj.push(4)
obj.push(5)
for _ in xrange(4):
    print(obj.pop()) # 5,7,5,4
