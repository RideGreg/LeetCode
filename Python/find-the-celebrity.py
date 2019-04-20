# Time:  O(n)
# Space: O(1)
#
# 277
# Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there
# may exist one celebrity. The definition of a celebrity is that all the other n - 1 people
# know him/her but he/she does not know any of them.

# Now you want to find out who the celebrity is or verify that there is not one. The only thing
# you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information of
# whether A knows B. You need to find out the celebrity (or verify there is not one) by asking
# as few questions as possible (in the asymptotic sense).

# You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement
#  a function int findCelebrity(n), your function should minimize the number of calls to knows.
# Note: There will be exactly one celebrity if he/she is in the party. Return the celebrity's label
# if there is a celebrity in the party. If there is no celebrity, return -1.

# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):
#

class Solution(object):
    # Solution: two pointers. Discard each person from either end per call of 'knows'
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 0, n-1
        while left < right:
            if knows(left, right):
                left += 1
            else:
                right -= 1
        # now left == right, the only remaining candidate
        for i in xrange(n):
            if i != left and (knows(left, i) or not knows(i, left)):
                return -1
        return left


    # a similar solution, discard each person per call of 'knows'
    def findCelebrity2(self, n):
        candidate = 0
        # Find the candidate.
        for i in xrange(1, n):
            if knows(candidate, i):  # All candidates < i are not celebrity candidates.
                candidate = i   # this actually discard original candidate
            # else actually discard i
        # Verify the candidate.
        for i in xrange(n):
            if i != candidate and (knows(candidate, i) or not knows(i, candidate)):
                return -1
        return candidate



    # Brute Force: Time O(n^2), Space O(n)
    # Transformed as a graph problem. We count the in/out-degrees for each person.
    # http://buttercola.blogspot.com/2015/09/leetcode-find-celebrity.html
    def findCelebrity_bruteForce(self, n):
        degrees = [0] * n
        for i in xrange(n):
            for j in xrange(n):
                if i != j and knows(i, j):
                    degrees[i] -= 1
                    degrees[j] += 1
        for i in xrange(n):
            if degrees[i] == n-1:
                return i
        return -1
