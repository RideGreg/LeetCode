# Time:  O(klogn)
# Space: O(1)

# 887
# You are given K eggs, and you have access to a building
# with N floors from 1 to N. 
#
# Each egg is identical in function,
# and if an egg breaks, you cannot drop it again.
#
# You know that there exists a floor F with 0 <= F <= N
# such that any egg dropped at a floor higher than F will break,
# and any egg dropped at or below floor F will not break.
#
# Each move, you may take an egg (if you have an unbroken one)
# and drop it from any floor X (with 1 <= X <= N). 
#
# Your goal is to know with certainty what the value of F is.
#
# What is the minimum number of moves that you need to know with
# certainty what F is, regardless of the initial value of F?
#
# Example 1:
#
# Input: K = 1, N = 2
# Output: 2
# Explanation: 
# Drop the egg from floor 1.  If it breaks, we know with certainty that F = 0.
# Otherwise, drop the egg from floor 2.
# If it breaks, we know with certainty that F = 1.
# If it didn't break, then we know with certainty F = 2.
# Hence, we needed 2 moves in the worst case to know what F is with certainty.
# Example 2:
#
# Input: K = 2, N = 6
# Output: 3
# Example 3:
#
# Input: K = 3, N = 14
# Output: 4
#
# Note:
# - 1 <= K <= 100
# - 1 <= N <= 10000

