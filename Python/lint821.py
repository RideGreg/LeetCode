class Solution:
    """
    @param seqA: The seqA
    @param seqB: The seqB
    @return: The answer
    """
    def timeIntersection(self, seqA, seqB):
        def overlap(p1, p2):
            return p2[0] <= p1[0] < p2[1] or p1[0] <= p2[0] < p1[1]
        ans = []
        for p1 in seqA:
            for p2 in seqB:
                if overlap(p1, p2):
                    ans.append([max(p1[0], p2[0]), min(p1[1], p2[1])])
        return ans

print Solution().timeIntersection([[1,2],[5,100]], [[1,6]])
print Solution().timeIntersection([[1,2],[10,15]], [[3,5], [7,9]])