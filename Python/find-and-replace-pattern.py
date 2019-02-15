# Time:  O(n * l)
# Space: O(1)

# 890
# You have a list of words and a pattern, and you want to know which words in words matches the pattern.
#
# A word matches the pattern if there exists a permutation of letters p so that after replacing
# every letter x in the pattern with p(x), we get the desired word.
#
# (Recall that a permutation of letters is a bijection from letters to letters: every letter maps
# to another letter, and no two letters map to the same letter.)
#
# Return a list of the words in words that match the given pattern.
#
# You may return the answer in any order.
#
#
#
# Example 1:
#
# Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
# Output: ["mee","aqq"]
# Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}.
# "ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation,
# since a and b map to the same letter.

import itertools


class Solution(object):
    def findAndReplacePattern(self, words, pattern): # use only 1 dict
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def match(word):
            lookup = {}
            for x, y in itertools.izip(pattern, word):
                if lookup.setdefault(x, y) != y:
                    return False
            return len(set(lookup.values())) == len(lookup.values())

        return filter(match, words)

    def findAndReplacePattern_ming(self, words, pattern): # USE THIS: use 1 dict + 1 set, early exit
        def match(s):
            lookup, used = {}, set()
            for c1, c2 in itertools.izip(s, pattern):
                if c1 in lookup:
                    if lookup[c1] != c2:
                        return False
                else:
                    if c2 in used:
                        return False
                    lookup[c1] = c2
                    used.add(c2)
            return True

        return filter(match, words)