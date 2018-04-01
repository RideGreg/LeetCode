class Solution:
    """
    @param: : string A to be repeated
    @param: : string B
    @return: the minimum number of times A has to be repeated
    """

    def repeatedString(self, A, B):
        if not A:
            return 1 if not B else -1
        import math
        ans = int(math.ceil(len(B)*1.0/len(A)))
        AA = A * ans
        if B in AA:
            return ans
        AA += A
        if B in AA:
            return ans+1
        return -1

print Solution().repeatedString('abcd','cdabcdab')
print Solution().repeatedString('abcd','cdab')
print Solution().repeatedString('abcd','c')
print Solution().repeatedString('abcd','cdabcdabx')
