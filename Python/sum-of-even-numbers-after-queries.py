# Time:  O(n + q)
# Space: O(1)

# 985
# We have an array A of integers, and an array queries of queries.
#
# For the i-th query val = queries[i][0], index = queries[i][1], we add val to A[index].  Then, the answer
# to the i-th query is the sum of the even values of A.
#
# (Here, the given index = queries[i][1] is a 0-based index, and each query permanently modifies the array A.)
#
# Return the answer to all queries.  Your answer array should have answer[i] as the answer to the i-th query.

# Input: A = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
# Output: [8,6,2,4]

class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        total = sum(v for v in A if v % 2 == 0)
        
        result = []
        for v, i in queries:
            if A[i] % 2 == 0:
                total -= A[i]
            A[i] += v
            if A[i] % 2 == 0:
                total += A[i]
            result.append(total)
        return result
