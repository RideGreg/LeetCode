# Time:  create: O(n)
#        get:    O(n)
# Space: O(n)

# 1166
# You are asked to design a file system which provides two functions:
#
# 1. createPath(path, value): Creates a new path and associates a value to it if possible and returns True.
# Returns False if the path already exists or its parent path doesn't exist.
# 2. get(path): Returns the value associated with a path or returns -1 if the path doesn't exist.
#
# The format of a path is one or more concatenated strings of the form: / followed by one or more
# lowercase English letters. For example, /leetcode and /leetcode/problems are valid paths while
# an empty string and / are not.

# Hint: What if you think of a tree hierarchy for the files? A path is a node in the tree.
# Use a hash table to store the valid paths along with their values.

# Hash table solution: prefix in path will stored in multiple keys.
class FileSystem(object):
    def __init__(self):
        self.__lookup = {"": -1}

    def create(self, path: str, value: int) -> bool:
        if path[:path.rfind('/')] not in self.__lookup:
            return False
        self.__lookup[path] = value
        return True
        
    def get(self, path: str) -> int:
        return self.__lookup.get(path, -1)


# Trie solution
import collections
class TrieNode(object):
    def __init__(self, x):
        self.val = x
        self.children = collections.defaultdict(TrieNode)

class FileSystem2(object):
    def __init__(self):
        self.root = TrieNode(None)

    def create(self, path: str, value: int) -> bool:
        cur = self.root
        dirs = self.__split(path)
        for s in dirs[:-1]:
            if s not in cur.children:
                return False
            cur = cur.children[s]
        cur.children[dirs[-1]] = TrieNode(value)
        return True

    def get(self, path: str) -> int:
        cur = self.root
        for s in self.__split(path):
            if s not in cur.children:
                return -1
            cur = cur.children[s]
        return cur.val

    def __split(self, path):
        if path == '/':
            return []
        return path.split('/')[1:]


obj = FileSystem()
print(obj.create("/a", 1)) # True
print(obj.get("/a")) # 1

print(obj.create("/leet", 1)) # True
print(obj.create("/leet/code", 2)) # True
print(obj.get("/leet/code")) # 2
print(obj.create("/c/d", 1)) # False
print(obj.get("/c")) # -1

