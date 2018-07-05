# Time:  O(n), n is the total sum of the lengths of words
# Space: O(t), t is the number of nodes in trie

# Given a list of words, we may encode it by writing a reference
# string S and a list of indexes A.
#
# For example, if the list of words is ["time", "me", "bell"],
# we can write it as S = "time#bell#"
# and indexes = [0, 2, 5].
#
# Then for each index, we will recover the word by reading from
# the reference string from that
# index until we reach a "#" character.
#
# What is the length of the shortest reference string S possible
# that encodes the given words?
#
# Example:
#
# Input: words = ["time", "me", "bell"]
# Output: 10
# Explanation: S = "time#bell#" and indexes = [0, 2, 5].
#
# Note:
# 1. 1 <= words.length <= 2000.
# 2. 1 <= words[i].length <= 7.
# 3. Each word has only lowercase letters.

import collections
import functools


class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.leaves = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        cur = self.root
        for c in word:
            if not c in cur.leaves:
                cur.leaves[c] = TrieNode()
            cur = cur.leaves[c]

    def levelOrderTraverse(self):
        ans = level = 0
        q = [self.root]
        while q:
            q0 = []
            level += 1
            for node in q:
                if not node.leaves:
                    ans += level
                else:
                    q0 += list(node.leaves.values())
            q = q0
        return ans

class Solution(object):
    def minimumLengthEncoding(self, words): # USE THIS
        """
        :type words: List[str]
        :rtype: int
        """
        words = set(words)
        trie = Trie()
        for w in words:
            trie.insert(w[::-1])
        return trie.levelOrderTraverse()

    def minimumLengthEncoding_anotherTrie(self, words):
        words = list(set(words))
        #Trie is a nested dictionary with nodes created when fetched entries are missing. Same as:
        #def _trie():
        #    return collections.defaultdict(_trie)
        _trie = lambda: collections.defaultdict(_trie)
        trie = _trie()

        '''
        reduce(..., S, trie) is trie[S[0]][S[1]][S[2]][...][S[S.length - 1]].
        Each step creats a empty defaultdict; for string at leaf node, the final is also an empty defaultdict.
        After this is done, trie looks like
        defaultdict({
            'e': defaultdict( {'m': defaultdict(  {'i': defaultdict(  {'t': defaultdict(  {})})})}),
            'l': defaultdict( {'l': defaultdict(  {'e': defaultdict(  {'b': defaultdict(  {})})})})
        })
        nodes looks like (for 'em', 'lleb', 'emit'):
        [ defaultdict( {'i': defaultdict(  {'t': defaultdict(  {})})}),
          defaultdict( {}),
          defualtdict( {})
        ]
        '''
        nodes = [functools.reduce(dict.__getitem__, word[::-1], trie)
                 for word in words]

        #Add word to the answer if it's node has no neighbors
        return sum(len(word) + 1
                   for i, word in enumerate(words)
                   if len(nodes[i]) == 0)

    def minimumLengthEncoding_set(self, words):
        good = set(words)
        for word in words:
            for k in range(1, len(word)): # each word's length is up to 7
                good.discard(word[k:])
        return sum(len(word) + 1 for word in good)

    # sort O(nlogn)
    def minimumLengthEncoding_sort(self, words):
        words = sorted(w[::-1] for w in set(words))
        ans, last = 0, ''
        for w in words:
            if not w.startswith(last):
                ans += len(last)+1
            last = w
        return ans+len(last)+1

print Solution().minimumLengthEncoding(["time", "me", "bell"])
print Solution().minimumLengthEncoding(["ahour", "atime", "btime"])