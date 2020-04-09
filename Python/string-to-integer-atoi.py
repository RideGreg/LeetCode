# Time:  O(n)
# Space: O(1)
#
# Implement atoi to convert a string to an integer.
#
# Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below
# and ask yourself what are the possible input cases.
#
# Notes: It is intended for this problem to be specified vaguely (ie, no given input specs).
# You are responsible to gather all the input requirements up front.
#
# spoilers alert... click to show requirements for atoi.
#
# Requirements for atoi:
# The function first discards as many whitespace characters as necessary
# until the first non-whitespace character is found. Then, starting from this character,
# takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
#
# The string can contain additional characters after those that
# form the integral number, which are ignored and have no effect on the behavior of this function.
#
# If the first sequence of non-whitespace characters in str is not a valid integral number,
# or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
#
# If no valid conversion could be performed, a zero value is returned.
# If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.
#

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        i, n, sign = 0, len(str), 1
        ans, INT_MAX = 0, 2**31 - 1 # INT_MIN can be represented by INT_MAX
        while i < n and str[i] == ' ':
            i += 1
        if i < n and str[i] in '+-':
            sign = 1 if str[i] == '+' else -1
            i += 1
        while i < n and str[i].isdigit():
            ans = 10 * ans + int(str[i])
            i += 1
            if ans > INT_MAX:      # prune
                return INT_MAX if sign > 0 else -1 * (INT_MAX+1)
        return sign * ans

    def myAtoi_noPrune(self, str: str) -> int:
        i, n, neg = 0, len(str), 0
        while i < n and str[i] == ' ':
            i += 1
        if i < n and str[i] in '+-':
            neg = 1 if str[i] == '-' else 0
            i += 1

        j = i       # get all digits then discard overflown digits: unnecessary
        while j < n and '0'<=str[j]<='9':
            j += 1
        if j == i: return 0
        num = int(str[i:j])

        if neg:
            return -1 * min(2**31, num)
        else:
            return min(2**31-1, num)

print(Solution().myAtoi("   -42")) # 42
print(Solution().myAtoi("-91283472332")) # -2147483648