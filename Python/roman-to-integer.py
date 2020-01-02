# Time:  O(n)
# Space: O(1)

# 13
#
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#                                                            1 5 10 50 100 500 1000
# Roman numerals are usually written largest to smallest from left to right.  12 is written as, XII,
# which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
#
# However, the number four is written as IV. Because the one is before the five we subtract it making four. The same
# principle applies to the number nine, which is written as IX. There are *six instances where subtraction is used*:
#
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
#
# Rules for subtracting letters:
#
# 1. Subtract only powers of ten, such as I, X, or C. Writing VL for 45 is not allowed: write XLV instead.
# 2. Subtract only a SINGLE letter from a SINGLE numeral. Write VIII for 8, not IIX; 19 is XIX, not IXX.
# 3. Don't subtract a letter from another letter more than ten times greater. This means that you can only subtract
#    I from V or X, and X from L or C, so MIM is illegal.

# Using the strict rules of Roman Numerals, the largest number that can be represented is 4,999.
# For large numbers, the Romans often wrote a bar above a numeral. The bar meant to multiply by 1000. E.g. 7000 would be (bar over) VII.

# Given a roman numeral, convert it to an integer.
# Input is guaranteed to be within the xrange from 1 to 3999.

class Solution:
    # @return an integer
    def romanToInt(self, s):
        numeral_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C":100, "D": 500, "M": 1000}
        decimal = 0
        for i in range(len(s)):
            if i > 0 and numeral_map[s[i]] > numeral_map[s[i - 1]]:
                decimal += numeral_map[s[i]] - 2 * numeral_map[s[i - 1]]
            else:
                decimal += numeral_map[s[i]]
        return decimal

if __name__ == "__main__":
    print(Solution().romanToInt("LVIII")) # 58
    print(Solution().romanToInt("MMMCMXCIX")) # 3999 = MMM 3000 + CM 900 + XC 90 + IX 9
    print(Solution().romanToInt("MCMXCIV")) # 1994 = M 1000 + CM 900 + XC 90 + IV 4
