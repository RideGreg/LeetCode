import heapq
class Solution(object):
    def smallestDistancePair(self, nums, k):
        h=[]
        d = {}
        for n in nums:
            if n not in d:
                d[n] = 0
            d[n] += 1
        for n in d:
            if d[n] > 1:
                cnt = ((d[n]*d[n]-1)/2)
                if cnt >= k:
                    return 0
                k -= cnt
#                h += [0] * 

        diff = 1
        while 1:
            for n in d:
                for m in d:
                    if abs(m-n) == diff and m<n:
                        cnt = d[n]*d[m]
                        if cnt >= k:
                            return diff
                        k -= cnt
            diff += 1

print Solution().smallestDistancePair([1,3,1], 3)

#        h=[]
#        for i in xrange(len(nums) - 1):
#            for j in xrange(i+1, len(nums)):
#                heapq.heappush(h, abs(nums[i]-nums[j]))
#        return heapq.nsmallest(k, h)[-1]
        h = []
        d = {}
        for n in nums:
            if n not in d:
                d[n] = 0
            d[n] += 1
        for n in d:
            if d[n] > 1:
                h += [0] * ((d[n]*d[n]-1)/2)
                if len(h) >= k:
                    return 0

        for n in d:
            for m in d:
                if m < n:
                    h += [abs(m-n)] * (d[n]*d[m])

        return heapq.nsmallest(k, h)[-1]