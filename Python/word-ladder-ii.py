# Time:  O(b^(d/2)), b is the branch factor of bfs, d is the result depth
# Space: O(w * l), w is the number of words, l is the max length of words

import collections
from string import ascii_lowercase

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

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        def backtracking(tree, beginWord, word): 
            return [[beginWord]] if word == beginWord else [path + [word] for new_word in tree[word] for path in backtracking(tree, beginWord, new_word)]

        words = set(wordList)
        if endWord not in words:
            return []
        tree = defaultdict(set)
        is_found, left, right, is_reversed = False, {beginWord}, {endWord}, False
        while left:
            words -= set(left)
            new_left = set()
            for word in left:
                for new_word in [word[:i]+c+word[i+1:] for i in xrange(len(beginWord)) for c in ascii_lowercase]:
                    if new_word not in words:
                        continue
                    if new_word in right: 
                        is_found = True
                    else: 
                        new_left.add(new_word)
                    tree[new_word].add(word) if not is_reversed else tree[word].add(new_word)
            if is_found:
                break
            left = new_left
            if len(left) > len(right): 
                left, right, is_reversed = right, left, not is_reversed
        return backtracking(tree, beginWord, endWord)


# BFS: ask for SHORTEST SEQUENCES
# If two words has 1 char diff, they are connected in BFS.
# Since path needs to output, we record the path along the BFS. And trace back to produces the paths.
# Time:  O(b^d), b is the branch factor of bfs, d is the result depth
# Space: O(w * l), w is the number of words, l is the max length of words
class Solution2(object):
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def findLadders(self, start, end, wrodList):
        def backtrack(word, path):
            if word not in trace:
                path.append(word)
                result.append(path[::-1])
                path.pop()
            else:
                for prev in trace[word]:
                    path.append(word)
                    self.backtrack(result, trace, path, prev)
                    path.pop()

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
class Solution3:
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
