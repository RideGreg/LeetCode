# Time:  O(n), n is the total sum of the lengths of folder names
# Space: O(t), t is the number of nodes in trie

# 1233 weekly contest 159 10/19/2019

# Given a list of folders, remove all sub-folders in those folders and return in any order the folders after removing.
#
# If a folder[i] is located within another folder[j], it is called a sub-folder of it.
#
# The format of a path is one or more concatenated strings of the form: / followed by one or more lowercase English letters.
# For example, /leetcode and /leetcode/problems are valid paths while an empty string and / are not.

# Constraints:
#
# 1 <= folder.length <= 4 * 10^4
# 2 <= folder[i].length <= 100
# folder[i] contains only lowercase letters and '/'
# folder[i] always starts with character '/'
# Each folder name is unique.

import collections
import itertools

class TrieNode:
    def __init__(self):
        self.is_string = False
        self.leaves = collections.defaultdict(TrieNode)

class Solution(object):
    def removeSubfolders(self, folder): # USE THIS
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        def dfs(cur, path):
            if cur.is_string:
                ans.append('/' + '/'.join(path))
                return
            for dir, nxt in cur.leaves.items():
                dfs(nxt, path + [dir])

        root = TrieNode()
        for f in folder:
            cur = root
            for dir in f.split('/')[1:]:
                cur = cur.leaves[dir]
            cur.is_string = True

        ans = []
        dfs(root, [])
        return ans

    # follow up: instead of returning parent folders, now return leaf folders and how many paths included in each leaf-folder path.
    def removeSubfolders_followup(self, folder):
        def dfs(cur, path, cnt):
            if cur.is_string:
                cnt += 1
            if not cur.leaves:
                ans.append(('/' + '/'.join(path), cnt))
                return
            for dir, nxt in cur.leaves.items():
                dfs(nxt, path + [dir], cnt)

        root = TrieNode()
        for f in folder:
            cur = root
            for dir in f.split('/')[1:]:
                cur = cur.leaves[dir]
            cur.is_string = True

        ans = []
        dfs(root, [], 0)
        return ans

    def removeSubfolders_kamyu(self, folder):
        def dfs(curr, path, result):
            if "_end" in curr:
                result.append("/" + "/".join(path))
                return
            for c in curr:
                if c == "_end":
                    continue
                path.append(c)
                dfs(curr[c], path, result)
                path.pop()

        _trie = lambda: collections.defaultdict(_trie)
        trie = _trie()
        for f in folder:
            f_list = f.split("/")
            reduce(dict.__getitem__,
                   itertools.islice(f_list, 1, len(f_list)),
                   trie).setdefault("_end")
        result = []
        dfs(trie, [], result)
        return result
  
print(Solution().removeSubfolders(["/a/b","/a","/c/d","/c/d/e","/c/f"])) # ["/a","/c/d","/c/f"]
print(Solution().removeSubfolders(["/a/b/c","/a/b/ca","/a/b/d"])) # ["/a/b/c","/a/b/ca","/a/b/d"]
print(Solution().removeSubfolders(["/a/b/c","/a","/a/b/d"])) # ["/a"]

print(Solution().removeSubfolders_followup(["/a/b","/a","/c/d","/c/d/e","/c/f"])) # [("/a/b",2), ("/c/d/e",2), ("/c/f",1)]
print(Solution().removeSubfolders_followup(["/a/b/c","/a/b/ca","/a/b/d"])) # [("/a/b/c",1), ("/a/b/ca",1), ("/a/b/d",1)]
print(Solution().removeSubfolders_followup(["/a/b/c","/a","/a/b/d"])) # [("/a/b/c",2), ("/a/b/d",2)]