# Time:  O(nlogn)
# Space: O(1)

# 646
# You are given n pairs of numbers.
# In every pair, the first number is always smaller than the second number.
#
# Now, we define a pair (c, d) can follow another pair (a, b)
# if and only if b < c. Chain of pairs can be formed in this fashion.
#
# Given a set of pairs, find the length longest chain which can be formed.
# You needn't use up all the given pairs. You can select pairs in any order.
#
# Example 1:
# Input: [[1,2], [2,3], [3,4]]
# Output: 2
# Explanation: The longest chain is [1,2] -> [3,4]
# Note:
# The number of given pairs will be in the range [1, 1000].

class Solution(object):
    # Greedy: among all num-pair can put in front of current num-pair,
    # choose the one with smallest end number.
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        ans, last = 0, float('-inf')
        for b, e in sorted(pairs, key=lambda x: x[1]):
            if last < b:
                ans += 1
                last = e
        return ans


    # DP O(n^2)
    def findLongestChain_TLE(self, pairs):
        pairs.sort()
        dp = [1] * len(pairs)

        for j in range(len(pairs)):
            for i in range(j):
                if pairs[i][1] < pairs[j][0]:
                    dp[j] = max(dp[j], dp[i] + 1)

        return max(dp)

print(Solution().findLongestChain([[1,2], [2,3], [3,4]])) # 2