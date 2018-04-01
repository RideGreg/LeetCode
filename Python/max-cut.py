class Solution:
    # @param rods, a list of integers
    # @param k, integer
    # @return an integer
    def maxCut(self, rods, k):
        longest = max(rods)
        if k == 1: return longest

        left, right, ans = 1, longest, 0
        while left <= right:
            mid = (right-left) / 2 + left
            counts = sum([x/mid for x in rods])
            if counts >= k:
                ans = mid
                left = mid + 1
            else:
                right = mid -1
        return ans

    def maxCut2(self, rods, k):
        def dfs(rods, target, start, tmp, ans):
            if target == 0:
                localMin = min([x/y for x, y in zip(rods, tmp)])
                if localMin > ans[0]:
                    ans[0] = localMin

            if len(tmp) < len(rods ):
                for i in reversed(xrange(1, start+1)): #{k,0,0...}, {k-1, 1, 0, 0...} ...
                    if i > target:
                        continue
                    tmp.append(i)
                    dfs(rods, target - i, i, tmp, ans)
                    tmp.pop()

        if k == 1: return max(rods)
        if k == 0: return 0

        ans = [0]
        dfs(sorted(rods, reverse=True), k, k, [], ans)
        return ans[0]

import time
if __name__ == "__main__":
    start = time.time()
    print Solution().maxCut([80, 101], 3) #50
    print Solution().maxCut([80, 101], 182) #0
    print Solution().maxCut([10, 101], 3) #33
    print Solution().maxCut([10, 80, 101], 3) #50
    print Solution().maxCut([10, 80, 101], 19) #10
    print Solution().maxCut([10, 80, 101], 20) #9
    print Solution().maxCut([10, 80, 98], 20) #8
    print Solution().maxCut([10, 80, 98], 188) #1
    print Solution().maxCut([10, 80, 98, 51], 239) #1
    print Solution().maxCut([10, 80, 98, 51], 240) #0
    print Solution().maxCut([10, 80, 98, 51], 1) #98
    print Solution().maxCut([10, 20, 30, 40, 50], 3) #30
    print Solution().maxCut([10, 20, 30, 40, 100], 3) #40
    print Solution().maxCut([10, 20, 30, 40, 210], 3) #70
    print time.time()-start, ' seconds'
