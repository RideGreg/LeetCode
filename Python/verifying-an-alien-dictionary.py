# Time:  O(n * l), l is the average length of words
# Space: O(1)

# 953
# In an alien language, surprisingly they also use english lowercase letters, but possibly in a
# different order. The order of the alphabet is some permutation of lowercase letters.
#
# Given a sequence of words written in the alien language, and the order of the alphabet,
# return true if and only if the given words are sorted lexicographicaly in this alien language.

class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        def check(s1, s2):
            l = min(len(s1), len(s2))
            for i in xrange(l):
                if lookup[s1[i]]<lookup[s2[i]]: return True
                if lookup[s1[i]]>lookup[s2[i]]: return False
            return len(s1) <= len(s2)

        lookup = {c: i for i, c in enumerate(order)}
        return all(check(words[i], words[i+1]) for i in xrange(len(words)-1))

    def isAlienSorted_kamyu(self, words, order):
        lookup = {c: i for i, c in enumerate(order)}
        for i in xrange(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            for k in xrange(min(len(word1), len(word2))):
                if word1[k] != word2[k]:
                    if lookup[word1[k]] > lookup[word2[k]]:
                        return False
                    break
            else:
                if len(word1) > len(word2):
                    return False
        return True

print(Solution().isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz")) # True
print(Solution().isAlienSorted(["word","world","row"], "worldabcefghijkmnpqstuvxyz")) # False
print(Solution().isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz")) # False