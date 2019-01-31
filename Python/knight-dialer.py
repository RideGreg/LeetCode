# Time:  O(logn)
# Space: O(1)

# 935
# A chess knight can move to 8 positions. Suppose we place our chess knight on any numbered key of a phone pad,
# and the knight makes N-1 hops.  Each hop must be from one key to another numbered key.
#
# Each time it lands on a key (including the initial placement of the knight), it presses the number of that key,
# pressing N digits total. How many distinct numbers can you dial in this manner?
#
# Since the answer may be large, output the answer modulo 10^9 + 7.
# 1 <= N <= 5000


import itertools

# Optimised to O(log) time instead of recursively doing pow operation.
#
# Construct a 10 * 10 transformation matrix M.
# M[i][j] = 1 if i and j is connected (knight can hop from i to j).
#
# if N = 1, return 10.
# if N > 1, return sum of [1,1,1,1,1,1,1,1,1,1] * M ^ (N - 1)
#
# The power of matrix reveals the number of walks in an undirected graph.
# https://math.stackexchange.com/questions/1890620/finding-path-lengths-by-the-power-of-adjacency-matrix-of-an-undirected-graph

# If A is the adjacency matrix of a graph, then ij'th entry of A^k will give the # of k-length paths (can use a node
# repeatedly) connecting the vertices i and j. E.g. the following matrix is A*A which shows the connectivity after 2 moves.
#             [[2, 1, 0, 1, 0, 0, 0, 1, 0, 1],
#              [1, 2, 0, 1, 0, 0, 0, 1, 0, 0],
#              [0, 0, 2, 0, 1, 0, 1, 0, 0, 0],
#              [1, 1, 0, 2, 0, 0, 0, 0, 0, 1],
#              [0, 0, 1, 0, 3, 0, 1, 0, 1, 0],
#              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#              [0, 0, 1, 0, 1, 0, 3, 0, 1, 0],
#              [1, 1, 0, 0, 0, 0, 0, 2, 0, 1],
#              [0, 0, 0, 0, 1, 0, 1, 0, 2, 0],
#              [1, 0, 0, 1, 0, 0, 0, 1, 0, 2]]

# This is like matrix multiplication. The same technique to optimize calculation of fibonacci sequence to O(logN).
# fibonacci 0 1 1 2 3 5 8 13 ... Fn = Q^(n-1)[0][0] or Q^n = [[F_n+1, F_n], [F_n, F_n-1]]
# Q-matrix [[1,1]
#           [1,0]]
# Q*Q      [[2,1]
#           [1,1]]

# O(1) formula for fibonacci number: F_n = round( ((1+5**0.5)/2)**n / 5**0.5 )
# http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fibFormula.html

class Solution(object):
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        def matrix_expo(A, K):
            result = [[int(i==j) for j in xrange(len(A))] for i in xrange(len(A))] # an identity matrix
            while K:
                if K % 2:
                    result = matrix_mult(result, A)
                A = matrix_mult(A, A)
                K /= 2   # cut in half for pow operation so O(logn)
            return result

        def matrix_mult(A, B):
            ZB = zip(*B) # cannot use izip (iterator object) which is only useful in one iteration (the first row below)
            return [[sum(a*b for a, b in itertools.izip(row, col)) % M \
                     for col in ZB] for row in A]
        
        M = 10**9 + 7
        source = [(4,6), (6,8), (7,9),(4,8),(0,3,9),(),(0,1,7),(2,6),(1,3),(2,4)]
        T = [[int(j in source[i]) for j in xrange(10)] for i in xrange(10)]
        '''
        T = [[0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
             [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
             [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
             [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [1, 1, 0, 0, 0, 0, 0, 1, 0, 0],
             [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
             [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
             [0, 0, 1, 0, 1, 0, 0, 0, 0, 0]]'''
        return sum(map(sum, matrix_expo(T, N-1))) % M


# Time:  O(n) Dynamic Programming
# Space: O(1)
class Solution2(object):
    def knightDialer(self, N):
        source = [(4,6), (6,8), (7,9),(4,8),(0,3,9),(),(0,1,7),(2,6),(1,3),(2,4)]
        dp = [[0]*10, [1]*10]
        for i in xrange(2,N+1):
            for j in xrange(10):
                dp[i%2][j] = sum(dp[(i-1)%2][k] for k in source[j])
        return sum(dp[N%2]) % (10**9+7)


    def knightDialer_kamyu(self, N):
        M = 10**9 + 7
        moves = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [],
                 [1, 7, 0], [2, 6], [1, 3], [2, 4]]

        dp = [[1 for _ in xrange(10)] for _ in xrange(2)]
        for i in xrange(2, N+1):
            dp[i % 2] = [0] * 10
            for j in xrange(10):
                for nei in moves[j]:
                    dp[i % 2][nei] += dp[(i-1) % 2][j]
                    dp[i % 2][nei] %= M
        return sum(dp[N % 2]) % M

print(Solution().knightDialer(1)) # 10
print(Solution().knightDialer(2)) # 20
print(Solution().knightDialer(3)) # 46