# Time:  O(n * l^2), it also takes O(l) to make the substring w[:i]+w[i+1:]
# Space: O(n * l)

# 1048 weekly contest 137 5/18/2019
# Given a list of words, each word consists of English lowercase letters.
#
# Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1
# to make it equal to word2.  For example, "abc" is a predecessor of "abac".
#
# A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a
# predecessor of word_2, word_2 is a predecessor of word_3, and so on.
#
# Return the longest possible length of a word chain with words chosen from the given list of words.

# 1 <= words.length <= 1000
# 1 <= words[i].length <= 16

from typing import List
import collections


class Solution(object):
    def longestStrChain(self, words): # USE THIS 200ms
        """
        :type words: List[str]
        :rtype: int
        """
        words.sort(key=len)
        dp = collections.defaultdict(int)
        for w in words:
            for i in range(len(w)):
                dp[w] = max(dp[w], dp[w[:i]+w[i+1:]]+1)
        return max(dp.values())

    # O(n^2 * l) 1920ms
    def longestStrChain_ming(self, words: List[str]) -> int:
        def isSub(s1, s2):
            if len(s1) + 1 != len(s2): return False
            i = 0
            for c in s2:
                if c == s1[i]:
                    i += 1
                    if i == len(s1): return True
            return False

        dp = [1] * len(words)
        words.sort(key=len)
        for i in range(1, len(words)): # traverse all words
            for j in reversed(range(i)): # traverse all previous words, reverse to reduce the call to isSub()
                if dp[j] + 1 > dp[i] and isSub(words[j], words[i]):
                    dp[i] = dp[j] + 1
        return max(dp)

print(Solution().longestStrChain(["a","b","ba","bca","bda","bdca"])) # 4
print(Solution().longestStrChain([
    "ksqvsyq","ks","kss","czvh","zczpzvdhx","zczpzvh","zczpzvhx","zcpzvh","zczvh","gr",
    "grukmj","ksqvsq","gruj","kssq","ksqsq","grukkmj","grukj","zczpzfvdhx","gru"])) # 7