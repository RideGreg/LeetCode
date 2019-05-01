# Time:  O(n^2), n is the length of S
# Space: O(1)

# 1016
# Given a binary string S (a string consisting only of '0' and '1's) and a positive integer N,
# return true if and only if for every integer X from 1 to N, the binary representation of X is a
# substring of S.
#
# Input: S = "0110", N = 3
# Output: true
#
# Input: S = "0110", N = 4
# Output: false
#
# 1 <= S.length <= 1000
# 1 <= N <= 10^9

class Solution(object):
    def queryString(self, S, N):
        """
        :type S: str
        :type N: int
        :rtype: bool
        """
        # brute force checking N, then N-1, until N//2+1 (for every i <= N//2, its binary 
        # string will be contained in binary string of 2*i)
        #
        # Another proof:
        # since S with length n has at most different n-k+1 k-digit numbers
        # => given S with length n, valid N is at most 2(n-k+1)
        # => valid N <= 2(n-k+1) < 2n = 2 * S.length
        return all(bin(i)[2:] in S for i in reversed(range(N//2 + 1, N+1)))
