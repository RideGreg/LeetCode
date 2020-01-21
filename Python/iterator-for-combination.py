# Time:  O(k), per operation
# Space: O(k)

# 1286 biweekly contest 15 12/14/2019

# Design an Iterator class, which has:
#
# - A constructor that takes a string characters of sorted distinct lowercase English letters and
# a number 'combinationLength' as arguments.
# - A function next() that returns the next combination of length 'combinationLength' in lexicographical order.
# - A function hasNext() that returns True if and only if there exists a next combination.

# 1 <= combinationLength <= characters.length <= 15
# It's guaranteed that all calls of the function next are valid.

# https://portingguide.readthedocs.io/en/latest/iterators.html

# Basically, all of the itertools module functions return iterator type of object. The idea is that, rather than computing
# a list of answers up front, they return an iterable object that 'knows' how to compute the answers, but doesn't do so
# unless `asked.' This way, there is no significant up front cost for computing elements. See also this very good introduction
# to generators https://wiki.python.org/moin/Generators (iterator includes generator, list, set...)

# In cases where the result is only iterated over, and only once, it makes sense to use a "generator expression" "()"
# rather than a list. This keeps memory requirements to a minimum. However, the resulting generator object
# is much less powerful than a list: it cannot be mutated, indexed or sliced, or iterated more than once.

# list comprehensions is generator expressions wrapped in a list constructor.

import itertools

class CombinationIterator(object): # USE THIS: awice. ABSOLUTELY NOT computing up front to save memory.
    def __init__(self, characters, combinationLength):
        self.s = characters
        self.k = combinationLength
        self.it = itertools.combinations(self.s, self.k)
        self.todo = self.binom(len(self.s), self.k)

    # A binomial coefficient equals the # of combinations of r items that can be selected from a set of n items.
    # It also represents an entry in Pascal's triangle. The numbers are called binomial coefficients because they
    # are coefficients in the binomial theorem 二项式定理, which describes the algebraic expansion of powers of a binomial (x+y)^n
    def binom(self, n, k):
        r = 1
        for i in range(1, k + 1):
            r *= n - i + 1
            r /= i
        return r

    def next(self):
        self.todo -= 1
        return "".join(next(self.it))

    def hasNext(self):
        return bool(self.todo)

class CombinationIterator_kamyu(object):

    def __init__(self, characters, combinationLength):
        """
        :type characters: str
        :type combinationLength: int
        """
        self.__it = itertools.combinations(characters, combinationLength) # only for one-time iteration, use python 3 iterator
        self.__curr = None
        self.__last = characters[-combinationLength:]

    def next(self):
        """
        :rtype: str
        """
        #self.__curr = "".join(self.__it.next()) # python 2, next() is a method of iterator
        self.__curr = "".join(next(self.__it)) # python 3, next() is a buit-in function
        return self.__curr
    
    def hasNext(self):
        """
        :rtype: bool
        """
        return self.__curr != self.__last



# Time:  O(k), per operation
# Space: O(k)
import functools


class CombinationIterator2(object):

    def __init__(self, characters, combinationLength):
        """
        :type characters: str
        :type combinationLength: int
        """
        self.__characters = characters
        self.__combinationLength = combinationLength
        self.__it = self.__iterative_backtracking()
        self.__curr = None
        self.__last = characters[-combinationLength:]
        
    def __iterative_backtracking(self):
        def conquer():
            if len(curr) == self.__combinationLength:
                return curr

        def prev_divide(c):
            curr.append(c)
        
        def divide(i):
            if len(curr) != self.__combinationLength:
                for j in reversed(range(i, len(self.__characters)-(self.__combinationLength-len(curr)-1))):
                    stk.append(functools.partial(post_divide))
                    stk.append(functools.partial(divide, j+1))
                    stk.append(functools.partial(prev_divide, self.__characters[j]))
            stk.append(functools.partial(conquer))

        def post_divide():
            curr.pop()
            
        curr = []
        stk = [functools.partial(divide, 0)]
        while stk:
            result = stk.pop()()
            if result is not None:
                yield result

    def next(self):
        """
        :rtype: str
        """
        self.__curr = "".join(next(self.__it))
        return self.__curr
        
    def hasNext(self):
        """
        :rtype: bool
        """
        return self.__curr != self.__last


it = CombinationIterator("abc", 2)
print(it.next()) # returns "ab"
print(it.hasNext()) # returns true
print(it.next()) # returns "ac"
print(it.hasNext()) # returns true
print(it.next()) # returns "bc"
print(it.hasNext()) # returns false
