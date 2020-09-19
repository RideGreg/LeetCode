# Time:  O(n * d), n is length of string, d is size of dictionary
# Space: O(d)
#
# Given two words (start and end), and a dictionary, find the length of shortest transformation sequence from start to end, such that:
#
# Only one letter can be changed at a time
# Each intermediate word must exist in the dictionary
# For example,
#
# Given:
# start = "hit"
# end = "cog"
# dict = ["hot","dot","dog","lot","log"]
# As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.
#
# Note:
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
#

# BFS
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        distance, cur, visited, lookup = 0, [beginWord], set([beginWord]), set(wordList)

        while cur:
            next_queue = []

            for word in cur:
                if word == endWord:
                    return distance + 1
                for i in range(len(word)):
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        candidate = word[:i] + j + word[i + 1:]
                        if candidate not in visited and candidate in lookup:
                            next_queue.append(candidate)
                            visited.add(candidate)
            distance += 1
            cur = next_queue

        return 0


# Time:  O(26 * d * l) = O(d * l), d is the size of wordlist, l is the max length of words
# Space: O(d * l)

from string import ascii_lowercase


# two-end bfs
class Solution2(object):
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0
        words = set(wordList)
        is_found, left, right, is_reversed = False, {beginWord}, {endWord},  False
        ladder = 2
        while left:
            words -= set(left)
            new_left = set()
            for word in left:
                for new_word in [word[:i]+c+word[i+1:] for i in xrange(len(beginWord)) for c in ascii_lowercase]:
                    if new_word in words:
                        if new_word in right: 
                            return ladder
                        else: 
                            new_left.add(new_word)
            left = new_left
            ladder += 1
            if len(left) > len(right): 
                left, right, is_reversed = right, left, not is_reversed
        return 0


# Time:  O(26 * d * l) = O(d * l), d is the size of wordlist, l is the max length of words
# Space: O(d * l)
class Solution3(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        lookup = set(wordList)
        if endWord not in lookup:
            return 0
        ladder = 2
        q = [beginWord]
        while q:
            new_q = []
            for word in q:
                for i in xrange(len(word)):
                    for j in ascii_lowercase:
                        new_word = word[:i] + j + word[i+1:]
                        if new_word == endWord:
                            return ladder
                        if new_word in lookup:
                            lookup.remove(new_word)
                            new_q.append(new_word)
            q = new_q
            ladder += 1
        return 0


if __name__ == "__main__":
    print(Solution().ladderLength("hit", "cog", set(["hot", "dot", "dog", "lot", "log"])))
    print(Solution().ladderLength("hit", "cog", set(["hot", "dot", "dog", "lot", "log", "cog"])))
