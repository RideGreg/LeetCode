# Time:  O(n * l^2)
# Space: O(n * l)

# 472
# Given a list of words, please write a program that returns
# all concatenated words in the given list of words.
#
# A concatenated word is defined as a string that is comprised entirely of
# at least two shorter words in the given array.
#
# Example:
# Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
#
# Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
#
# Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats";
#  "dogcatsdog" can be concatenated by "dog", "cats" and "dog";
# "ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
# Note:
# The number of elements of the given array will not exceed 10,000
# The length sum of elements in the given array will not exceed 600,000.
# All the input string will only include lower case letters.
# The returned elements order does not matter.

class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        lookup = set(words)
        result = []
        for word in words:
            dp = [True] + [False] * len(word)
            for i in range(len(word)):
                if dp[i]: # word[:i] exist in dictionary
                    for j in range(i+1, len(word)+1):
                        if j - i < len(word) and word[i:j] in lookup:
                            dp[j] = True

                    if dp[len(word)]:
                        result.append(word)
                        break

        return result

    # memorization
    def findAllConcatenatedWordsInADict2(self, words):
        wset = set(words)
        ans, lookup = [], {}

        def match(s):
            if s not in lookup:
                if s in wset:
                    lookup[s] = True
                else:
                    for i in range(1, len(s)):
                        if s[:i] in wset and match(s[i:]):
                            lookup[s] = True
                            break
                    else:
                        lookup[s] = False

            return lookup[s]

        for w in words:
            for i in range(1, len(w)):
                if match(w[:i]) and match(w[i:]):
                    ans.append(w)
                    break
        return ans

print(Solution().findAllConcatenatedWordsInADict(['sun', 'moon', 'star', 'sunmoon', 'sunstarsun', 'earthsun', 'suns', 'sunsun']))
# ['sunmoon', 'sunstarsun', 'sunsun']
print(Solution().findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]))
# ["catsdogcats","dogcatsdog","ratcatdogcat"]