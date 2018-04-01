class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        ans, curmax, i = 0, float("-inf"), 0
        while i < len(arr):
            curmax = max(curmax, arr[i])
            newmax = curmax
            valid = True
            for j in xrange(i + 1, len(arr)):
                newmax = max(newmax, arr[j])
                if arr[j] < curmax:
                    valid = False
                    break
            if valid:
                ans += 1
                curmax = float("-inf")
                i += 1
            else:
                curmax = newmax
                i = j
        return ans
'''
        ans, curmax, i = 0, float("-inf"), 0
        while i < len(arr):
            curmax = max(curmax, arr[i])
            valid = True
            for j in xrange(i + 1, len(arr)):
                if arr[j] < curmax:
                    valid = False
                    break
            if valid:
                ans += 1
                curmax = float("-inf")

            i += 1
        return ans
'''
print Solution().maxChunksToSorted([4,2,2,1,1])