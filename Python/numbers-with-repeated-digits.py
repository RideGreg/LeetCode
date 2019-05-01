# Time:  O(logn), the # of permutations A(m,n) is O(1), We count digit by digit, so it's O(logN)
# Space: O(logn)

# 1012
# Given a positive integer N, return the number of positive integers less than or
# equal to N that have at least 1 repeated digit.

# Solution: Similar as
# 788. Rotated Digits
# 902. Numbers At Most N Given Digit Set
#
# Explanation:
# - Transform N + 1 to arrayList
# - Count the number with digits < n
# - Count the number with same prefix
# For example,
# if N = 8765, L = [8,7,6,6],
# the number without repeated digit can the the following format:
# XXX
# XX
# X
# 1XXX ~ 7XXX
# 80XX ~ 86XX
# 870X ~ 875X
# 8760 ~ 8765

from functools import lru_cache

class Solution(object):
    def numDupDigitsAtMostN(self, N):
        """
        :type N: int
        :rtype: int
        """
        # Permutation: P(9,3) = 9*8*7, P(9,2) = 9*8, P(9,1) = 9
        @lru_cache(None)
        def P(m, n):
            if n == 0:
                return 1
            return P(m, n-1) * (m-n+1)

        digits = list(map(int, str(N+1)))
        result, L = 0, len(digits)

        # Given 321
        #
        # 1. count numbers without repeated digits:
        # - X
        # - XX
        for i in range(1, L):
            result += 9 * P(9, i-1) # 9 * (9*8*7...)
        
        # 2. count numbers without repeated digits:
        # - 1XX ~ 2XX
        # - 30X ~ 31X
        # - 320 ~ 321
        prefix_set = set()
        for i, x in enumerate(digits):
            for y in range(1 if i == 0 else 0, x):
                if y not in prefix_set:
                    result += P(9-i, L-i-1) # actually select L-i-1 from 10-i-1 numbers
            if x in prefix_set:
                break
            prefix_set.add(x)
        return N-result

    def numDupDigitsAtMostN_ming(self, n):
        s = str(n)
        bit = len(s)
        unique = self.countUniqueUpToLength(bit - 1)
        # no need to consider number > 9999999999, because all digits are used, no more unique digits
        if bit > 10:
            return n - unique

        # consider numbers with same leading digits
        used = []  # used digits
        for i in range(bit - 1):
            head = int(s[i])  ### !!! better to sore as integer array
            if i == 0:
                mult = head - 1  # digit 0 cannot used as beginning
            else:
                mult = head - sum(1 for x in used if x < head)

            if mult > 0:
                unique += mult * self.countUniqueInRemainBits(i, bit - i - 1)

            if head not in used:  # put head at current position, count remaining positions
                used.append(head)
            else:  # not unique, no need to count numbers with head at current position, i.e. 44xxx
                return n - unique


        start = 1 if bit == 1 else 0  # if single digit, 0 cannot be used as last digit
        unique += sum(1 for i in xrange(start, int(s[-1]) + 1) if i not in used)
        return n - unique

    # count of numbers with unique digits with length <= bit (not including number 0, as
    # when calculating count of numbers w/ repeated digits = n - #unique, n doesn't include 0 either)
    # The general dynamic programming formula: for k>=2, f(k) = 9*9*8*7 ... * 9-k+2.
    # bit <=:  0 1 2  3          4
    # #unique: 0 9 90 90+648=738 738+4536=5274
    def countUniqueUpToLength(self, bit): #!!! suggest this API only canculate one length, do sum outside of calling this API.
        if bit == 0: return 0

        count, fk = 9, 9
        for k in xrange(2, min(bit + 1, 11)):
            fk *= 10 - (k - 1)
            count += fk
        return count

    # bit is # of bits need to put digit at, i is positions already determined in original
    # input number, i.e. i+1 digits were used, only 10-(i+1) digits available, so start with 9-i
    def countUniqueInRemainBits(self, i, bit):
        if bit == 0:
            return 1  # return value is used in multiplication
        ans, start = 1, 9 - i
        for _ in range(bit):
            ans *= start
            start -= 1
        return ans

print(Solution().numDupDigitsAtMostN(20)) # 1
print(Solution().numDupDigitsAtMostN(100)) # 10
print(Solution().numDupDigitsAtMostN(1000)) # 262