# Time:  O(n)
# Space: O(1)

# 926 contest 107 10/20/2018
# A string of '0's and '1's is monotone increasing if it consists of some number of '0's (possibly 0),
# followed by some number of '1's (also possibly 0.)
#
# We are given a string S of '0's and '1's, and we may flip any '0' to a '1' or a '1' to a '0'.
#
# Return the minimum number of flips to make S monotone increasing.

# Dynamic Programming

class Solution(object):
    def minFlipsMonoIncr_ming(self, S): # USE THIS, easy to understand
        old0, old1 = 0, 0
        for c in S:
            new0 = old0 + int(c)
            new1 = min(old0, old1) + 1 - int(c)
            old0, old1 = new0, new1
        return min(old0, old1)

    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        flip0, flip1 = 0, 0
        for c in S:
            flip0 += int(c == '1')
            flip1 = min(flip0, flip1 + int(c == '0'))
        return flip1

# Prefix Sums
# The answer has two halves, a left (zero) half, and a right (one) half.
#
# It comes down to a question of knowing, for each candidate half: how many ones are in the left half,
# and how many zeros are in the right half.
#
# We calculate prefix sums P in linear time. Then if we want x zeros followed by N-x ones,
# there are P[x] ones in the start that must be flipped, plus (N-x) - (P[N] - P[x]) zeros that must be flipped.
#
# We take the minimum among all candidate answers to arrive at the final answer.
# Time:  O(n)
# Space: O(n)

    def minFlipsMonoIncr_prefixSum(self, S):
        P = [0]
        for x in S:
            P.append(P[-1] + int(x))

        return min(P[j] + len(S)-j-(P[-1]-P[j])
                   for j in xrange(len(P)))

print(Solution().minFlipsMonoIncr('00110')) # 1
print(Solution().minFlipsMonoIncr('010110')) # 2
print(Solution().minFlipsMonoIncr('00011000')) # 2
