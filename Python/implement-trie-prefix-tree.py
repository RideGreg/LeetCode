# Time:  O(n), per operation
# Space: O(1)
# 208
# Implement a trie with insert, search, and startsWith methods.
#
# Note:
# You may assume that all inputs are consist of lowercase letters a-z.
#

import collections

class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.is_string = False
        self.leaves = collections.defaultdict(TrieNode)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        cur = self.root
        for c in word:
            cur = cur.leaves[c]
        cur.is_string = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        node = self.childSearch(word)
        return node is not None and node.is_string

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        return self.childSearch(prefix) is not None

    def childSearch(self, word):
        cur = self.root
        for c in word:
            cur = cur.leaves.get(c, None)
            if cur is None:
                break
        return cur

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")


# Implement trie with nested dict
# http://stackoverflow.com/questions/11015320/how-to-create-a-trie-in-python
_end = '_end_'
class Trie2:
    def __init__(self):
        self.root = {}

    def make_trie(self, *words):
        root = {}
        for word in words:
            cur = root
            for c in word:
                cur = cur.setdefault(c, {})
            cur[_end] = _end
        self.root = root

    def search(self, word):
        cur = self.root
        for c in word:
            if c not in cur:
                return False
            cur = cur[c]
        else:
            return _end in cur

    def startsWith(self, prefix):
        cur = self.root
        for c in prefix:
            if c not in cur:
                return False
            cur = cur[c]
        return True

trie2 = Trie()
for w in ('foo', 'bar', 'baz', 'barz'):
    trie2.insert(w)
print(trie2.search('bar')) #True
print(trie2.search('baa')) #False
print(trie2.search('ba'))  #False
print(trie2.startsWith('baz')) #True
print(trie2.startsWith('ba')) #True
print(trie2.startsWith('c')) #False
