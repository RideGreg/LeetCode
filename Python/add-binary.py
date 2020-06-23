# Time:  O(n)
# Space: O(1)
# 67
# Given two binary strings, return their sum (also a binary string).
#
# For example,
# a = "11"
# b = "1"
# Return "100".
#

try:
    xrange          # Python 2
except NameError:
    xrange = range  # Python 3


class Solution(object):
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        m, n, c = len(a)-1, len(b)-1, 0
        ans = []
        while m >= 0 or n >= 0 or c:
            if m >= 0:
                c += int(a[m])
                m -= 1
            if n >= 0:
                c += int(b[n])
                n -= 1
            c, v = divmod(c, 2)
            ans.append(str(v))
        return ''.join(ans[::-1])


# Time:  O(n)
# Space: O(1)
from itertools import izip_longest


class Solution2(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = ""
        carry = 0
        for x, y in izip_longest(reversed(a), reversed(b), fillvalue="0"):
            carry, remainder = divmod(int(x)+int(y)+carry, 2)
            result += str(remainder)
        
        if carry:
            result += str(carry)
        
        return result[::-1]
