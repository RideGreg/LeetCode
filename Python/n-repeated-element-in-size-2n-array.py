# Time:  O(n)
# Space: O(1)

# 961
# In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.
# Return the element repeated N times.
# 4 <= A.length <= 10000

# Challenge: can you do it with O(1) space (not using hash table)?

class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # Put the same N elem in 2N positions, it has to appear at distance 1 or 2 away.
        for i in xrange(2, len(A)):
            if A[i-1] == A[i] or A[i-2] == A[i]:
                return A[i]
        return A[0]           # this is for the edge case [2,1,3,2]

print(Solution().repeatedNTimes([2,1,2,5,3,2])) # 2
