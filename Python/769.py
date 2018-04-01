class Solution(object):
    def maxChunksToSorted(self, arr):
        #if len(arr) == 1: return 1
        end, ans = 0, 0
        for i, n in enumerate(arr):
            end = max(end, n)
            if i == end:
                ans += 1
                end = 0
        return ans

print Solution().maxChunksToSorted([4,3,2,1,0])
print Solution().maxChunksToSorted([1,0,2,3,4])
print Solution().maxChunksToSorted([2,0,1])#1
print Solution().maxChunksToSorted([1,0])
print Solution().maxChunksToSorted([0,1])