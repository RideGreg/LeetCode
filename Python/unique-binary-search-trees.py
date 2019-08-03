# Time:  O(n)
# Space: O(1)
#
# 96
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

# Math solution. Answer is a Catalan Number = C(2n, n) - C(2n, n+1) = C(2n, n)/(n+1) = (2n)! / ((n+1)! * n!)
# C(2n,n) is # of total combinations of n '(' in 2n positions, C(2n,n+1) is # of bad combinations
# that doesn't meet the condition #of '(' > #of ')' i.e. n+1 '(' and n-1 ')'.
# start from C_0: 1,1,2,5,14,42,132... Catalan Number solves many combinatorial problem,
# iff this regulation is satisfied: C_0 = 1,  and C_n = sum{C_i * C_n-1-i)} for i is 0..n-1.
# or the problem can be described as: order n pairs of (a, b), at any time cannot have more B than A.


# http://mathforum.org/advanced/robertd/catalan.html
# https://www.youtube.com/watch?v=Py6ode0LF2c (On the Catalan numbers)
# http://www-math.mit.edu/~rstan/ec/catalan.pdf

# parentheses
# 1. count # of expressions containing n pairs of correctly matched parentheses.
# CORE THINKING: at any time cannot have more ) than (.
# n pairs can be arranged as: ( i pairs ) n-1-i pairs
# e.g. 3 pairs parentheses => 5 expressions
# ()()()   ()(()) (())()  (()())  ((()))
# 2. parenthesizing of a product of k+1 factors:
# e.g. insert 3 pairs of parentheses between product of 4 numbers:
# (1 (2 (3 4)))   (1 ((2 3) 4)) ((1 2) (3 4))   ((1 (2 3)) 4)   (((1 2) 3) 4)

# tree
# 3. count # of FULL binary trees with n+1 leaves (or 2n+1 nodes, FULL means each node has 2 or 0 children)
# e.g. 4 leaves full binary tree can be arranged as: 1 leave left subtree + 3 leaves right subtree (2)
# + 2 leaves left subtree + 2 leaves right subtree (1) + 3 leaves left subtree + 1 leave right subtree (2)
# or see problem 1: 4 leaves (1,2,3,4) => n=3 => C_3=5 ways to construct a binary tree

# 4. count # of Binary Search Trees with n keys (consider left/right subtree)

# geometry
# 5. Triangulation problem: count # of ways to cut n+2 side polygon into n triangles
# 6. handshake problem: C_n: # of ways that 2n people in a circle can pair off to shake hands, with no crossing hands.
# assume people 0 pair with people 2i+1, then left side has 2i people, right side has 2(n-1-i) people.

# path in grid
# 7. count # of paths of length 2n through (n+1)x(n+1) grid that do not rise above main diagonal,
#    or # of shortest rook paths across a (n+1)x(n+1) triangular chessboard.
# CORE THINKING: at any time cannot have more north steps than east steps. Similar to problem 1.
# https://www.youtube.com/watch?v=GlI17WaMrtw  explains why it is C(2n,n)-C(2n,n+1)


class Solution(object):   # USE THIS
    def numTrees(self, n):
        import functools, operator
        fact = lambda x,y: functools.reduce(operator.mul, range(x,y+1), 1)
        return fact(n+1,2*n) // fact(1,n+1)


class Solution3(object):   # calculate C(2n, n) - C(2n, n+1)
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        import functools
        if n == 0:
            return 1

        def combination(n, k):
            import operator
            fact = lambda x,y: functools.reduce(operator.mul, range(x, y+1), 1)
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
        for i in range(1, n+1):
            dp[i] = sum(dp[j]*dp[i-1-j] for j in range(i))
        return dp[n]


if __name__ == "__main__":
    print(Solution().numTrees(3))
