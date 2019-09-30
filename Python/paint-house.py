# Time:  O(n)
# Space: O(1)

# 256
# There are a row of n houses, each house can be painted with one of the three colors: red, blue or green.
# The cost of painting each house with a certain color is different. You have to paint all the houses
# such that no two adjacent houses have the same color.
#
# The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example,
# costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is the cost of
# painting house 1 with color green, and so on... Find the minimum cost to paint all houses.

class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        ans = [0] * 3
        for c in costs:
            ans = [c[0] + min(ans[1], ans[2]),
                   c[1] + min(ans[2], ans[0]),
                   c[2] + min(ans[0], ans[1])]
        return min(ans)


# Time:  O(n)
# Space: O(n)
class Solution2(object): # modified input list
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0

        n = len(costs)
        for i in range(1, n):
            costs[i][0] += min(costs[i - 1][1], costs[i - 1][2])
            costs[i][1] += min(costs[i - 1][0], costs[i - 1][2])
            costs[i][2] += min(costs[i - 1][0], costs[i - 1][1])

        return min(costs[n - 1])

print(Solution().minCost([[14,2,11],[11,14,5],[14,3,10]])) # 10 = blue 2 + green 5 + blue 3
print(Solution().minCost([[1,2,3],[1,4,6]])) # 3
