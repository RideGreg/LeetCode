# Time:  O(n)
# Space: O(1)

# 1018
# Given an array A of 0s and 1s, consider N_i: the i-th subarray from A[0] to A[i] interpreted
# as a binary number (from most-significant-bit to least-significant-bit.)
#
# Return a list of booleans answer, where answer[i] is true if and only if N_i is divisible by 5.

# Input: [0,1,1]
# Output: [true,false,false]
# Explanation:
# The input numbers in binary are 0, 01, 011; which are 0, 1, and 3 in base-10.  Only the first
# number is divisible by 5, so answer[0] is true.

# Input: [0,1,1,1,1,1]
# Output: [true,false,false,false,true,false]

class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        ans, n = [], 0
        for x in A:
            n = (n*2+x) % 5 # mod 5, so vastly more efficient for both time and space complexity
            ans.append(False if n%5 else True)
        return ans

    def prefixesDivBy5_(self, A):
        for i in range(1, len(A)):
            A[i] += A[i-1] * 2 % 5
        return [x % 5 == 0 for x in A]
