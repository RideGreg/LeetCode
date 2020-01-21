# Time:  O(n)
# Space: O(1)

# 821 weekly contest 81 4/21/2018


# Given a string S and a character C,
# return an array of integers representing the shortest distance
# from the character C in the string.
#
# Example 1:
#
# Input: S = "loveleetcode", C = 'e'
# Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
#
# Note:
# - S string length is in [1, 10000].
# - C is a single character, and guaranteed to be in string S.
# - All letters in S and C are lowercase.

import itertools

try:
    xrange          # Python 2
except NameError:
    xrange = range  # Python 3


class Solution(object):
    def shortestToChar(self, S, C): # USE THIS: two pass
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        result = [float('inf')] * len(S)
        prev = float('inf')
        for i in itertools.chain(xrange(len(S)), reversed(xrange(len(S)))): # iterator saves space
        #to_iterate = list(range(len(S))) + list(reversed(range(len(S))))
        #for i in to_iterate:
            if S[i] == C:
                prev = i
            result[i] = min(result[i], abs(i-prev))
        return result

    # Space O(n)
    def shortestToChar_ming(self, S, C):
        pos = [i for i, x in enumerate(S) if x==C]
        cur = 0
        pre, post = float('-inf'), pos[cur]
        ans = []
        for i, x in enumerate(S):
            if x == C:
                ans.append(0)
                pre = post
                cur += 1
                post = pos[cur] if cur < len(pos) else float('inf')
            else:
                ans.append(min(abs(i-pre), abs(i-post)))
        return ans


print(Solution().shortestToChar("loveleetcode", 'e')) # [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
print(Solution().shortestToChar("loveleetcode", 't')) # [7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4]
print(Solution().shortestToChar("loveleetcodea", 'a')) # [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(Solution().shortestToChar("xloveleetcode", 'x')) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
