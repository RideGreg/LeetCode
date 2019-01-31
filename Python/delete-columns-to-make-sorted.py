# Time:  O(n * l)
# Space: O(1)

# 944
# We are given an array A of N lowercase letter strings, all of the same length.
#
# Now, we may choose any set of deletion indices, and for each string, we delete all the characters in those indices.
#
# For example, if we have an array A = ["abcdef","uvwxyz"] and deletion indices {0, 2, 3}, then the final array after
# deletions is ["bef", "vyz"], and the remaining columns of A are ["b","v"], ["e","y"], and ["f","z"].
#
# Suppose we chose a set of deletion indices D such that after deletions, each remaining column in A is in non-decreasing sorted order.
#
# Return the minimum possible value of D.length.
#
#
# Example 1:
# Input: ["cba","daf","ghi"]
# Output: 1
# Explanation:
# After choosing D = {1}, each column ["c","d","g"] and ["a","f","i"] are in non-decreasing sorted order.
#
# Example 2:
# Input: ["a","b"]
# Output: 0
# Explanation: D = {}
#
# Example 3:
# Input: ["zyx","wvu","tsr"]
# Output: 3
# Explanation: D = {0, 1, 2}
#
# Note:
# 1 <= A.length <= 100
# 1 <= A[i].length <= 1000

class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        result = 0
        for c in xrange(len(A[0])):
            for r in xrange(1, len(A)):
                if A[r-1][c] > A[r][c]:
                    result += 1
                    break
        return result


# Time:  O(n * l)
# Space: O(n)
import itertools


class Solution2(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        result = 0
        for col in itertools.izip(*A):
            if any(col[i] > col[i+1] for i in xrange(len(col)-1)):
                result += 1
        return result