class Solution(object):
    # ask the question in reverse: given T moves (and K eggs), what is the most # of floors f(T,K)
    # that we can still "solve" (find 0<=F<=f(T,K) with certainty)? Then, the problem is to find the least T
    # for which f(T,K)>=N. Because more tries is always at least as good, f is increasing on T, which means we
    # could binary search for the answer.
    #
    # Now, we find the recurrence for f. If in an optimal strategy we drop the egg from floor X_0,
    # then either it breaks and we can solve f(T-1,K-1) lower floors (floors < X_0); or it doesn't break
    # and we can solve f(T-1,K) higher floors (floors >= X_0). In total,
    # f(T,K)=f(T-1,K-1) + (1+f(T-1,K)) where 1 is floor 0 added to floors >=X_0

    # Also, it is easily seen that f(t,1)=t when t >= 1, and f(1,k)=1 when k >= 1.
    # We can solve by binomial recurrence that f(t,k) = sum(xCt), where 1<=x<=k
    # Detail see https://leetcode.com/problems/super-egg-drop/solution/

    # Alternatively, when we have t tries and K eggs, the result of our t throws must be a t-length sequence of
    # successful and failed throws, with at most K failed throws. The # of sequences with 0 failed throws is
    # 0Ct, the # of sequences with 1 failed throw is 1Ct etc.
    # so that the number of such sequences is 0Ct + 1Ct + ... + kCt.

    # Upperbound: we can only distinguish at most these many floors in t tries (as each sequence only map to
    # 1 answer per sequence.) This process includes distinguishing F=0, so that the corresponding value of N
    #  is one less than this sum (in implementation we don't count 0Ct).
    #
    # Lower bound for the number of floors that can be distinguished: as the result
    # of a throw on floor X will bound the answer to be either <=X or >X.
    # Hence, in an optimal throwing strategy, each such sequence actually maps to a unique answer.

    # In other words: each combination of x moves with k broken eggs could represent a unique f(x).
    # Thus, the range size of f(x) that all combinations can cover is the sum of C(x, k), k = 1..K

    def superEggDrop(self, K, N): # USE THIS
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        def check(n):
            # Each combination of n moves with k broken eggs could represent a unique F.
            # Thus, the range size of F that all cominations can cover is the sum of C(n, k), k = 1..K
            # start from 1Cx = x, then 2Cx = x(x-1)/2, ... to kCx = x(x-1)..(x-k+1)/k!
            # 0Cx = 1 is not considered because floor 0 is not included f(x) (max # of floors can distinguished)

            # let f(n, K) be the max number of floors could be solved by n moves and K eggs,
            # we want to do binary search to find min of n, s.t. f(n, K) >= N,
            # if we use one move to drop egg with X floors
            # 1. if it breaks, we can search new X in the range [X+1, X+f(n-1, K-1)]
            # 2. if it doesn't break, we can search new X in the range [X-f(n-1, K), X-1]
            # => f(n, K) = (X+f(n-1, K-1))-(X-f(n-1, K))+1 = f(n-1, K-1)+f(n-1, K)+1
            # => (1) f(n, K)   = f(n-1, K)  +1+f(n-1, K-1)
            #    (2) f(n, K-1) = f(n-1, K-1)+1+f(n-1, K-2)
            # let g(n, K) = f(n, K)-f(n, K-1), and we substract (1) by (2)
            # => g(n, K) = g(n-1, K)+g(n-1, K-1), obviously, it is binomial coefficient
            # => C(n, K) = g(n, K) = f(n, K)-f(n, K-1),
            #    which also implies if we have one more egg with n moves and x-1 egges, we can have more C(n, x) floors solvable
            # => f(n, K) = C(n, K)+f(n, K-1) = C(n, K) + C(n, K-1) + ... + C(n, 1) + f(n, 0) = sum(C(n, k) for k in [1, K])
            # => all we have to do is to check sum(C(n, k) for k in [1, K]) >= N,
            #    if true, there must exist a 1-to-1 mapping from each F in [1, N] to each sucess and failure sequence of every C(n, k) combinations for k in [1, K]
            total, c = 0, 1
            for k in range(1, K+1):
                c *= n-k+1
                c //= k
                total += c
                if total >= N:
                    return True
            return False

        lo, hi = 1, N
        while lo < hi:
            mi = (lo + hi) // 2
            if not check(mi): # mi move is invalid, discard anything <= mi
                lo = mi + 1
            else:             # mi is valid, discard anything > mi
                hi = mi
        return lo


    # 1D dynamic programming not working. Assume dp[i] is how many floors above floor 0 left to check.
    # dp[1] = 1: when N=1 (floor 0,1), we need 1 move (drop egg from f1: break->F=0, not break->F=1).
    # For dp[3]: N=3 (floor 0,1,2,3), our 1st move is to drop egg from f1: break->F=0, not break->more
    # moves needed; but we cannot use dp[1] (i.e. 1 more move needed), we have to drop eggs from both f2
    # and f3 thus totally 3 moves are needed.

    # 2D dp O(KN^2). dp(k, n): k eggs and n floors (above floor 0) left.
    # TLE for K=4, N=10000
    # Dynamic programming, as we encounter similar subproblems. Our state is (K, N): K eggs and N floors left.
    # When we drop an egg from floor X, it either survives and we have state (K, N-X), or it breaks
    # and we have state (K-1, X-1).
    #
    # dp(K,N)= min( max(dp(K,N-X),dp(K-1,X-1)) )
    #         1<=X<=N
    #
    # This approach would lead to a O(K N^2) algorithm, not efficient enough for the given constraints.
    # However, we can try to speed it up.
    def superEggDrop_2Ddp_myBisect_memo(self, K, N): # O(KNlogN) can USE THIS
        def dp(k, n):
            if (k, n) not in memo:
                if n <= 1:
                    ans = n
                elif k == 1:
                    ans = n
                else:
                    # find maximal x in [1, n] where t1 < t2
                    lo, hi = 1, n
                    while lo < hi:
                        x = (lo + hi + 1) // 2
                        t1 = dp(k-1, x-1)
                        t2 = dp(k, n-x)
                        if t1 < t2:
                            lo = x
                        else:
                            hi = x - 1
                    ans = 1 + min(max(dp(k-1, x-1), dp(k, n-x))
                                  for x in (lo, lo + 1))

                memo[k, n] = ans
            return memo[k, n]

        memo = {}
        return dp(K, N)

    def superEggDrop_2Ddp_myBisect_lrucache(self, K, N): # USE THIS ok too
        from functools import lru_cache
        @lru_cache(None)
        def dp(k, n):
            if n <= 1:
                ans = n
            elif k == 1:
                ans = n
            else:
                lo, hi = 1, n
                # keep a gap of 2 X values to manually check later
                while lo < hi:
                    x = (lo + hi + 1) // 2
                    t1 = dp(k-1, x-1)
                    t2 = dp(k, n-x)

                    if t1 < t2:
                        lo = x
                    else:
                        hi = x - 1

                ans = 1 + min(max(dp(k-1, x-1), dp(k, n-x))
                              for x in (lo, lo + 1))

            return ans

        return dp(K, N)



    def superEggDrop_2Ddp(self, K, N): # TLE O(KN^2)
        dp = [[float('inf')]*(N+1) for _ in xrange(K+1)]
        for i in xrange(K+1):
            dp[i][0] = 0
        for j in xrange(1, N+1):
            dp[1][j] = j

        for i in xrange(2, K+1):
            for j in xrange(1, N+1):
                # if j floors left, try drop egg from 1 to j floor and choose the smallest
                # when drop egg from floor k, if not break then dp[i][j-k], if break then dp[i-1][k-1]
                dp[i][j] = 1 + min(max(dp[i][j-k], dp[i-1][k-1]) for k in xrange(1, j+1))
        return dp[K][N]

    # optimized to as dp[i][j-k] decrease with k, dp[i-1][k-1] increase with k, best k is the crossing
    # point of these 2 subproblem. We don't need to check every k, use bisect to find optimal k.
    def superEggDrop_2Ddp_bisect(self, K, N): # O(KNlogN) 4000ms
        dp = [[float('inf')]*(N+1) for _ in xrange(K+1)]
        for i in xrange(K+1):
            dp[i][0] = 0
        for j in xrange(1, N+1):
            dp[1][j] = j

        for i in xrange(2, K+1):
            for j in xrange(1, N+1):
                lo, hi = 1, j
                while lo +1 < hi:
                    k = (lo+hi)/2
                    t1, t2 = dp[i-1][k-1], dp[i][j-k]
                    if t1 < t2:
                        lo = k
                    elif t1 > t2:
                        hi = k
                    else:
                        lo = hi = k
                dp[i][j] = 1 + min(max(dp[i][j-k], dp[i-1][k-1]) for k in (lo, hi))
        return dp[K][N]

    def superEggDrop_2Ddp_bisect_memo_leetcodeBisect(self, K, N):  # O(KNlogN) 800ms, not calculate every dp[i][j]
        def dp(k, n):
            if (k, n) not in memo:
                if n == 0:
                    ans = 0
                elif k == 1: # 1 egg can solve n floors in n move, just try by bottom up
                    ans = n
                else:
                    lo, hi = 1, n
                    # keep a gap of 2 X values to manually check later
                    while lo + 1 < hi:
                        x = (lo + hi) / 2
                        t1, t2 = dp(k-1, x-1), dp(k, n-x)

                        if t1 < t2:
                            lo = x
                        elif t1 > t2:
                            hi = x
                        else:
                            lo = hi = x
                    ans = 1 + min(max(dp(k-1, x-1), dp(k, n-x)) for x in (lo, hi))
                memo[k, n] = ans
            return memo[k, n]

        memo = {}
        return dp(K, N)

    def superEggDrop_wrong(self, K: int, N: int) -> int:
        # WRONG: blindly use middle point as optimal
        def dp(n, k):
            if n == 1 and k > 0:
                return 1
            elif n <= 3 and k > 0:
                return 2
            return 1 + max(dp((n-1)//2, k-1), dp((n+1)//2, k))
        return dp(N, K)

print(Solution().superEggDrop(1,2)) # 2
print(Solution().superEggDrop(2,6)) # 3
print(Solution().superEggDrop(3,14)) # 4

