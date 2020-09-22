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
    # Greedy: 
    # 1. If two num-pair can chain, it is good and we increment chain length by 1; 

    # 2. If they overlap, which one to keep? the one with smaller end, so we leave more
    # space for future pairs. This also answers the question should we sort by begin or by end.
    # If sorting by begin, if 2nd pair overlaps 1st pair, we still need to compare their
    # ends to determine which one to keep -- not good as we sorting by end.

    # 3. If we have a chain, we just need to keep the last item's end, and the info of all
    # previous items no longer useful. Why? For next num-pair, if can extend, we extend
    # the chain; if it overlaps the last item, no matter the new pair overlaps the last last
    # item or not, it won't imporve the chain length AND it is always better to keep 
    # the last item (skip the new one) so we have a smaller end. 
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