class Solution(object):
    def anagramMappings(self, A, B):
        mapping, ans = {}, []
        for i, n in enumerate(B):
            mapping[n] = i
        for n in A:
            ans.append(mapping[n])
        return ans

print Solution().anagramMappings([12, 28, 46, 32, 50], [50, 12, 32, 46, 28])
