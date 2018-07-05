# Time:  O(n)
# Space: O(1)
#
# Given n, how many structurally unique BST's (binary search trees) that store values 1...n?
#
# For example,
# Given n = 3, there are a total of 5 unique BST's.
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
#

# Math solution. Answer is a Catalan Number = C(2n, n) - C(2n, n+1) or C(2n, n)/(n+1) or (2n)! / ((n+1)! * n!)
# Catalan Number also counts # of expressions containing n pairs of correctly matched parentheses.
# https://en.wikipedia.org/wiki/Catalan_number
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1

        def combination(n, k):
            import operator
            fact = lambda x,y: reduce(operator.mul, xrange(x, y+1), 1)
            return fact(n-k+1, n) / fact(1, k)

            '''
            count = 1
            # C(n, k) = (n) / 1 * (n - 1) / 2 ... * (n - k + 1) / k
            for i in xrange(1, k + 1):
                count = count * (n - i + 1) / i;
            return count
            '''

        return combination(2 * n, n) - combination(2 * n, n - 1)

# Time:  O(n^2)
# Space: O(n)
# DP solution.
class Solution2:
    # @return an integer
    def numTrees(self, n):
        dp = [1] * (n+1)
        for i in xrange(1, n+1):
            dp[i] = sum(dp[j]*dp[i-1-j] for j in xrange(i))
        return dp[n]

        '''
        counts = [1, 1]
        for i in xrange(2, n + 1):
            count = 0
            for j in xrange(i):
                count += counts[j] * counts[i - j - 1]
            counts.append(count)
        return counts[-1]
        '''

if __name__ == "__main__":
    print Solution().numTrees(3)
