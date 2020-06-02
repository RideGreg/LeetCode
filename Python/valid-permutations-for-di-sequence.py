# Time:  O(n^2)
# Space: O(n)

# 903
# We are given S, a length n string of characters from the set {'D', 'I'}.
# (These letters stand for "decreasing" and "increasing".)
#
# A valid permutation is a permutation P[0], P[1], ..., P[n]
# of integers {0, 1, ..., n}, such that for all i:
#
# If S[i] == 'D', then P[i] > P[i+1], and;
# If S[i] == 'I', then P[i] < P[i+1].
# How many valid permutations are there?
# Since the answer may be large, return your answer modulo 10^9 + 7.
#
# Example 1:
#
# Input: "DID"
# Output: 5
# Explanation: 
# The 5 valid permutations of (0, 1, 2, 3) are:
# (1, 0, 3, 2)
# (2, 0, 3, 1)
# (2, 1, 3, 0)
# (3, 0, 2, 1)
# (3, 1, 2, 0)
#
# Note:
# - 1 <= S.length <= 200
# - S consists only of characters from the set {'D', 'I'}.

# Solution: Dynamic Programming
# Ituition: try to put down digits 1 by 1.

# Ituition uses 2d, actual implementation uses 1d (each iteration represents a new row in dp[0], dp[1].. dp[n]).
# dp[i][j] means # of possible permutations of first i + 1 digits,
# where the i + 1th digit using j + 1th RELATIVELY smallest in the remaining of digits.
# rows represent the sequence composed of n+1, n, n-1 ... 1 digits,
# cols 0 -> j in row i is to choose a digit from RELATIVELY smallest to largest from the remaining available digits.
# Sample dp array for 'DD':
#   i=0: 1, 1, 1 (using 0, using 1, using 2 at 1st char all have 1 permutation)
#          |  /|
#          |/ |
#         /  |
#   i=1: 2, 1 (permutations using 0 at 2nd char = sum(perm of using k at 1 st char, where k is any digits > 0);
#          |   permutations using 1 at 2nd char = perm of using 2 at 1 st char;
#         |    permutations using 2 at 2nd char = None;
#        |     In actual implementation, prefix / postfix sum is a shortcut for computation)
#   i=2: 1
class Solution(object):
    def numPermsDISequence(self, S):
        """
        :type S: str
        :rtype: int
        """
        # Initially, for 1-digit permutation, any digit from the n+1 available digits can be used,
        # # of permutations for using smallest (0) to largest digit (n) is always 1
        dp = [1]*(len(S)+1)
        for c in S:         # for 2nd, 3rd ... digits
            if c == "I":
                dp = dp[:-1] # if Increasing, the last col in last dp used the largest digit, thus useless.
                for i in range(1, len(dp)): # prefix sum
                    dp[i] += dp[i-1]
            else:
                dp = dp[1:] # if Decreasing, the first col in last dp represents using the relatively smallest digit, thus useless
                for i in reversed(range(len(dp)-1)): # suffix sum
                    dp[i] += dp[i+1]
        return dp[0] % (10**9+7)

print(Solution().numPermsDISequence("DD")) # 1: dp [1,1,1] -> [2,1] -> [1]
print(Solution().numPermsDISequence("DI")) # 2: dp [1,1,1] -> [2,1] -> [2]
print(Solution().numPermsDISequence("ID")) # 2: dp [1,1,1] -> [1,2] -> [2]
print(Solution().numPermsDISequence("II")) # 1: dp [1,1,1] -> [1,2] -> [1]
print(Solution().numPermsDISequence("DID"))# 5: dp [1,1,1,1] -> [3,2,1] -> [3,5] -> [5]
print(Solution().numPermsDISequence("DDID"))# 9: dp [1,1,1,1,1] -> [4,3,2,1] -> [6,3,1] -> [6,9] -> [9]
