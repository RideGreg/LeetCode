# Time:  O(n*l + m*L), m is the number of puzzles, L is the length of puzzles
#                    , n is the number of words, l is the max length of words
# Space: O(L!)

# 1178
# With respect to a given puzzle string, a word is valid if both the following conditions are satisfied:
# - word contains the first letter of puzzle.
# - For each letter in word, that letter is in puzzle.

# For example, if the puzzle is "abcdefg", then valid words are "faced", "cabbage", and "baggage";
# while invalid words are "beefed" (doesn't include "a") and "based" (includes "s" which isn't in the puzzle).
# Return an array answer, where answer[i] is the number of words in the given word list words that are
# valid with respect to the puzzle puzzles[i].

# 1 <= words.length <= 10^5, 4 <= words[i].length <= 50
# 1 <= puzzles.length <= 10^4, puzzles[i].length == 7
# words[i][j], puzzles[i][j] are English lowercase letters.
# Each puzzles[i] doesn't contain repeated characters.
#


# 最普通的思路是对每个 puzzle，都对 words 遍历一遍，方法很直观，但一定超时。words.length * puzzles.length 会达到 10^9

# 如何大大缩短时间？其实我们可以发现一些规律和题目给我们的暗示：
# 对于 word，其实每个 word 代表了一种模式，abc 和 aaaaabbbccc 是等价的。 我们需要提取出这种模式(位运算)
# 对于一个 puzzle，有两种遍历谜底的思路。 一是遍历 words，另一种是遍历自己的模式子集。题目给我们的暗示是
# puzzles[i].length == 7。这就意味着一个 puzzle 的模式，子集不会超过 2^7 = 128
# 因此我们遍历 puzzle 模式的子集，采用 map 映射的方式统计谜底个数。

# 如何将一个字符串转化为他所对应的模式? 这就可以巧妙地用到位运算，字母只有26个，因此可以很轻松的将每个字符串
# 转化为一个 int 型数据。同样，每个 puzzle 字符串也可以转化为这样的模式。
#

class Solution(object):
    def findNumOfValidWords(self, words, puzzles):
        """
        :type words: List[str]
        :type puzzles: List[str]
        :rtype: List[int]
        """
        L = 7
        def search(node, puzzle, start, first, met_first):
            result = 0
            if "_end" in node and met_first:
                result += node["_end"];
            for i in xrange(start, len(puzzle)):
                if puzzle[i] not in node:
                    continue
                result += search(node[puzzle[i]], puzzle, i+1,
                                 first, met_first or (puzzle[i] == first))
            return result

        _trie = lambda: collections.defaultdict(_trie)
        trie = _trie()
        for word in words:
            count = set(word)
            if len(count) > L:
                continue
            word = sorted(count)
            end = reduce(dict.__getitem__, word, trie)
            end["_end"] = end["_end"]+1 if "_end" in end else 1
        result = []
        for puzzle in puzzles:
            first = puzzle[0]
            result.append(search(trie, sorted(puzzle), 0, first, False))
        return result


# Time:  O(m*2^(L-1) + n*(l+m)), m is the number of puzzles, L is the length of puzzles
#                              , n is the number of words, l is the max length of words
# Space: O(m*2^(L-1))
import collections


class Solution(object):
    def findNumOfValidWords(self, words, puzzles):
        """
        :type words: List[str]
        :type puzzles: List[str]
        :rtype: List[int]
        """
        L = 7
        lookup = collections.defaultdict(list)
        for i, puzzle in enumerate(puzzles):
            bits = []
            base = 1 << (ord(puzzle[0])-ord('a'))
            for j in range(1, L):
                bits.append(ord(puzzle[j])-ord('a'))
            for k in range(2**len(bits)): # <= 2**6 = 64
                bitset = base
                for j in range(len(bits)):
                    if k & (1<<j):
                        bitset |= 1<<bits[j]
                lookup[bitset].append(i)

        result = [0]*len(puzzles)
        for word in words:
            bitset = 0
            for c in word:
                bitset |= 1 << (ord(c)-ord('a'))
            if bitset not in lookup:
                continue
            for i in lookup[bitset]:
                result[i] += 1
        return result

    # O(len(words) * len(puzzles)) -> 10^9
    def findNumOfValidWords_TLE(self, words, puzzles):
        wset = list(map(set, words))
        pset = list(map(set, puzzles))

        return [sum(p[0] in wset[i] and wset[i] < pset[j] for i,w in enumerate(words))
               for j,p in enumerate(puzzles)]

print(Solution().findNumOfValidWords(
    ["aaaa","asas","able","ability","actt","actor","access"],
    ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"])) # [1,1,3,2,4,0]