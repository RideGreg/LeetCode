# Time:  O(n)
# Space: O(n)

# Given a string, find the first non-repeating character in it and
# return it's index. If it doesn't exist, return -1.
#
# Examples:
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode",
# return 2.
# Note: You may assume the string contain only lowercase letters.


from collections import defaultdict

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        lookup = defaultdict(int)
        candidtates = set()
        for i, c in enumerate(s):
            if lookup[c]:
                candidtates.discard(lookup[c])
            else:
                lookup[c] = i+1
                candidtates.add(i+1)

        return min(candidtates)-1 if candidtates else -1

    def firstUniqChar_ming1(self, s):  # USE THIS
        import collections
        d = collections.Counter(s)
        return next((i for i, c in enumerate(s) if d[c] == 1), -1)

    def firstUniqChar_ming2(self, s):
        import collections
        od = collections.OrderedDict()
        for i, c in enumerate(s):
            od[c] = i if c not in od else -1  # record index for uniq char, -1 for duplicate char

        # https://stackoverflow.com/questions/2361426/get-the-first-item-from-an-iterable-that-matches-a-condition
        return next((v for v in od.values() if v >= 0), -1)
