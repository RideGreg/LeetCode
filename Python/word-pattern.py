# Time:  O(n)
# Space: O(c), c is unique count of pattern

 # 290
# Given a pattern and a string str, find if str follows the same pattern.
#
# Examples:
#   1. pattern = "abba", str = "dog cat cat dog" should return true.
#   2. pattern = "abba", str = "dog cat cat fish" should return false.
#   3. pattern = "aaaa", str = "dog cat cat dog" should return false.
#   4. pattern = "abba", str = "dog dog dog dog" should return false.
#
# Notes:
#   1. Both pattern and str contains only lowercase alphabetical letters.
#   2. Both pattern and str do not have leading or trailing spaces.
#   3. Each word in str is separated by a single space.
#   4. Each letter in pattern must map to a word with length that is at least 1.

#from itertools import izip  # Generator version of zip.
import collections
class Solution(object):
    # Time:  O(n), Space: O(n)
    # maintain 2 dicts for a char's last position. Map patterns to id,
    # better than mapping between the patterns.
    def wordPattern(self, pattern: str, str: str) -> bool: # USE THIS
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split()
        if len(pattern) != len(words): # necessary! e.g. 'aa', 'bb bb bb'
            return False

        lookup1, lookup2 = {}, {}
        for i, c in enumerate(pattern):
            id1, id2 = lookup1.get(c, -1), lookup2.get(words[i], -1)
            if id1 != id2:
                return False
            lookup1[c] = lookup2[words[i]] = i
        return True


    def wordPattern2(self, pattern, str): # also good
        words = str.split()  # Space: O(n)
        if len(pattern) != len(words):
            return False

        p2s, usedword = {}, set()
        for i, c in enumerate(pattern):
            if c in p2s:
                if words[i] != p2s[c]:
                    return False
            else:
                if words[i] in usedword:
                    return False
                # Build mapping. Space: O(c)
                p2s[c] = words[i]
                usedword.add(words[i])
        return True

    # Time O(nlogn) SLOW: sort array to judge equality is unnecessary
    def wordPattern3(self, pattern: str, str: str) -> bool:
        def divideGroups(iterable):
            cnt = collections.defaultdict(list)
            for i, c in enumerate(iterable):
                cnt[c].append(i)
            return sorted(cnt.values())

        return divideGroups(pattern) == divideGroups(str.split(' '))

    # 比较乱，不用。主要参考一下generator写法如何节省空间。
    def wordPattern4(self, pattern, str):
        if len(pattern) != self.wordCount(str):
            return False

        w2p, p2w = {}, {}
        for p, w in zip(pattern, self.wordGenerator(str)):
            if w not in w2p and p not in p2w:
                # Build mapping. Space: O(c)
                w2p[w] = p
                p2w[p] = w
            elif w not in w2p or w2p[w] != p:
                # Contradict mapping.
                return False
        return True

    def wordCount(self, str): # don't produce array, save space
        cnt = 1 if str else 0
        for c in str:
            if c == ' ':
                cnt += 1
        return cnt

    # Generate a word at a time without saving all the words.
    def wordGenerator(self, str):
        w = ""
        for c in str:
            if c == ' ':
                yield w
                w = ""
            else:
                w += c
        yield w


print(Solution().wordPattern("abba", "dog cat cat dog")) # True
print(Solution().wordPattern("abba", "dog cat cat fish")) # False
print(Solution().wordPattern("abba", "dog dog dog dog")) # False
print(Solution().wordPattern('aa', 'bb bb bb')) # False