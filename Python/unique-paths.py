# Time:  O(m * n)
# Space: O(m + n)
#
# 62
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#
# The robot can only move either down or right at any point in time.
# The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
#
# How many possible unique paths are there?
#
# Note: m and n will be at most 100.
#

class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        if m < n:
            return self.uniquePaths(n, m)
        ways = [1] * n

        for _ in range(1, m):
            for j in range(1, n):
                ways[j] += ways[j - 1]

        return ways[n - 1]

    # math: Time O(min(m,n)) Space O(1).
    # combination: total m+n-2 steps, pick n-1 steps as going right. C(m+n-2, n-1) = (m+n-2)!/((n-1)!*(m-1)!)
    def uniquePaths_combination(self, m, n): # USE THIS
        import operator, functools
        if m < n:
            m, n = n, m

        # THIS IS how to do factorial
        # initializer 1 is needed for empty list (m=2,n=1)
        fact = lambda x,y: functools.reduce(operator.mul, range(x,y+1), 1)
        return fact(m, m+n-2) // fact(1, n-1)

if __name__ == "__main__":
    print(Solution().uniquePaths(1, 2))
