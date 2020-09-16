# Time:  O(n * d^2), n is length of string, d is size of dictionary. In BFS, search neighbors for
#             each word is nested loop O(d^2), compare if they diff by 1 char O(n)
# Space: O(d^2) BFS worst case edge # is O(d^2), all nodes connected to each other.

# 126
# Given two words (start and end), and a dictionary, find all shortest transformation sequence(s)
# from start to end, such that:
#
# Only one letter can be changed at a time
# Each intermediate word must exist in the dictionary. Note that beginWord is not a transformed word, but endWord is.
# For example,
#
# Given:
# start = "hit"
# end = "cog"
# dict = ["hot","dot","dog","lot","log","cog]
# Return
#   [
#     ["hit","hot","dot","dog","cog"],
#     ["hit","hot","lot","log","cog"]
#   ]
# Note:
# All words have the same length.
# All words contain only lowercase alphabetic characters.
#

# BFS: ask for SHORTEST SEQUENCES
# If two words has 1 char diff, they are connected in BFS.
# Since path needs to output, we record the path along the BFS. And trace back to produces the paths.
class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def findLadders(self, start, end, wrodList):
        def backtrack(word, path):
            if word not in trace:
                ans.append([word] + path)
                return

            for prev in trace[word]:
                backtrack(prev, [word] + path)

        dict = set(wrodList)
        dict.add(end)
        # BFS
        cur, visited = [start], set([start])
        trace, found = collections.defaultdict(list), False
        while cur and not found:
            for word in cur:
                visited.add(word)

            next = set()
            for word in cur:
                for i in range(len(word)):
                    for j in range(26):
                        c = chr(j + ord('a'))
                        ww = word[:i] + c + word[i + 1:]
                        if ww not in visited and ww in dict:
                            if ww == end:
                                found = True
                            next.add(ww)
                            trace[ww].append(word)
            cur = next

        ans = []
        if found:
            backtrack(end, [])
        return ans


# Backtracking: TLE, since it visits many non-minimum path.
import collections
class Solution2:
    def findLadders(self, beginWord, endWord, wordList):
        def backtrack(curPath):
            w = curPath[-1]
            if w == endWord:
                if len(curPath) <= self.minL:
                    self.minL = len(curPath)
                    path[self.minL].append(curPath[:])
                return

            if len(curPath) > self.minL: return # prune

            for i in range(len(w)):
                for j in range(26):
                    c = chr(j + ord('a'))
                    ww = w[:i] + c + w[i+1:]
                    if ww != w and ww in wordset and ww not in used:
                        used.add(ww)
                        curPath.append(ww)
                        backtrack(curPath)
                        curPath.pop()
                        used.discard(ww)

        wordset = set(wordList)
        self.minL, path = float('inf'), collections.defaultdict(list)
        used = set([beginWord])
        backtrack([beginWord])
        return path[self.minL] if path else []


print(Solution().findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
    #     ["hit","hot","dot","dog","cog"],
    #     ["hit","hot","lot","log","cog"]

print(Solution().findLadders("qa", "sq", [
    "si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca",
    "br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au",
    "ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga",
    "li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er",
    "sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"
]))
# [['qa', 'ba', 'be', 'se', 'sq'], ['qa', 'ba', 'bi', 'si', 'sq'], ['qa', 'ba', 'br', 'sr', 'sq'],
# ['qa', 'ca', 'ci', 'si', 'sq'], ['qa', 'ca', 'cm', 'sm', 'sq'], ['qa', 'ca', 'co', 'so', 'sq'],
# ['qa', 'ca', 'cr', 'sr', 'sq'], ['qa', 'fa', 'fe', 'se', 'sq'], ['qa', 'fa', 'fm', 'sm', 'sq'],
# ['qa', 'fa', 'fr', 'sr', 'sq'], ['qa', 'ga', 'ge', 'se', 'sq'], ['qa', 'ga', 'go', 'so', 'sq'],
# ['qa', 'ha', 'he', 'se', 'sq'], ['qa', 'ha', 'hi', 'si', 'sq'], ['qa', 'ha', 'ho', 'so', 'sq'],
# ['qa', 'la', 'le', 'se', 'sq'], ['qa', 'la', 'li', 'si', 'sq'], ['qa', 'la', 'ln', 'sn', 'sq'],
# ['qa', 'la', 'lo', 'so', 'sq'], ['qa', 'la', 'lr', 'sr', 'sq'], ['qa', 'la', 'lt', 'st', 'sq'],
# ['qa', 'ma', 'mb', 'sb', 'sq'], ['qa', 'ma', 'me', 'se', 'sq'], ['qa', 'ma', 'mi', 'si', 'sq'],
# ['qa', 'ma', 'mn', 'sn', 'sq'], ['qa', 'ma', 'mo', 'so', 'sq'], ['qa', 'ma', 'mr', 'sr', 'sq'],
# ['qa', 'ma', 'mt', 'st', 'sq'], ['qa', 'na', 'nb', 'sb', 'sq'], ['qa', 'na', 'ne', 'se', 'sq'],
# ['qa', 'na', 'ni', 'si', 'sq'], ['qa', 'na', 'no', 'so', 'sq'], ['qa', 'pa', 'pb', 'sb', 'sq'],
# ['qa', 'pa', 'ph', 'sh', 'sq'], ['qa', 'pa', 'pi', 'si', 'sq'], ['qa', 'pa', 'pm', 'sm', 'sq'],
# ['qa', 'pa', 'po', 'so', 'sq'], ['qa', 'pa', 'pt', 'st', 'sq'], ['qa', 'ra', 'rb', 'sb', 'sq'],
# ['qa', 'ra', 're', 'se', 'sq'], ['qa', 'ra', 'rh', 'sh', 'sq'], ['qa', 'ra', 'rn', 'sn', 'sq'],
# ['qa', 'ta', 'tb', 'sb', 'sq'], ['qa', 'ta', 'tc', 'sc', 'sq'], ['qa', 'ta', 'th', 'sh', 'sq'],
# ['qa', 'ta', 'ti', 'si', 'sq'], ['qa', 'ta', 'tm', 'sm', 'sq'], ['qa', 'ta', 'to', 'so', 'sq'],
# ['qa', 'ya', 'yb', 'sb', 'sq'], ['qa', 'ya', 'ye', 'se', 'sq'], ['qa', 'ya', 'yo', 'so', 'sq']]