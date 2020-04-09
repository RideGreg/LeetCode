# Time:  O(n), n is the length of key
# Space: O(t), t is the number of nodes in trie

# Implement a MapSum class with insert, and sum methods.
#
# For the method insert, you'll be given a pair of (string, integer).
# The string represents the key and the integer represents the value.
# If the key already existed, then the original key-value pair will be overridden to the new one.
#
# For the method sum, you'll be given a string representing the prefix,
# and you need to return the sum of all the pairs' value whose key starts with the prefix.
#
# Example 1:
# Input: insert("apple", 3), Output: Null
# Input: sum("ap"), Output: 3
# Input: insert("app", 2), Output: Null
# Input: sum("ap"), Output: 5

import collections

class TrieNode(object):
    def __init__(self):
        self.v = 0
        self.leaves = collections.defaultdict(TrieNode)

class MapSum:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        cur = self.root
        for c in key:
            cur = cur.leaves[c]
        cur.v = val

    def sum(self, prefix: str) -> int:
        ans, cur = 0, self.root
        for c in prefix:
            cur = cur.leaves.get(c, None)
            if not cur: return 0

        stk = [cur]
        while stk:
            node = stk.pop()
            ans += node.v
            for ch in node.leaves.values():
                stk.append(ch)
        return ans

class MapSum2(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        _trie = lambda: collections.defaultdict(_trie)
        self.__root = _trie()

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        # Time: O(n)
        curr = self.__root
        for c in key:
            curr = curr[c]
        delta = val
        if "_end" in curr:
            delta -= curr["_end"]

        curr = self.__root
        for c in key:
            curr = curr[c]
            if "_count" in curr:
                curr["_count"] += delta
            else:
                curr["_count"] = delta
        curr["_end"] = val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        # Time: O(n)
        curr = self.__root
        for c in prefix:
            if c not in curr:
                return 0
            curr = curr[c]
        return curr["_count"]


# Your MapSum object will be instantiated and called as such:
obj = MapSum()
obj.insert("apple", 3)
print(obj.sum("ap")) # 3
obj.insert("app", 2)
print(obj.sum("ap")) # 5
