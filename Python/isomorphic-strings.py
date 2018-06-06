# Time:  O(n)
# Space: O(1)

# Given two strings s and t, determine if they are isomorphic.
#
# Two strings are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character
# while preserving the order of characters. No two characters may map to
# the same character but a character may map to itself.
#
# For example,
# Given "egg", "add", return true.
#
# Given "foo", "bar", return false.
#
# Given "paper", "title", return true.
#
# Note:
# You may assume both s and t have the same length.

from itertools import izip  # Generator version of zip.

class Solution(object):
    def isIsomorphic(self, s, t):  # USE THIS
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        s2t, t2s = {}, {}
        for w, p in izip(s, t):
            wmap, pmap = s2t.get(w), t2s.get(p)
            if wmap is None and pmap is None:
                s2t[w] = p
                t2s[p] = w
            elif wmap != p:
                # Contradict mapping. Check one direction is sufficient, because setting is for both dict.
                return False
        return True

    def isIsomorphic_ming(self, s, t):
        s2t, usedt = {}, set()
        for x, y in izip(s, t):
            if x in s2t:
                if s2t[x] != y:
                    return False
            else:
                if y in usedt:
                    return False
            s2t[x] = y
            usedt.add(y)
        return True

# Time:  O(n)
# Space: O(1)
class Solution2(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False

        return self.halfIsom(s, t) and self.halfIsom(t, s)

    def halfIsom(self, s, t):
        lookup = {}
        for i in xrange(len(s)):
            if s[i] not in lookup:
                lookup[s[i]] = t[i]
            elif lookup[s[i]] != t[i]:
                return False
        return True
