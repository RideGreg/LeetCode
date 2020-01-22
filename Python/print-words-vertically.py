# Time:  O(n)
# Space: O(n)

# 1324 weekly contest 172 1/18/2020

# Given a string s. Return all the words vertically in the same order in which they appear in s.
# Words are returned as a list of strings, complete with spaces when is necessary. (Trailing spaces are not allowed).
# Each word would be put on only one column and that in one column there will be only one word.

# It's guaranteed that there is only one space between 2 words.

import itertools


class Solution(object):
    def printVertically(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        return ["".join(c).rstrip() for c in itertools.izip_longest(*s.split(), fillvalue=' ')]

    def printVertically_ming(self, s):
        words = s.split()
        longest = max(words, key=len)
        ans = [[] for _ in range(len(longest))]
        for w in words:
            for i in range(len(longest)):
                ans[i].append(w[i] if i < len(w) else ' ')
        return [''.join(x).rstrip() for x in ans]


print(Solution().printVertically("HOW ARE YOU")) # ["HAY","ORO","WEU"]
# "HAY"
# "ORO"
# "WEU"
print(Solution().printVertically("TO BE OR NOT TO BE")) # ["TBONTB","OEROOE","   T"]
# "TBONTB"
# "OEROOE"
# "   T"
print(Solution().printVertically("CONTEST IS COMING")) # ["CIC","OSO","N M","T I","E N","S G","T"]
