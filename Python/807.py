class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        rm = [max(r) for r in grid]
        cm = [max(c) for c in zip(*grid)]
        #print rm, cm
        ans = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                ans += min(rm[i], cm[j]) - grid[i][j]
        return ans

print Solution().maxIncreaseKeepingSkyline([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]])