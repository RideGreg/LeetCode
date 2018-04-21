# Time:  O((d * l) * logd), l is the average length of words
# Space: O(1)

# Given a string and a string dictionary,
# find the longest string in the dictionary
# that can be formed by deleting some characters of the given string.
# If there are more than one possible results,
# return the longest word with the smallest lexicographical order.
# If there is no possible result, return the empty string.
#
# Example 1:
# Input:
# s = "abpcplea", d = ["ale","apple","monkey","plea"]
#
# Output:
# "apple"
# Example 2:
# Input:
# s = "abpcplea", d = ["a","b","c"]
#
# Output:
# "a"
# Note:
# All the strings in the input will only contain lower-case letters.
# The size of the dictionary won't exceed 1,000.
# The length of all the strings in the input won't exceed 1,000.

class Solution(object):
    # sort is expensive. time O(xnlogn+xn), n is # of strings in d,
    # x is average string len; space O(logn), sorting takes space.
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        d.sort(key = lambda x: (-len(x), x))
        for word in d:
            i = 0
            for c in s:
                if i >= len(word):
                    break
                if word[i] == c:
                    i += 1
            if i == len(word):
                return word
        return ""

    # better. Time O(nx), space O(x) ans variable or O(1) if only consider n (#of strings in d).
    def findLongestWord_noSort(self, s, d):
        ans = ''
        for w in d:
            if len(w) == len(ans) and w < ans or len(w) > len(ans):
                i, j = 0, 0
                while i < len(s) and j < len(w):
                    if s[i] == w[j]:
                        j += 1
                    i += 1
                if j == len(w):
                    ans = w
        return ans
