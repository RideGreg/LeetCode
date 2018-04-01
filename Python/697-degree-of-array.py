class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos = {}
        maxTimes = 0
        maxNum = []
        minLen = float('inf')
        for i in xrange(len(nums)):
            if not nums[i] in pos:
                pos[nums[i]] = []
            pos[nums[i]].append(i)
            if len(pos[nums[i]]) > maxTimes:
                maxTimes = len(pos[nums[i]])
                maxNum = [nums[i]]
            elif len(pos[nums[i]]) == maxTimes:
                maxTimes = len(pos[nums[i]])
                maxNum.append(nums[i])
        for n in maxNum:
            curPos = pos[n]
            curLen = curPos[-1]-curPos[0]+1 if len(curPos) > 1 else 1
            minLen = min(minLen, curLen)
        return minLen

print Solution().findShortestSubArray([1, 2, 2, 3, 1])
print Solution().findShortestSubArray([1,2,2,3,1,4,2])