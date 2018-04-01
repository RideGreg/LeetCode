# Time:  O(n), n is the total sum of the lengths of words
# Space: O(t), t is the number of nodes in trie

# Given a list of strings words representing an English Dictionary,
# find the longest word in words that can be built one character at a time by other words in words.
# If there is more than one possible answer, return the longest word with the smallest lexicographical order.
#
# If there is no answer, return the empty string.
# Example 1:
# Input: 
# words = ["w","wo","wor","worl", "world"]
# Output: "world"
# Explanation: 
# The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
#
# Example 2:
# Input: 
# words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
# Output: "apple"
# Explanation: 
# Both "apply" and "apple" can be built from other words in the dictionary.
# However, "apple" is lexicographically smaller than "apply".
#
# Note:
# - All the strings in the input will only contain lowercase letters.
# - The length of words will be in the range [1, 1000].
# - The length of words[i] will be in the range [1, 30].

class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        _trie = lambda: collections.defaultdict(_trie)
        trie = _trie()
        for i, word in enumerate(words):
            reduce(dict.__getitem__, word, trie)["_end"] = i

        # DFS
        stack = trie.values()
        result = ""
        while stack:
            curr = stack.pop()
            if "_end" in curr:
                word = words[curr["_end"]]
                if len(word) > len(result) or (len(word) == len(result) and word < result):
                    result = word
                stack += [curr[letter] for letter in curr if letter != "_end"]
        return result

class TrieNode:
    def __init__(self):
        self.is_string = False
        self.leaves = {}

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        valid = True
        curr = self.root
        for id, c in enumerate(word,1):
            if not c in curr.leaves:
                curr.leaves[c] = TrieNode()
            curr = curr.leaves[c]

            if not curr.is_string and id != len(word):
                valid = False
        curr.is_string = True
        return valid

# bad: 1. Need to sort first (has to insert short word before long word); 2. trie takes space
class Solution_ming(object):
    def longestWord(self, words):
        res = ''
        words = sorted(words)
        d = WordDictionary()
        for w in words:
            valid = d.addWord(w)
            print w, valid
            if valid and len(w) > len(res):
                res = w
        return res

class Solution_bruteForce(object):
    def longestWord(self, words):
        ans = ""
        wordset = set(words)
        for word in words:
            if len(word) > len(ans) or len(word) == len(ans) and word < ans:
                if all(word[:k] in wordset for k in xrange(1, len(word))):
                    ans = word

        return ans

print Solution().longestWord(["w","wo","wor","worl", "world"])
#print Solution().longestWord(["htncv","htncvn","ht","mvaq","h","htnc"])
#print Solution().longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"])
#print Solution().longestWord(["yo","ew","fc","zrc","yodn","fcm","qm","qmo","fcmz","z","ewq","yod","ewqz","y"])