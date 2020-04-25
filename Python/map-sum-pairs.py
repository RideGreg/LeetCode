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
        self.sum = 0
        self.v = 0
        self.leaves = collections.defaultdict(TrieNode)

class MapSum:   # USE THIS: calculation in 'insert' time, 'sum' is fast
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        cur = self.root
        for c in key:
            cur = cur.leaves[c]

        delta = val - cur.v  # if set new value to the same string, cannot simply add
        cur.v = val

        cur = self.root
        for c in key:
            cur = cur.leaves[c]
            cur.sum += delta

    def sum(self, prefix: str) -> int:
        cur = self.root
        for c in prefix:
            if c not in cur.leaves:
                return 0
            cur = cur.leaves[c]
        return cur.sum

    ''' THIS IS WRONG when insert is actually OVERWRITE
    ["MapSum", "insert", "sum", "insert", "sum"]
    [[], ["aa",3], ["a"], ["aa",2], ["a"]]
    if wnat to update values during insert, need to use delta
    
    def insert(self, key: str, val: int) -> None:
        cur = self.root
        for c in key:
            cur = cur.leaves[c]
            cur.v += val

    def sum(self, prefix: str) -> int:
        ans, cur = 0, self.root
        for c in prefix:
            if c not in cur.leaves:
                return 0
            cur = cur.leaves[c]
        return cur.v'''

class TrieNode2(object):
    def __init__(self):
        self.v = 0
        self.leaves = collections.defaultdict(TrieNode2)

class MapSum2:
    def __init__(self):
        self.root = TrieNode2()

    def insert(self, key: str, val: int) -> None:
        cur = self.root
        for c in key:
            cur = cur.leaves[c]
        cur.v = val

    def sum(self, prefix: str) -> int:
        ans, cur = 0, self.root
        # find the node corresponding to 'prefix'
        for c in prefix:
            if c not in cur.leaves:
                return 0
            cur = cur.leaves[c]
        # DFS to sum up all words with the prefix
        stk = [cur]
        while stk:
            node = stk.pop()
            ans += node.v
            for ch in node.leaves.values():
                stk.append(ch)
        return ans


class MapSum_kamyu(object):
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
obj.insert("app", 8)
print(obj.sum("ap")) # 11
