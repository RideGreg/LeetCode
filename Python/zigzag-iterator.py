# Time:  O(n), number of all values
# Space: O(k), number of sequences

# 281
# Given two 1d vectors, implement an iterator to return their elements alternately.
# Need the following methods:
#  hasNext: Boolean - returns true if there is another Int in the structure.
#  next: Int - returns the next integer in the structure.
#  remove: (this is not in LC original problem, added by Ming) - removes the last integer
#           returned by next(), can only be called after calling next and only once per call to next.

import collections

class ZigzagIterator(object): # USE THIS: queue for rotate, can handle multiple sequences; support remove()
    def __init__(self, v1, v2):
        self.q = collections.deque()
        for v in (v1, v2):
            if v:
                self.q.append([0, v])
        self.preId = self.preV = None

    def next(self):
        idx, arr = self.q.popleft()
        if idx < len(arr) - 1:
            self.q.append([idx + 1, arr])
        self.preId = idx
        self.preV = arr
        return arr[idx]

    def hasNext(self):
        return bool(self.q)

    def remove(self):
        if self.preV == self.q[-1][1]:
            self.q[-1][0] -= 1
        self.preV.pop(self.preId)


# VERY GOOD using queue and built-in iter() to save space. But built-in iter() cannot retreat, so cannot do remove().
# https://stackoverflow.com/questions/2777188/making-a-python-iterator-go-backwards
class ZigzagIterator_kamyu(object): # USE THIS: queue for rotate, can handle multiple sequences
    def __init__(self, v1, v2):
        """
        Initialize your q structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.q = collections.deque([(len(v), iter(v)) for v in (v1, v2) if v])

    def next(self):
        """
        :rtype: int
        """
        len, iter = self.q.popleft()
        if len > 1:
            self.q.append((len-1, iter))
        return next(iter)

    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.q)



class ZigzagIterator_ming(object): # not use queue for rotate, hard to do multiple sequences.
    def __init__(self, v1, v2):
        self.v0, self.v1 = v1, v2
        self.i0 = self.i1 = 0
        self.seqId = 0 if self.v0 else 1
        self.preSeqId = None

    def next(self):
        self.preSeqId = self.seqId

        if self.seqId == 0:
            ans = self.v0[self.i0]
            self.i0 += 1
            if self.i1 < len(self.v1):
                self.seqId = 1
        else:
            ans = self.v1[self.i1]
            self.i1 += 1
            if self.i0 < len(self.v0):
                self.seqId = 0
        return ans

    def hasNext(self):
        return self.i0 < len(self.v0) or self.i1 < len(self.v1)

    def remove(self):
        if self.preSeqId == 0:
            self.i0 -= 1
            self.v0.pop(self.i0)
        else:
            self.i1 -= 1
            self.v1.pop(self.i1)


# Merges two arrays into one. Not working correctly for remove() function.
class ZigzagIterator_wrong_remove(object):
    def __init__(self, v1, v2):
        n = min(len(v1), len(v2))
        self.v = [x for i in range(n) for x in (v1[i], v2[i])]
        self.v.extend(v1[n:] + v2[n:])
        self.id = 0

    def next(self):
        self.id += 1
        return self.v[self.id - 1]

    def hasNext(self):
        return self.id < len(self.v)

    def remove(self):
        self.id -= 1
        self.v.pop(self.id)


# Your ZigzagIterator object will be instantiated and called as such:
v1 = [1,2,5]
v2 = [3,4,6,7]
i = ZigzagIterator(v1, v2)
while i.hasNext():
    print(i.next()) # 1,3,2,4,5,6,7

i = ZigzagIterator(v1, v2)
while i.hasNext():
    if i.next() % 3 == 0:
        i.remove() # 3,6

i = ZigzagIterator(v1, v2)
while i.hasNext():
    print(i.next()) # 1,4,2,7,5
