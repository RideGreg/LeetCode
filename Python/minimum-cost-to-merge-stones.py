
# Time:  O(n^3 / k)
# Space: O(n^2)

# 1000
# There are N piles of stones arranged in a row.  The i-th pile has stones[i] stones.
#
# A move consists of merging exactly K consecutive piles into one pile, and the cost of this move is equal to
# the total number of stones in these K piles.
#
# Find the minimum cost to merge all piles of stones into one pile.  If it is impossible, return -1.

# top-down dp + memoization

class Solution(object):
    # Seem that most of games, especially stone games, are solved by dp?
    # 2D dp
    # dp[i][j] means the minimum cost needed to merge stones[i] ~ stones[j].
    #
    # stones[i] ~ stones[j] will merge as much as possible.
    #
    # Finally (j - i) % (K - 1) + 1 piles will be left.
    # It's less than K piles and no more merger happens.
    #
    # Complexity Time O(N^3/K) Space O(N^2)
    def mergeStones(self, stones, K): # USE THIS
        """
        :type stones: List[int]
        :type K: int
        :rtype: int
        """
        n = len(stones)
        if (n - 1) % (K - 1): return -1
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        import functools
        @functools.lru_cache(None)
        def dp(i, j):
            if j - i + 1 < K: return 0

            # divide into 2 groups, each group has >= 1 stone, merge separately
            # each time reduce # of stones by K-1
            res = min(dp(i, mid) + dp(mid + 1, j) for mid in range(i, j, K - 1))

            # e.g. K = 5, and # of stones: 5, or 9, or 13 ...
            if (j - i) % (K - 1) == 0:
                res += prefix[j + 1] - prefix[i]
            return res

        return dp(0, n - 1)


    # dp[i][j][m] means the cost needed to merge stone[i] ~ stones[j] into m piles.
    #
    # Initial status dp[i][i][1] = 0 and dp[i][i][m] = infinity
    #
    # dp[i][j][1] = dp[i][j][k] + stonesNumber[i][j]
    # dp[i][j][m] = min(dp[i][mid][1] + dp[mid + 1][j][m - 1])
    #
    # Q: Why mid jump at step K - 1
    # A: We can merge K piles into one pile,
    # we can't merge K+1, K+2 ... K+(K-2) piles into one pile.
    # We can merge K + (K - 1) piles into on pile,
    # We can merge K + (K - 1) * n piles into one pile. So the step is K - 1.
    #
    # The origine python2 solution is a bit too long on the memorization part.
    # So I rewrote it in python3 with cache helper, so it will be clear for logic.
    # http://book.pythontips.com/en/latest/function_caching.html
    def mergeStones_3Ddp_python3(self, stones, K): # 3D dp, python 3
        n = len(stones)
        if (n-1) % (K-1): return -1
        inf = float('inf')
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        import functools
        @functools.lru_cache(None)
        def dp(i, j, m):
            if (j - i + 1 - m) % (K - 1):
                return inf
            if i == j:
                return 0 if m == 1 else inf
            if m == 1:
                return dp(i, j, K) + prefix[j + 1] - prefix[i]
            return min(dp(i, mid, 1) + dp(mid + 1, j, m - 1) for mid in range(i, j, K - 1))
        res = dp(0, n - 1, 1)
        return res if res < inf else -1

    def mergeStones_3Ddp_python2(self, stones, K): # custom function caching
        def dp(K, i, j, k):
            if (i, j, k) in lookup:
                return lookup[i, j, k]
            if i == j:
                result = 0 if k == 1 else float("inf")
            else:
                if k == 1:
                    result = dp(K, i, j, K) + \
                             prefix[j+1] - prefix[i]
                else:
                    result = float("inf")
                    for mid in range(i, j, K-1):
                        result = min(result, dp(K, i, mid, 1) +
                                             dp(K, mid+1, j, k-1))
            lookup[i, j, k] = result
            return result
        
        result = dp(K, 0, len(stones)-1, 1)
        return result if result != float("inf") else -1


    def mergeStones_dfs_LTE(self, stones, K): # TLE for cost=[69,39,79,78,16,6,36,97,79,27,14,31,4], K=2
        def dfs(todo, cost, K):
            if len(todo) == 1:
                self.ans = min(self.ans, cost)

            if len(todo) < K: return

            for i in range(len(todo)-K+1):
                s = sum(todo[i:i+K])
                dfs(todo[:i]+[s]+todo[i+K:], cost+s, K)

        self.ans = float('inf')
        dfs(stones, 0, K)
        return -1 if self.ans == float('inf') else self.ans

    def mergeStones_dfs_wrong(self, stones, K): # wrong for cost=[6,4,4,6], K=2. Expect 40
        def dfs(todo, cost, K):
            if len(todo) == 1:
                self.ans = min(self.ans, cost)

            if len(todo) < K: return

            min_i, s = 0, sum(todo[:K])
            for i in range(1, len(todo)-K+1):
                if sum(todo[i:i+K]) < s:
                    s = sum(todo[i:i+K])
                    min_i = i
            dfs(todo[:min_i]+[s]+todo[min_i+K:], cost+s, K)

        self.ans = float('inf')
        dfs(stones, 0, K)
        return -1 if self.ans == float('inf') else self.ans


    def mergeStones_kamyu(self, stones, K):
        if (len(stones)-1) % (K-1):
            return -1
        prefix = [0]
        for x in stones:
            prefix.append(prefix[-1]+x)
        dp = [[0]*len(stones) for _ in xrange(len(stones))]
        for l in xrange(K-1, len(stones)):
            for i in xrange(len(stones)-l):
                dp[i][i+l] = min(dp[i][j]+dp[j+1][i+l] for j in xrange(i, i+l, K-1))
                if l % (K-1) == 0:
                    dp[i][i+l] += prefix[i+l+1] - prefix[i]
        return dp[0][len(stones)-1]


print(Solution().mergeStones([3,2,4,1], 2)) # 20. [3,2,4,1] -> [5,4,1] -> [5,5] -> [10]
print(Solution().mergeStones([3,2,4,1], 3)) # -1
print(Solution().mergeStones([3,5,1,2,6], 3)) # 25. [3,5,1,2,6] -> [3,8,6] -> [17]
print(Solution().mergeStones([69,39,79,78,16,6,36,97,79,27,14,31,4], 2)) # 1957
