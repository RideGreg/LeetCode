# Time:  O((logn)^2) = O(1) due to n is a 32-bit number
# Space: O(logn) = O(1)

# Starting with a positive integer N,
# we reorder the digits in any order (including the original order)
# such that the leading digit is not zero.
#
# Return true if and only if we can do this in a way
# such that the resulting number is a power of 2.
#
# Example 1:
#
# Input: 1
# Output: true
# Example 2:
#
# Input: 10
# Output: false
# Example 3:
#
# Input: 16
# Output: true
# Example 4:
#
# Input: 24
# Output: false
# Example 5:
#
# Input: 46
# Output: true
#
# Note:
# - 1 <= N <= 10^9

import collections


class Solution(object):
    def reorderedPowerOf2(self, N): # USE THIS hash solution
        """
        :type N: int
        :rtype: bool
        """
        # for original and reordered number, the count of their digits are the same.
        # check against all power of 2: 2^0 .. 2^30
        count = collections.Counter(str(N))
        return any(count == collections.Counter(str(1 << i))
                   for i in xrange(31)) # 10^9 ~= 2^30

    def reorderedPowerOf2_permutation(self, N):  # TLE
        """
        In the last line, 'for cand in itertools.permutations(str(N))' will
        iterate through the six possibilities cand = ('1', '2', '8'),
        cand = ('1', '8', '2'), cand = ('2', '1', '8'), and so on.

        The check cand[0] != '0' is a check that the candidate permutation
        does not have a leading zero.

        The check bin(int("".join(cand))).count('1') == 1 is a check that cand
        represents a power of 2: namely, that the number of ones in its binary
        representation is 1.
        """
        import itertools
        return any(cand[0] != '0' and bin(int("".join(cand))).count('1') == 1
                   for cand in itertools.permutations(str(N)))

    def reorderedPowerOf2_permutation2(self, N):  # TLE
        s = str(N)
        l = len(s)

        def gen(s):
            if not s: yield ''
            for i in xrange(len(s)):
                if len(s) != l or s[i] != '0':
                    for ss in gen(s[:i]+s[i+1:]):
                        yield s[i] + ss

        def isPower2(x):
            while x != 1:
                prev, x = x, x>>1
                if x*2 != prev:
                    return False
            return True

        for x in gen(s):
            if isPower2(int(x)):
                return True
        return False