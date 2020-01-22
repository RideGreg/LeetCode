# Time:  O(nlogn)
# Space: O(n)

# 1296 weekly contest 168 12/21/2019

# Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into sets of k consecutive numbers
# Return True if its possible otherwise return False.

# Constraints:
#
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^9
# 1 <= k <= nums.length

import collections
from typing import List


class Solution(object):
    def isPossibleDivide_kamyu(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        count = collections.Counter(nums)
        for num in sorted(count.keys()):
            c = count[num]
            if not c:
                continue
            for i in xrange(num, num+k):
                if count[i] < c:
                    return False
                count[i] -= c
        return True

    def isPossibleDivide(self, nums: List[int], k: int) -> bool: # USE THIS
        N = len(nums)
        if N%k: return False
        cnt = collections.Counter(nums)
        ks = sorted(cnt.keys())
        i = 0
        while N:
            while i < len(ks) and cnt[ks[i]] <= 0:
                i += 1
            ntime = cnt[ks[i]]
            for num in range(ks[i], ks[i]+k):
                if cnt[num] < ntime:
                    return False
                cnt[num] -= ntime
            N -= ntime * k
        return True

    # con: reduce count 1 at a time, not efficient
    def isPossibleDivide_ming(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        if N%k: return False
        cnt = collections.Counter(nums)
        ks = sorted(cnt.keys())
        i = 0
        for _ in range(N//k):
            while i < len(ks) and cnt[ks[i]] <= 0:
                i += 1
            for num in range(ks[i], ks[i]+k):
                if cnt[num] <= 0:
                    return False
                cnt[num] -= 1
        return True

    def isPossibleDivide_506140166(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        if n%k:
            return False
        cnt=collections.Counter(nums)
        st=min(cnt)
        while len(cnt)>0:
            ntime=cnt[st]
            for num in range(st,st+k):
                if cnt[num]<ntime:
                    return False
                elif cnt[num]==ntime:
                    cnt.pop(num)
                else:
                    cnt[num]-=ntime
            if cnt:
                st=min(cnt)
        return True

print(Solution().isPossibleDivide([1,2,3,3,4,4,5,6], 4)) # True
print(Solution().isPossibleDivide([3,2,1,2,3,4,3,4,5,9,10,11], 3)) # True
print(Solution().isPossibleDivide([3,3,2,2,1,1], 3)) # True
print(Solution().isPossibleDivide([1,2,3,4], 3)) # False
