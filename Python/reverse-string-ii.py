# Time:  O(n)
# Space: O(1)

# Given a string and an integer k, you need to reverse the first k characters
# for every 2k characters counting from the start of the string.
# If there are less than k characters left, reverse all of them.
# If there are less than 2k but greater than or equal to k characters,
# then reverse the first k characters and left the other as original.
# Example:
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
# Restrictions:
# The string consists of lower English letters only.
# Length of the given string and k will in the range [1, 10000]

# https://stackoverflow.com/questions/931092/reverse-a-string-in-python
class Solution(object):
    def reverseStr(self, s, k): # 2.24 s, most readable
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # why change to list? 'str' object is immutable and does not support item assignment
        s = list(s)
        for i in xrange(0, len(s), 2*k):
            s[i:i+k] = reversed(s[i:i+k])
        return "".join(s)
    def reverseStr2(self, s, k): # 1.11 s, fastest
        ss = ''
        for i in xrange(0, len(s), k):
            if i == 0:
                ss += s[k-1::-1]
            else:
                ss += s[i+k-1:i-1:-1] if i % 2 == 0 else s[i:i+k]
        return ss
    def reverseStr3(self, s, k): # 3.16 s, slowest
        ss = ''
        for i in xrange(0, len(s), k):
            ss += ''.join(reversed(s[i:i+k])) if i % 2 == 0 else s[i:i+k]
        return ss

print    Solution().reverseStr('abcdefxyabcdefxyabcdefxyabcdefg', 2)
print    Solution().reverseStr2('abcdefxyabcdefxyabcdefxyabcdefg', 2)
print    Solution().reverseStr3('abcdefxyabcdefxyabcdefxyabcdefg', 2)

import time
start = time.time()
for i in xrange(200000):
    Solution().reverseStr('abcdefxyabcdefxyabcdefxyabcdefg', 2)
print "%s seconds" % (time.time()-start)
start = time.time()
for i in xrange(200000):
    Solution().reverseStr2('abcdefxyabcdefxyabcdefxyabcdefg', 2)
print "%s seconds" % (time.time()-start)
start = time.time()
for i in xrange(200000):
    Solution().reverseStr3('abcdefxyabcdefxyabcdefxyabcdefg', 2)
print "%s seconds" % (time.time()-start)
