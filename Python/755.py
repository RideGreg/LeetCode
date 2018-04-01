class Solution(object):
    def pourWater(self, heights, V, K):
        while V > 0:
            cur = K
            for i in reversed(xrange(K)):
                if heights[i] > heights[cur]:
                    break
                elif heights[i] < heights[cur]:
                    cur = i
            if cur == K:
                for i in xrange(K+1, len(heights)):
                    if heights[i] > heights[cur]:
                        break
                    elif heights[i] < heights[cur]:
                        cur = i
            heights[cur] += 1
            V -= 1
        return heights

print Solution().pourWater([2,1,1,2,1,2,2], 4, 3)
print Solution().pourWater([1,2,3,4], 2, 2)
print Solution().pourWater([3,1,3], 5, 1)
print Solution().pourWater([1,2,3,4,3,2,1,2,3,4,3,2,1], 5, 2)