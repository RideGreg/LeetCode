# Time:  O(1), if we take the length of S, TS,T as O(1).
# Space: O(1)

# Given two strings S and T, each of which represents a non-negative rational number, return True if and only if
# they represent the same number. The strings may use parentheses to denote the repeating part of the rational number.
#
# In general a rational number can be represented using up to three parts: an integer part, a non-repeating part,
# and a repeating part. The number will be represented in one of the following three ways:
#
# <IntegerPart> (e.g. 0, 12, 123)
# <IntegerPart><.><NonRepeatingPart>  (e.g. 0.5, 1., 2.12, 2.0001)
# <IntegerPart><.><NonRepeatingPart><(><RepeatingPart><)> (e.g. 0.1(6), 0.9(9), 0.00(1212))

# The repeating portion of a decimal expansion is conventionally denoted within a pair of round brackets.  For example:
#
# 1 / 6 = 0.16666666... = 0.1(6) = 0.1666(6) = 0.166(66)
#
# Both 0.1(6) or 0.1666(6) or 0.166(66) are correct representations of 1 / 6.



# idea: As both numbers represent a fraction, we need a fraction class to handle fractions.
# The hard part is the repeating part.
# Say we have a string like S = "0.(12)". It represents (for r = \frac{1}{100}):
#
# S = \frac{12}{100} + \frac{12}{10000} + \frac{12}{10^6} + \frac{12}{10^8} + \frac{12}{10^10} + ...
# S = 12 * (r + r^2 + r^3 + ...)
# S = 12 * \frac{r}{1-r}
#
# as the sum (r + r^2 + r^3 + ...) is a geometric sum. A geometric series is a series with a constant ratio between successive terms.
# In general, for a repeating part x with length k, we have r = 10^(-k) and the contribution is \frac{xr}{1-r}.
#
# The other two parts are easier, as it is just a literal interpretation of the value.

from fractions import Fraction


class Solution(object):
    def isRationalEqual(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def frac(s):
            dotParts = s.split('.')
            ans = Fraction(int(dotParts[0]), 1)

            if len(dotParts) > 1:
                decimal = dotParts[1].split('(')
                if decimal[0]:
                    ans += Fraction(int(decimal[0]), 10 ** len(decimal[0]))

                if len(decimal) > 1:
                    repeatPart = decimal[1][:-1]
                    ans += Fraction(int(repeatPart), 10 ** len(decimal[0]) * (10 ** len(repeatPart) - 1))

            return ans

        return frac(S) == frac(T)

    def isRationalEqual_leetcodeOfficial(self, S, T):
        def frac(S):
            if '.' not in S:
                return Fraction(int(S), 1)

            i = S.index('.')
            result = Fraction(int(S[:i]), 1)
            non_int_part = S[i+1:]
            if '(' not in non_int_part:
                if non_int_part:
                    result += Fraction(int(non_int_part), 10**len(non_int_part))
                return result

            i = non_int_part.index('(')
            if i:
                result += Fraction(int(non_int_part[:i]), 10**i)
            repeat_part = non_int_part[i+1:-1]
            result += Fraction(int(repeat_part), 10**i * (10**len(repeat_part)-1))
            return result

        return frac(S) == frac(T)

print(Solution().isRationalEqual("0.(52)", "0.5(25)")) # True
print(Solution().isRationalEqual("0.1666(6)", "0.166(66)")) # True
print(Solution().isRationalEqual("0.9(9)", "1.")) # True