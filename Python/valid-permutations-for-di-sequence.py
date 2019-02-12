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

# dp[i][j] means the number of possible permutations of first i + 1 digits,
# where the i + 1th digit using j + 1th smallest in the remaining of digits.
# rows are form n+1, n, n-1 ... 1 digits sequence
# cols 0 -> j in row i is to choose a digit from smallest to largest from the remaining available digits.
class Solution(object):
    def numPermsDISequence(self, S):
        """
        :type S: str
        :rtype: int
        """
        # Initially, any digit from the n+1 available digits can be put down, the possible ways for any of them is always 1
        dp = [1]*(len(S)+1)
        for c in S:
            if c == "I":
                dp = dp[:-1] # if Increasing, the last col in previous row already used the largest digit, thus cannot use further
                # calculate prefix sum: because every previous col can contribute to current largest digit, every previous col
                # except the last can contribute to current 2nd-largest digit
                for i in xrange(1, len(dp)):
                    dp[i] += dp[i-1]
            else:
                dp = dp[1:] # if Decreasing, the first col in previous row already used the smallest digit, thus cannot use further
                for i in reversed(xrange(len(dp)-1)): # calculate suffix sum
                    dp[i] += dp[i+1]
        return dp[0] % (10**9+7)

print(Solution().numPermsDISequence("DD")) # 1: dp [1,1,1] -> [2,1] -> [1]
print(Solution().numPermsDISequence("DI")) # 2: dp [1,1,1] -> [2,1] -> [2]
print(Solution().numPermsDISequence("ID")) # 2: dp [1,1,1] -> [1,2] -> [2]
print(Solution().numPermsDISequence("II")) # 1: dp [1,1,1] -> [1,2] -> [1]
print(Solution().numPermsDISequence("DID"))# 5: dp [1,1,1,1] -> [3,2,1] -> [3,5] -> [5]
print(Solution().numPermsDISequence("DDID"))# 9: dp [1,1,1,1,1] -> [4,3,2,1] -> [6,3,1] -> [6,9] -> [9]
