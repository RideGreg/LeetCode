class Solution(object):
    def findLength(self, A, B):
        res = 0
        dp = [[0] * (len(B)+1) for _ in xrange(len(A)+1)] 
# if use this initialization, every row copies each other
#        dp = [[0] * (len(B)+1)] * (len(A)+1)
        print dp
        for i in xrange(1, len(A)+1):
            for j in xrange(1, len(B)+1):
#                print i, j
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    res = max(res, dp[i][j])
            print dp
        return res

    def findLength_awice(self, A, B):
        memo = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        for i in range(len(A) - 1, -1, -1):
            for j in range(len(B) - 1, -1, -1):
                if A[i] == B[j]:
                    memo[i][j] = memo[i+1][j+1]+1
        return max(max(row) for row in memo)

print Solution().findLength([1,2,3,2,1], [5,3,2,1,4])
