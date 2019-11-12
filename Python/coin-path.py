# Time:  O(n * B)
# Space: O(n)

# 656
# Given an array A (index starts at 1) consisting of N integers: A1, A2, ..., AN and an integer B.
# The integer B denotes that from any place (suppose the index is i) in the array A, you can jump
# to any one of the place in the array A indexed i+1, i+2, …, i+B if this place can be jumped to.
# Also, if you step on the index i, you have to pay Ai coins. If Ai is -1, it means you can’t
# jump to the place indexed i in the array.
#
# Now, you start from the place indexed 1 in the array A, and your aim is to reach the place
# indexed N using the minimum coins. You need to return the path of indexes (starting from 1 to N)
# in the array you should take to get to the place indexed N using minimum coins.
#
# If there are multiple paths with the same cost, return the lexicographically smallest such path.
#
# If it's not possible to reach the place indexed N then you need to return an empty array.


class Solution(object):
    # 不一定需要存whole path，考虑存prev_pos来优化空间
    #
    # DP: bookshadow
    # 数组cost[i]表示以第i枚硬币结尾时的最小开销。
    # 数组path[i]表示以第i枚硬币时的最佳选择方案。
    #
    # 若cost[i] > cost[j] + A[i] 或者 cost[i] == cost[j] + A[i] && path[i] > path[j] + [i]
    # 则令cost[i] = cost[j] + A[i], path[i] = path[j] + [i]
    def cheapestJump(self, A, B):
        """
        :type A: List[int]
        :type B: int
        :rtype: List[int]
        """
        N = len(A)
        cost = [0x7FFFFFFF] * (N + 1)
        cost[1] = A[0]
        path = [[] for _ in range(N + 1)]
        path[1] = [1]

        for x in range(2, N + 1):
            if A[x - 1] == -1: continue
            for y in range(1, B + 1):
                z = x - y
                if z < 1: break
                if A[z - 1] == -1: continue
                if cost[x] > cost[z] + A[x - 1] or \
                    cost[x] == cost[z] + A[x - 1] and path[x] > path[z] + [x]:
                    cost[x] = cost[z] + A[x - 1]
                    path[x] = path[z] + [x]
        return path[-1]

    def cheapestJump_kamyu(self, A, B):
        result = []
        if not A or A[-1] == -1:
            return result
        n = len(A)
        dp, next_pos = [float("inf")] * n, [-1] * n
        dp[n-1] = A[n-1]
        for i in reversed(range(n-1)):
            if A[i] == -1:
                continue
            for j in range(i+1, min(i+B+1,n)):
                # cost相等但path has better lexicographical order已经考虑到了，因为每个next_pos都是最小
                if A[i] + dp[j] < dp[i]:
                    dp[i] = A[i] + dp[j]
                    next_pos[i] = j
        if dp[0] == float("inf"):
            return result
        k = 0
        while k != -1:
            result.append(k+1)
            k = next_pos[k]
        return result

print(Solution().cheapestJump([1,2,4,-1,2], 2)) # [1,3,5]
print(Solution().cheapestJump([1,2,4,-1,2], 1)) # []
