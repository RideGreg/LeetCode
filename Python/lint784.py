class Solution:
    """
    @param dic: the n strings
    @param target: the target string
    @return: The ans
    """
    def theLongestCommonPrefix(self, dic, target):
        def getLen(a, b):
            i, j = 0, 0
            while i < len(a) and j < len(b):
                if a[i] == b[j]:
                    i += 1
                    j += 1
                else:
                    break
            return i
        ans = 0
        for w in dic:
            ans = max(ans, getLen(w, target))
        return ans

print Solution().theLongestCommonPrefix(["abcba","acc","abwsf"], 'abse')
print Solution().theLongestCommonPrefix(["aaa","bbb","aabb"], 'aaab')