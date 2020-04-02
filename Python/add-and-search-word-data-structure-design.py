# Time:  O(min(n, h)), per operation
# Space: O(min(n, h))

# 211
# Ming: Time Complexity:  addWord - O(L) ,   search - O(26L)，  Space Complexity - O(26L)   这里 L是单词的平均长度。
# http://www.cnblogs.com/yrbbest/p/4979621.html
# More follow up: http://www.cnblogs.com/EdwardLiu/p/5052887.html
#
# Design a data structure that supports the following two operations:
#
# void addWord(word)
# bool search(word)
# search(word) can search a literal word or a regular expression string
# containing only letters a-z or ..
# A . means it can represent any one letter.
#
# For example:
#
# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
# Note:
# You may assume that all words are consist of lowercase letters a-z.
#


class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.is_string = False
        self.leaves = {}


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        curr = self.root
        for c in word:
            if c not in curr.leaves:
                curr.leaves[c] = TrieNode()  # use defaultdict(TreeNode) can save these two lines
            curr = curr.leaves[c]
        curr.is_string = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        def helper(i, node):
            if i == len(word):
                return node.is_string

            c = word[i]
            if c in node.leaves:
                return helper(i + 1, node.leaves[c])
            elif c == '.':
                for d in node.leaves:
                    if helper(i + 1, node.leaves[d]):
                        return True
            return False

        return helper(0, self.root)

# Your WordDictionary object will be instantiated and called as such:
wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
print(wordDictionary.search("mad")) # False
print(wordDictionary.search(".ad")) # True
print(wordDictionary.search("b..")) # True
print(wordDictionary.search("b.")) # False
