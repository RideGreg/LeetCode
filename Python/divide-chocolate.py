# Time:  O(nlogn)
# Space: O(1)

# 1231 biweekly contest 11 10/19/2019
# You have one chocolate bar that consists of some chunks. Each chunk has its own sweetness given by the array sweetness.
#
# You want to share the chocolate with your K friends so you start cutting the chocolate bar into K+1 pieces using
# K cuts, each piece consists of some consecutive chunks.
#
# Being generous, you will eat the piece with the minimum total sweetness and give the other pieces to your friends.
# Find the maximum total sweetness of the piece you can get by cutting the chocolate bar optimally.
#
# Constraints:
# 0 <= K < sweetness.length <= 10^4
# 1 <= sweetness[i] <= 10^5

class Solution(object):
    def maximizeSweetness(self, sweetness, K):
        """
        :type sweetness: List[int]
        :type K: int
        :rtype: int
        """
        def check(K, x):
            curr, cuts = 0, 0
            for s in sweetness:
                curr += s
                if curr >= x:
                    curr = 0
                    cuts += 1
                    if cuts >= K+1: return True
            return False

        l, r = min(sweetness), sum(sweetness) // (K+1)
        while l < r:
            m = (l+r+1) // 2
            if check(K, m):
                l = m
            else:
                r = m - 1
        return l

    # O(n^2)
    def maximizeSweetness_dp(self, sweetness, K):
        sz = len(sweetness)
        sums = [0]
        for s in sweetness:
            sums.append(sums[-1]+s)

        dp = [[[None] * (K+1) for _ in range(sz)] for _ in range(sz)]

        def dfs(i, j, k):
            if k == 0:
                dp[i][j][k] = sums[j+1]-sums[i]
            elif k == j-i:
                dp[i][j][k] = min(sweetness[i:j+1])
            else:
                if dp[i][j][k] == None:
                    dp[i][j][k] = float('-inf')
                    for m in range(i, j-k+1):
                        dp[i][j][k] = max(dp[i][j][k],
                                          min(dfs(i,m,0), dfs(m+1,j,k-1)))

            return dp[i][j][k]

        return dfs(0, sz-1, K)

print(Solution().maximizeSweetness([1,2,3,4,5,6,7,8,9], 5)) # 6
print(Solution().maximizeSweetness([5,6,7,8,9,1,2,3,4], 8)) # 1
print(Solution().maximizeSweetness([1,2,2,1,2,2,1,2,2], 2)) # 5
print(Solution().maximizeSweetness([1,2,3,4,5,6,7,8,9], 0)) # 45
print(Solution().maximizeSweetness([1,2,2,1,2,2,1,2,2], 0)) # 15