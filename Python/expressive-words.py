# Time:  O(n + s), n is the sum of all word lengths, s is the length of S
# Space: O(l + s), l is the max word length

# 809
# Sometimes people repeat letters to represent extra feeling,
# such as "hello" -> "heeellooo", "hi" -> "hiiii".
# Here, we have groups, of adjacent letters that are all the same character,
# and adjacent characters to the group are different.
# A group is extended if that group is length 3 or more, so "e" and "o"
# would be extended in the first example, and "i" would be extended in the second example.
# As another example, the groups of "abbcccaaaa" would be "a", "bb", "ccc", and "aaaa";
# and "ccc" and "aaaa" are the extended groups of that string.
#
# For some given string S, a query word is stretchy
# if it can be made to be equal to S by extending some groups.
# Formally, we are allowed to repeatedly choose a group (as defined above) of characters c,
# and add some number of the same character c to it so that the length of the group is 3 or more.
# Note that we cannot extend a group of size one like "h" to a group of size two like "hh" -
# all extensions must leave the group extended - ie., at least 3 characters long.
#
# Given a list of query words, return the number of words that are stretchy.
#
# Example:
# Input:
# S = "heeellooo"
# words = ["hello", "hi", "helo"]
# Output: 1
# Explanation:
# We can extend "e" and "o" in the word "hello" to get "heeellooo".
# We can't extend "helo" to get "heeellooo" because the group "ll" is not extended.
#
# Notes:
# - 0 <= len(S) <= 100.
# - 0 <= len(words) <= 100.
# - 0 <= len(words[i]) <= 100.
# - S and all words in words consist only of lowercase letters

import itertools


class Solution(object):
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        # Run length encoding
        def RLE(S):
            return itertools.izip(*[(k, len(list(grp)))
                                  for k, grp in itertools.groupby(S)])

        R, count = RLE(S)
        result = 0
        for word in words:
            R2, count2 = RLE(word)
            if R2 != R:
                continue
            result += all(c1 >= max(c2, 3) or c1 == c2
                          for c1, c2 in itertools.izip(count, count2))
        return result

    # two poniters
    def expressiveWords_ming(self, S, words):
        def helper(S, word):
            si, wi = 0, 0
            while si < len(S) and wi < len(word):
                if S[si] != word[wi]:
                    return False

                scnt = wcnt = 1
                while si+scnt < len(S) and S[si+scnt] == S[si]:
                    scnt += 1
                while wi+wcnt < len(word) and word[wi+wcnt] == word[wi]:
                    wcnt += 1
                if not(scnt==wcnt or (scnt>wcnt and scnt >= 3)):
                    return False

                si += scnt
                wi += wcnt
            return si == len(S) and wi == len(word)

        return sum(1 for word in words if helper(S, word))

print(Solution().expressiveWords("heeellooo", ["hello", "hi", "helo"]))
