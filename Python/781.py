class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        if not answers: return 0
        import collections, math
        s = collections.Counter(answers)
        return sum(int((k+1)*math.ceil(v/float(k+1))) for k,v in s.iteritems())


print Solution().numRabbits([1,1,2])
print Solution().numRabbits([10,10,10])
print Solution().numRabbits([])
print Solution().numRabbits([2,2,2,2,2,2,2])
