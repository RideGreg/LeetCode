# Time:  O(n^0.25 * logn)
# Space: O(logn)

# 906
# Let's say a positive integer is a superpalindrome
# if it is a palindrome, and it is also the square of a palindrome.
#
# Now, given two positive integers L and R (represented as strings),
# return the number of superpalindromes in the inclusive range [L, R].
#
# Example 1:
#
# Input: L = "4", R = "1000"
# Output: 4
# Explanation: 4, 9, 121, and 484 are superpalindromes.
# Note that 676 is not a superpalindrome: 26 * 26 = 676,
# but 26 is not a palindrome.
#
# Note:
# - 1 <= len(L) <= 18
# - 1 <= len(R) <= 18
# - L and R are strings representing integers in the range [1, 10^18).
# - int(L) <= int(R)
                                                        
# Solution: Mathematical
# Say P = R^2 is a superpalindrome. Because R is a palindrome, assume k is the first half of the digits in R,  k determine
# R up to two possibilities. We can iterate through k. For example, if k=1234, then R = 1234321 (odd # of digits) or
# 12344321 (even # of digits).
#
# Notice because P < 10^18, R < 10^9, and R=k|k' (concatenation), where k' is k reversed (and also possibly truncated
# by one digit); so that k < 10^5=MAGIC, our magic constant.

# For each 1<=k<MAGIC, create the associated palindrome R, and check whether R^2 is a palindrome.
#
# We should handle the odd and even possibilities separately, as we would like to break early so as not to do extra work.
#
# To check whether an integer is a palindrome, we could check whether it is equal to its reverse. To create the reverse
# of an integer, we can do it digit by digit.

class Solution(object):
    def superpalindromesInRange(self, L, R):
        """
        :type L: str
        :type R: str
        :rtype: int
        """
        def is_palindrome(k):
            return str(k) == str(k)[::-1]

        halfLen = (len(R)+1) / 4.0 # KENG: not using float will truncate to int: e.g. if len(R)=2 shouldn't be 0
        limit = int( 10**halfLen )
        l, r = int(L), int(R)

        result = 0

        # count odd length
        for k in xrange(limit):
            s = str(k)
            t = s + s[-2::-1]
            v = int(t)**2
            # early exit
            if v > r:
                break
            if v >= l and is_palindrome(v):
                result += 1

        # count even length
        for k in xrange(limit):
            s = str(k)
            t = s + s[::-1]
            v = int(t)**2
            # early exit
            if v > r:
                break
            if v >= l and is_palindrome(v):
                result += 1

        return result
