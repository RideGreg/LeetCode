# Time:  O(n^3)
# Space: O(n^2)

# 1246 biweekly contest 12 11/2/2019
# Given an integer array arr, in one move you can select a palindromic subarray arr[i], arr[i+1], ..., arr[j]
# where i <= j, and remove that subarray from the given array. Note that after removing a subarray, the elements
# on the left and on the right of that subarray move to fill the gap left by the removal.
#
# Return the minimum number of moves needed to remove all numbers from the array.

# Constraints:
# 1 <= arr.length <= 100
# 1 <= arr[i] <= 20

class Solution(object):
    # USE THIS, clear to understand
    # check every bisect (although some are unnecessary, don't increase overall time)
    def minimumMoves(self, arr):
        N = len(arr)
        dp = [[(1 if i == j else N) for i in range(N)] for j in range(N)]

        for sz in range(2, N+1):
            for i in range(N-sz+1):
                j = i+sz-1
                if sz == 2:
                    dp[i][j] = 1 if arr[i] == arr[j] else 2
                else:
                    dp[i][j] = min(dp[i][k]+dp[k+1][j] for k in range(i, j))
                    if arr[i] == arr[j]:
                        dp[i][j] = min(dp[i][j], dp[i+1][j-1])
        return dp[0][-1]


    def minimumMoves_kamyu(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        N = len(arr)
        dp = [[(1 if i == j else 0) for i in range(N)] for j in range(N)]
        for sz in range(2, N+1):
            for i in range(N-sz+1):
                j = i+sz-1
                if sz == 2:
                    dp[i][j] = 1 if arr[i] == arr[j] else 2
                else:
                    dp[i][j] = 1+dp[i+1][j]
                    # compare i-1, i+2..j-1, j
                    if arr[i] == arr[i+1]:
                        dp[i][j] = min(dp[i][j], 1 + dp[i+2][j])
                    for k in range(i+2, j):
                        if arr[i] == arr[k]:
                            dp[i][j] = min(dp[i][j], dp[i+1][k-1] + dp[k+1][j])
                    if arr[i] == arr[j]:
                        dp[i][j] = min(dp[i][j], dp[i+1][j-1])
        return dp[0][len(arr)-1]


print(Solution().minimumMoves([1,3,4,1,5])) #3
print(Solution().minimumMoves([1,3])) # 2
print(Solution().minimumMoves([1,3,1])) # 1
print(Solution().minimumMoves([19,14,6,5,16,4,16,3,10,7])) # 8

a = [17,6,5,18,17,4,18,8,16,8,12,1,5,14,14,6,17,18,2,19,11,15,8,18,7,8,20,2,10,3,18,17,18,18,8,9,20,3,16,19,6,9,8,8,16,19,13,8,5,20]
print(Solution().minimumMoves(a)) # 25 not 32
a = [14,17,7,9,20,7,15,10,10,12,1,9,4,17,18,7,9,13,20,19,20,20,9,5,2,4,12,19,3,11,7,1,14,12,3,11,13,7,9,11,3,1,10,4,20,11,13,20,10,9,8,20,3,9,13,2,13,11,1,9,13,19,20,16,9,2,13,9,7,17,8,5,13,6,15,11,10,9,15,1]
print(Solution().minimumMoves(a)) # 42 not 48
