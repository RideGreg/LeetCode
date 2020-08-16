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

import collections
class TrieNode:             # 节点上存储 二有(leaves, is_string)一没有(char key)
    # Initialize your data structure here.
    def __init__(self):     # Note 1: char not stored on TrieNode, {char: TrieNode} is the key-value pair in 'leaves' dict
        self.is_string = False
        self.leaves = collections.defaultdict(TrieNode) # Note 2: defaultdict takes param of class name, not a object


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        curr = self.root
        for c in word:
            curr = curr.leaves[c]
        curr.is_string = True       # Note 3: don't forget set the flag!

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    # 对于dot char可能match多个子节点，普通的for loop是顺序执行，无法回溯处理。必须用递归recursion或者栈stack保留待处理子节点。
    def search(self, word):
        def dfs(i, node):  # dfs 参数一般包括当前index和状态信息
            if i == len(word):
                return node.is_string

            c = word[i]
            if c in node.leaves:
                return dfs(i + 1, node.leaves[c])
            elif c == '.':
                for new_node in node.leaves.values():
                    if dfs(i + 1, new_node):
                        return True
            return False

        return dfs(0, self.root)

    def search_iteration(self, word):  #不用递归用stack实现dfs，与简单dfs遍历不同的是，必须在每个entry记录状态信息
        stk = [(0, self.root)]
        while stk:
            i, node = stk.pop()
            if i == len(word):
                if node.is_string:
                    return True
            else:
                c = word[i]
                if c in node.leaves:
                    stk.append((i + 1, node.leaves[c]))
                elif c == '.':
                    for new_node in node.leaves.values():
                        stk.append((i+1, new_node))
        return False

# Your WordDictionary object will be instantiated and called as such:
wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
wordDictionary.addWord("bx")
print(wordDictionary.search("mad")) # False
print(wordDictionary.search(".ad")) # True
print(wordDictionary.search("b..")) # True
print(wordDictionary.search("b.")) # True
print(wordDictionary.search("b...")) # False
