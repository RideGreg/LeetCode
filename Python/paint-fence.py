# Time:  O(n)
# Space: O(1)

# 276
# There is a fence with n posts, each post can be painted with one of the k colors.
#
# You have to paint all the posts such that no more than two adjacent fence posts have the same color.
#
# Return the total number of ways you can paint the fence.
#
# Note:
# n and k are non-negative integers.

# DP solution with rolling window.
class Solution(object):
    # for each new post i, it can be "same" color with post i-1 if we haven't have same color neighbors before.
    # or it has "diff" color with post i-1. The total # of ways on each post is "same+diff".
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0: return 0
        same, diff = 0, k
        for i in range(2, n+1):
            same, diff = diff, (k-1) * (same+diff)
        return same + diff

    def numWays_kamyu(self, n, k):
        if n == 0:
            return 0
        elif n == 1:
            return k
        ways = [0] * 3
        ways[0] = k
        ways[1] = (k - 1) * ways[0] + k
        for i in range(2, n):
            ways[i % 3] = (k - 1) * (ways[(i - 1) % 3] + ways[(i - 2) % 3])
        return ways[(n - 1) % 3]

# Time:  O(n)
# Space: O(n)
# DP solution.
class Solution2(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1:
            return k
        ways = [0] * n
        ways[0] = k
        ways[1] = (k - 1) * ways[0] + k
        for i in range(2, n):
            ways[i] = (k - 1) * (ways[i - 1] + ways[i - 2])
        return ways[n - 1]

print(Solution().numWays(5, 3)) # 180
