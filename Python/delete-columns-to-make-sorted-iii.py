# Time:  O(n * l^2), n is the length of A, l is the length of each word in A.
# Space: O(l)

# 960
# We are given an array A of N lowercase letter strings, all of the same length.
#
# Now, we may choose any set of deletion indices, and for each string, we delete all the characters in those indices.
#
# For example, if we have an array A = ["babca","bbazb"] and deletion indices {0, 1, 4}, then the final array after
# deletions is ["bc","az"].
#
# Suppose we chose a set of deletion indices D such that after deletions, the final array has every element (row)
# in lexicographic order.
#
# For clarity, A[0] is in lexicographic order (ie. A[0][0] <= A[0][1] <= ... <= A[0][A[0].length - 1]),
# A[1] is in lexicographic order (ie. A[1][0] <= A[1][1] <= ... <= A[1][A[1].length - 1]), and so on.
#
# Return the minimum possible value of D.length.

# Dynamic Programming:
# lets try to find # of columns to keep, instead of # to delete. At the end, we can subtract to find the desired answer.
#
# let's say we must keep the column j. The previous column i we keep must have all rows lexicographically sorted
# (ie. i[x] <= j[x]), and we can say that we have deleted all columns between i and j.
#
# Use dp[k] be # of columns that are kept in answering the question for input [row[:k+1] for row in A].

class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        W = len(A[0])
        dp = [1] * W
        for j in xrange(1, W):
            for i in xrange(j):
                if all(row[i] <= row[j] for row in A):
                    dp[j] = max(dp[j], dp[i]+1)
        return W - max(dp)

print(Solution().minDeletionSize(["babca","bbazb"])) # 3
print(Solution().minDeletionSize(["edcba"])) # 4
print(Solution().minDeletionSize(["ghi","def","abc"])) # 0