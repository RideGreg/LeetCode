# Time:  O(n)
# Space: O(k)

# 992
# Given an array A of positive integers, call a (contiguous, not necessarily distinct) subarray
# of A good if the number of different integers in that subarray is exactly K.
#
# (For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)
#
# Return the number of good subarrays of A.

# Input: A = [1,2,1,2,3], K = 2
# Output: 7
# Explanation: Subarrays formed with exactly 2 different integers:
# [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].

import collections


class Solution(object):
    # sliding window solution. Find at most k, instead of exact k.
    # Maintain a counter for count of digits. Scan digits one by one,
    # add length of sliding window to total # of subarrays. Adjust window beginning as needed.
    def subarraysWithKDistinct(self, A, K): # USE THIS
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        def atMostK(A, K):
            count = collections.defaultdict(int)
            result, left = 0, 0
            for right in xrange(len(A)):
                count[A[right]] += 1
                while len(count) > K:
                    count[A[left]] -= 1
                    if count[A[left]] == 0:
                        count.pop(A[left])
                    left += 1
                result += right-left+1
            return result
        
        return atMostK(A, K) - atMostK(A, K-1)

    def subarraysWithKDistinct_lastPos(self, A, K): # 9700 ms. OrderedDict version is even slower (TLE)
        lookup = {}
        s, ans = -1, 0
        for endPos, v in enumerate(A):
            lookup[v] = endPos
            # 3rd new item: need to remove the oldest item and adjust window start point
            if len(lookup) > K:
                a = min(lookup, key=lookup.get)
                s = lookup[a]
                del lookup[a]
            if len(lookup) == K:
                firstEnd = min(lookup.values())
                ans += firstEnd - s
        return ans

    def subarraysWithKDistinct_lastPos2(self, A, K): # TLE: OrderedDict is very slow
        lookup = collections.OrderedDict()
        s, ans = -1, 0
        for i, x in enumerate(A):
            if x in lookup:
                del lookup[x]
            lookup[x] = i

            if len(lookup) > K:
                _, s = lookup.popitem(last=False)
            if len(lookup) == K:
                ans += lookup.values()[0] - s
        return ans

# Time:  O(n)
# Space: O(k)
# Solution: maintain two sliding windows. Each sliding window will be able to count
# how many different elements there are in the window, and add and remove elements
# in a queue-like fashion.

# Similar to Solution 1, get difference between k and k-1
class Window(object):
    def __init__(self):
        self.__count = collections.defaultdict(int)

    def add(self, x):
        self.__count[x] += 1

    def remove(self, x):
        self.__count[x] -= 1
        if self.__count[x] == 0:
            self.__count.pop(x)
            
    def size(self):
        return len(self.__count)


class Solution2(object):
    def subarraysWithKDistinct(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        window1, window2 = Window(), Window()
        result, left1, left2 = 0, 0, 0
        for i in A:
            window1.add(i)
            while window1.size() > K:
                window1.remove(A[left1])
                left1 += 1
            window2.add(i)
            while window2.size() >= K:
                window2.remove(A[left2])
                left2 += 1
            result += left2-left1
        return result


print(Solution().subarraysWithKDistinct([1,2,1,2,3], 2)) # 7
print(Solution().subarraysWithKDistinct([1,2,1,3,4], 3)) # 3
