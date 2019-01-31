# Time:  O(n * l), n is length of A, l is the length of each word in A.
# Space: O(n)

# 955
# We are given an array A of N lowercase letter strings, all of the same length.
#
# Now, we may choose any set of deletion indices, and for each string, we delete all the characters in those indices.
#
# For example, if we have an array A = ["abcdef","uvwxyz"] and deletion indices {0, 2, 3}, then the final array after
# deletions is ["bef","vyz"].
#
# Suppose we chose a set of deletion indices D such that after deletions, the final array has its elements in
# lexicographic order (A[0] <= A[1] <= A[2] ... <= A[A.length - 1]).
#
# Return the minimum possible value of D.length.
#
# Example 1:
# Input: ["ca","bb","ac"]
# Output: 1
# Explanation: After deleting the first column, A = ["a", "b", "c"].
# Now A is in lexicographic order (ie. A[0] <= A[1] <= A[2]).

# Example 2:
# Input: ["xc","yb","za"]
# Output: 0
# Explanation: A is already in lexicographic order, so we don't need to delete anything.

# Example 3:
# Input: ["zyx","wvu","tsr"]
# Output: 3
# Explanation: We have to delete every column.

class Solution(object):
    def minDeletionSize(self, A): # USE THIS
        """
        :type A: List[str]
        :rtype: int
        """
        unsorted, ans = range(len(A)-1), 0
        for j in xrange(len(A[0])):
            nextset = []
            for i in unsorted:
                if A[i][j] > A[i+1][j]: # the column j must be deleted
                    ans += 1
                    break
                if A[i][j] == A[i+1][j]: # the row i and i+1 still need comparison
                    nextset.append(i)
            else:
                if not nextset: # all elements are sorted by previous kept columns
                    return ans
                unsorted = nextset
        return ans

    def minDeletionSize_kamyu(self, A): # using set
        result = 0
        unsorted = set(range(len(A)-1))
        for j in xrange(len(A[0])):
            if any(A[i][j] > A[i+1][j] for i in unsorted):
                result += 1
            else:
                unsorted -= set(i for i in unsorted if A[i][j] < A[i+1][j])
        return result


# Time:  O(n * m)
# Space: O(n)
class Solution2(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        result = 0
        is_sorted = [False]*(len(A)-1)
        for j in xrange(len(A[0])):
            tmp = is_sorted[:]
            for i in xrange(len(A)-1):
                if A[i][j] > A[i+1][j] and tmp[i] == False:
                    result += 1
                    break
                if A[i][j] < A[i+1][j]:
                    tmp[i] = True
            else:
                is_sorted = tmp
        return result
