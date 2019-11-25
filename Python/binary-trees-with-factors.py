# Time:  O(n^2)
# Space: O(n)

# 823
# Given an array of unique integers, each integer is strictly greater than 1.
# We make a binary tree using these integers and each number may be used for
# any number of times.
# Each non-leaf node's value should be equal to the product of the values of
# it's children.
# How many binary trees can we make?  Return the answer modulo 10 ** 9 + 7.
#
# Example 1:
#
# Input: A = [2, 4]
# Output: 3
# Explanation: We can make these trees: [2], [4], [4, 2, 2]
# Example 2:
#
# Input: A = [2, 4, 5, 10]
# Output: 7
# Explanation: We can make these trees:
#              [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].
#
# Note:
# - 1 <= A.length <= 1000.
# - 2 <= A[i] <= 10 ^ 9.


# DP: The largest value v used must be the root node in the tree. Say dp(v) is # of ways to
# make a tree with root node v.
#
# If the root node of the tree (with value v) has children with values x and y (and x * y == v),
# then there are dp(x) * dp(y) ways to make this tree.

try:
    xrange          # Python 2
except NameError:
    xrange = range  # Python 3


class Solution(object):
    def numFactoredBinaryTrees(self, A): # USE THIS. But dict cannot handle follow up of non-unique + each number use once.
        """
        :type A: List[int]
        :rtype: int
        """
        import collections
        MOD = 10**9 + 7
        A.sort()
        dp = {}
        for i in range(len(A)):
            dp[A[i]] = 1
            for j in range(i):
                q, r = divmod(A[i], A[j])
                if r == 0 and q in dp:
                    dp[A[i]] += dp[A[j]]*dp[q]
                    dp[A[i]] %= MOD
        return sum(dp.values()) % MOD

    # Follow up: if non-unique and each number use only once. Use array. need index for reverse look up.
    def numFactoredBinaryTrees_awice(self, A):
        MOD = 10 ** 9 + 7
        N = len(A)
        A.sort()
        dp = [1] * N
        index = {x: i for i, x in enumerate(A)}
        for i, x in enumerate(A):
            for j in xrange(i):
                if x % A[j] == 0: #A[j] will be left child
                    right = x / A[j]
                    if right in index:
                        dp[i] += dp[j] * dp[index[right]]
                        dp[i] %= MOD

        return sum(dp) % MOD

print(Solution().numFactoredBinaryTrees([2,4])) # 3
print(Solution().numFactoredBinaryTrees([2,4,5,10])) # 7