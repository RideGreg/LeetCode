class Solution(object):
    def dominantIndex(self, nums):
        m, mid, m2, mid2 = float("-inf"), -1, float("-inf"), -1
        for i, n in enumerate(nums):
            if n > m:
                mid, m = i, n
        for i, n in enumerate(nums):
            if n > m2 and i != mid:
                mid2, m2 = i, n
        print m, mid, m2, mid2
        return mid if m >= m2*2 else -1

#print Solution().dominantIndex([3, 6, 1, 0])
print Solution().dominantIndex([1,1,1,1])
