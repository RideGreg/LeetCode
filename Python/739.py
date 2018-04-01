class Solution(object):
    def dailyTemperatures(self, temperatures):
        '''1. init all 0, then can set; 2. only store index, not need value'''
        length = len(temperatures)
        ans, stk = [0] * length, []
        for i in xrange(length):
            while stk and temperatures[stk[-1]] < temperatures[i]:
                ans[stk[-1]] = i - stk[-1]
                stk.pop()
            stk.append(i)
        return ans

''' TLE
        ans = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            for j, tt in enumerate(temperatures[i+1:], i+1):
                if tt > t:
                    ans[i]=j-i
                    break
        return ans
'''

print Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])

