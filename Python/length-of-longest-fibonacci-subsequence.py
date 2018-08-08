# Time:  O(n^2*logm) n is length of A, m is largest value of A
# Space: O(n) space used by the hashSet

# A sequence X_1, X_2, ..., X_n is fibonacci-like if:
#
# n >= 3
# X_i + X_{i+1} = X_{i+2} for all i + 2 <= n
# Given a strictly increasing array A of positive integers forming a sequence,
# find the length of the longest fibonacci-like subsequence of A.
# If one does not exist, return 0.
#
# (Recall that a subsequence is derived from another sequence A by
#  deleting any number of elements (including none) from A,
#  without changing the order of the remaining elements.
#  For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].)
#
# Example 1:
#
# Input: [1,2,3,4,5,6,7,8]
# Output: 5
# Explanation:
# The longest subsequence that is fibonacci-like: [1,2,3,5,8].
# Example 2:
#
# Input: [1,3,7,11,12,14,18]
# Output: 3
# Explanation:
# The longest subsequence that is fibonacci-like:
# [1,11,12], [3,11,14] or [7,11,18].
#
# Note:
# - 3 <= A.length <= 1000
# - 1 <= A[0] < A[1] < ... < A[A.length - 1] <= 10^9
# - (The time limit has been reduced by 50% for submissions in Java, C, and C++.)

class Solution(object):
    # Brute Force with HashSet
    # Due to the exponential growth of terms in Fibonacci-like sequence, at most 43 terms in seq w/ maximum value 10^9.
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        lookup = set(A)
        result = 2
        for i in xrange(len(A)):
            for j in xrange(i+1, len(A)):
                x, y, l = A[i], A[j], 2
                while x+y in lookup:
                    x, y, l = y, x+y, l+1
                result = max(result, l)
        return result if result > 2 else 0

    # Similar to problem "Longest Increasing Subsequenc",
    # time O(N^2),
    # space O(NlogM), each item in longest may require a logM-length sequence.
    #
    # Think of two consecutive terms A[i], A[j] in a fibonacci-like sequence as a single node (i, j),
    # and the entire subsequence is a path between these consecutive nodes. E.g, with the fibonacci-like subsequence
    # (A[1] = 2, A[2] = 3, A[4] = 5, A[7] = 8, A[10] = 13), the path is from nodes (1, 2) <-> (2, 4) <-> (4, 7) <-> (7, 10).
    # The motivation for this is that two nodes (i, j) and (j, k) are connected if and only if A[i] + A[j] == A[k].
    #
    # Algorithm
    # Let longest[i,j] be the longest path ending in [i,j] (default to 2). Then longest[j,k] = longest[i,j] + 1 if (i,j) and (j,k)
    # are connected. Since i is uniquely determined as A.index(A[k] - A[j]), we can efficiently check for each j < k for potential i,
    # and update longest[j,k] accordingly.
    def lenLongestFibSubseq_dp(self, A):
        import collections
        index = {x: i for i, x in enumerate(A)}
        longest = collections.defaultdict(lambda: 2)

        ans = 0
        for k, z in enumerate(A):
            for j in xrange(k):
                i = index.get(z - A[j], None)
                if i is not None and i < j:
                    cand = longest[j, k] = longest[i, j] + 1
                    ans = max(ans, cand)

        return ans if ans >= 3 else 0