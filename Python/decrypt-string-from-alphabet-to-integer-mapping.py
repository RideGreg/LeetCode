# Time:  O(n)
# Space: O(1)

# 1309 weekly contest 170 1/4/2020

# # Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase
# # characters as follows:
# #
# # Characters ('a' to 'i') are represented by ('1' to '9') respectively.
# # Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
# # Return the string formed after mapping.
# #
# # It's guaranteed that a unique mapping will always exist.

# forward solution
class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        def alpha(num):
            return chr(ord('a') + int(num)-1)

        i = 0
        result = []
        while i < len(s):
            if i+2 < len(s) and s[i+2] == '#':
                result.append(alpha(s[i:i+2]))
                i += 3
            else:
                result.append(alpha(s[i]))
                i += 1
        return "".join(result)


# Time:  O(n)
# Space: O(1)
# backward solution
class Solution2(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        def alpha(num):
            return chr(ord('a') + int(num)-1)

        i = len(s)-1
        result = []
        while i >= 0:
            if s[i] == '#':
                result.append(alpha(s[i-2:i]))
                i -= 3
            else:
                result.append(alpha(s[i]))
                i -= 1
        return "".join(reversed(result))

# Time:  O(n)
# Space: O(1)
import re


# regex solution
class Solution3(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        def alpha(num):
            return chr(ord('a') + int(num)-1)

        return "".join(alpha(i[:2]) for i in re.findall(r"\d\d#|\d", s))

print(Solution().freqAlphabets("10#11#12")) # 'jkab'
print(Solution().freqAlphabets("1326#")) # 'acz'
print(Solution().freqAlphabets("25#")) # 'y
print(Solution().freqAlphabets("12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"))
# "abcdefghijklmnopqrstuvwxyz"