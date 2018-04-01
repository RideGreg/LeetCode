class Solution(object):
    def numSubarrayBoundedMax(self, A, L, R):
        dp = [0 for _ in xrange(len(A)+1)]
        start, end = 0, None
        for i in xrange(len(A)):
            if L<=A[i]<=R:
                end = i
                dp[i+1] = dp[i] + end - start + 1
            elif L>A[i]:
                dp[i+1] = dp[i] + end - start + 1 if end != None else dp[i]
            else:
                dp[i+1] = dp[i]
                start, end = i+1, None
        return dp[-1]

print Solution().numSubarrayBoundedMax([732,
                                        703,
                                        795,873,
                                        662,13,314,
                                        988,769,
                                        646,558,661,
                                        808,896,
                                        467,353,704,
                                        905,
                                        705,
                                        760,801,
                                        341,668,598,98,241],
658,
719)
print Solution().numSubarrayBoundedMax([73,55,36,5,55,14,9,7,72,52], 32, 69)