# Time:  O(logn)
# Space: O(1)
# 275
# Follow up for H-Index: What if the citations array is sorted in
# ascending order? Could you optimize your algorithm?
#
# Hint:
#
# Expected runtime complexity is in O(log n) and the input is sorted.
#

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        N = len(citations)
        l, r = 0, N
        while l < r:
            m = (r-l)//2 + l
            if citations[m] >= N-m:
                r = m
            else:
                l = m + 1
        return N - l

print(Solution().hIndex([0,1,3,5,6])) # 3