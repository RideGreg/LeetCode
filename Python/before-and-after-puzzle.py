# Time:  O(l * rlogr)  , l is the max length of phrases
#                      , r is the number of result, could be up to O(n^2)
# Space: O(l * (n + r)), n is the number of phrases

# 1181
# Given a list of phrases, generate a list of Before and After puzzles.
#
# A phrase is a string that consists of lowercase English letters and spaces only. No space appears in the start
# or the end of a phrase. There are no consecutive spaces in a phrase.
#
# Before and After puzzles are phrases that are formed by merging two phrases where the last word of the first phrase
# is the same as the first word of the second phrase.
#
# Return the Before and After puzzles that can be formed by every two phrases phrases[i] and phrases[j] where i != j.
# Note that the order of matching two phrases matters, we want to consider both orders.
#
# You should return a list of distinct strings sorted lexicographically.

# 1 <= phrases.length <= 100
# 1 <= phrases[i].length <= 100
# Hint:
# What if you check every pair of strings (bruteforce)?
# For every two strings, check if they can form a puzzle by comparing their last and first words.


import collections


class Solution(object):
    def beforeAndAfterPuzzles(self, phrases):
        """
        :type phrases: List[str]
        :rtype: List[str]
        """
        lastword = collections.defaultdict(list)
        for i, phrase in enumerate(phrases):
            right = phrase.rfind(' ')
            word = phrase if right == -1 else phrase[right+1:]
            lastword[word].append(i)

        result_set = set()
        for i, phrase in enumerate(phrases):
            left = phrase.find(' ')
            word = phrase if left == -1 else phrase[:left]
            if word not in lastword:
                continue
            for j in lastword[word]:
                if j != i:
                    result_set.add(phrases[j] + phrase[len(word):])
        return sorted(result_set)

print(Solution().beforeAndAfterPuzzles(["writing code", "code rocks"]))
# ["writing code rocks"]

print(Solution().beforeAndAfterPuzzles([
    "mission statement",
    "a quick bite to eat",
    "a chip off the old block",
    "chocolate bar",
    "mission impossible",
    "a man on a mission",
    "block party",
    "eat my words",
    "bar of soap"
]))
# Output: ["a chip off the old block party",
#          "a man on a mission impossible",
#          "a man on a mission statement",
#          "a quick bite to eat my words",
#          "chocolate bar of soap"]

print(Solution().beforeAndAfterPuzzles(["a","b","a"])) # ["a"]
