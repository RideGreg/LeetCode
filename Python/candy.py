# Time:  O(n)
# Space: O(n)
# 135
# There are N children standing in a line. Each child is assigned a rating value.
#
# You are giving candies to these children subjected to the following requirements:
#
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# What is the minimum candies you must give?
#

class Solution(object):
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        N = len(ratings)
        ans = [1] * N
        for i in range(1, N):
            if ratings[i] > ratings[i-1]:
                ans[i] = ans[i-1] + 1
        for i in range(N-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                ans[i] = max(ans[i], ans[i+1] + 1)
        return sum(ans)


if __name__ == "__main__":
    print(Solution().candy([1, 2, 3, 2, 3, 5, 2, 5])) #15 = sum([1,2,3,1,2,3,1,2]

