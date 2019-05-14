# Time:  O(m * n)
# Space: O(min(m, n))

# 1035
# We write the integers of A and B (in the order they are given) on two separate
# horizontal lines.
#
# Now, we may draw a straight line connecting two numbers A[i] and B[j] as long as A[i] == B[j],
# and the line we draw does not intersect any other connecting (non-horizontal) line.
#
# Return the maximum number of connecting lines we can draw in this way.

# Input: A = [1,4,2], B = [1,2,4]
# Output: 2
# Explanation: We can draw 2 uncrossed lines as in the diagram.
# We cannot draw 3 uncrossed lines, because the line from A[1]=4 to B[2]=4 will intersect
# the line from A[2]=2 to B[1]=2.

# Input: A = [2,5,1,2,5], B = [10,5,2,1,5,2]
# Output: 3
#
# Input: A = [1,3,7,1,7,5], B = [1,9,2,5,1]
# Output: 2

# same as Longest Common Subsequence

class Solution(object):
    def maxUncrossedLines(self, A, B): # USE THIS: clearer to understand
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        if len(A) < len(B):
            A, B = B, A
        m, n = len(A), len(B)
        dp = [[0]*(n+1) for _ in range(2)]
        for i in range(1,m+1):
            for j in range(1, n+1):
                if A[i-1] == B[j-1]:
                    dp[i%2][j] = dp[(i-1)%2][j-1] + 1
                else:
                    dp[i%2][j] = max(dp[(i-1)%2][j], dp[i%2][j-1])
        return dp[i%2][-1]


    def maxUncrossedLines_1Ddp(self, A, B):
        if len(A) < len(B):
            A, B = B, A
        m, n = len(A), len(B)
        dp = [0]*(n+1)
        for i in range(1,m+1):
            # E.g. A=[1], B=[1,2,4,1]
            # ending chars match, adding a new pair becomes long subseq, do REVERSE scan.
            for j in reversed(range(1, n+1)):
                if A[i-1] == B[j-1]:
                    dp[j] = dp[j-1] + 1
            # ending chars not match, max of (0..i-1 vs 0..j) and (0..i vs 0..j-1), do FORWARD scan.
            for j in range(1, n+1):
                if A[i-1] != B[j-1]:
                    dp[j] = max(dp[j], dp[j-1])
        return dp[-1]
