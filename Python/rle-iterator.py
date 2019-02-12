# Time:  O(n)
# Space: O(1)

# 900
# Write an iterator that iterates through a run-length encoded sequence.
#
# The iterator is initialized by RLEIterator(int[] A),
# where A is a run-length encoding of some sequence.
# More specifically, for all even i,
# A[i] tells us the number of times that
# the non-negative integer value A[i+1] is repeated in the sequence.
#
# The iterator supports one function: next(int n),
# which exhausts the next n elements (n >= 1) and
# returns the last element exhausted in this way.
# If there is no element left to exhaust, next returns -1 instead.
#
# For example, we start with A = [3,8,0,9,2,5],
# which is a run-length encoding of the sequence [8,8,8,5,5].
# This is because the sequence can be read as "three eights, zero nines, two fives".
#
# Example 1:
#
# Input: ["RLEIterator","next","next","next","next"], [[[3,8,0,9,2,5]],[2],[1],[1],[2]]
# Output: [null,8,8,5,-1]
# Explanation: 
# RLEIterator is initialized with RLEIterator([3,8,0,9,2,5]).
# This maps to the sequence [8,8,8,5,5].
# RLEIterator.next is then called 4 times:
#
# .next(2) exhausts 2 terms of the sequence, returning 8.  The remaining sequence is now [8, 5, 5].
#
# .next(1) exhausts 1 term of the sequence, returning 8.  The remaining sequence is now [5, 5].
#
# .next(1) exhausts 1 term of the sequence, returning 5.  The remaining sequence is now [5].
#
# .next(2) exhausts 2 terms, returning -1.  This is because the first term exhausted was 5,
# but the second term did not exist.  Since the last term exhausted does not exist, we return -1.
#
# Note:
# - 0 <= A.length <= 1000
# - A.length is an even integer.
# - 0 <= A[i] <= 10^9
# - There are at most 1000 calls to RLEIterator.next(int n) per test case.
# - Each call to RLEIterator.next(int n) will have 1 <= n <= 10^9.

class RLEIterator(object):
    # init stores the prefix sum of length, so iterator can use bisect
    def __init__(self, A):
        """
        :type A: List[int]
        """
        self.total = 0
        self.length = [] # list of tuple [(prefix sum length, value)]
        for i in xrange(0, len(A), 2):
            if A[i]:
                length = A[i] + self.length[-1][0] if self.length else A[i]
                self.length.append((length, A[i + 1]))

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        import bisect
        self.total += n
        if self.total > self.length[-1][0]: return -1
        pos = bisect.bisect_left(self.length, (self.total, -1))
        return self.length[pos][1]

class RLEIterator_kamyu(object):
    def __init__(self, A):
        """
        :type A: List[int]
        """
        self.__A = A
        self.__i = 0
        self.__used = 0

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        while self.__i < len(self.__A):
            if  n > self.__A[self.__i] - self.__used:
                n -= self.__A[self.__i] - self.__used
                self.__used = 0
                self.__i += 2
            else:
                self.__used += n
                return self.__A[self.__i+1]
        return -1


# Your RLEIterator object will be instantiated and called as such:
obj = RLEIterator([3,8,0,9,2,5])
print(obj.next(2))
print(obj.next(1))
print(obj.next(1))
print(obj.next(2))
