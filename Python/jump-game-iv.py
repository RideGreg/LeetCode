# Time:  O(n)
# Space: O(n)

# 1345 biweekly contest 19 2/8/2020

# Given an array of integers arr, you are initially positioned at the first index of the array.
#
# In one step you can jump from index i to index:
#   i + 1 where: i + 1 < arr.length.
#   i - 1 where: i - 1 >= 0.
#   j where: arr[i] == arr[j] and i != j.

# Return the minimum number of steps to reach the last index of the array.
# Notice that you can not jump outside of the array at any time.

import collections


class Solution(object):
    def minJumps(self, arr): # USE THIS: increment ans per BFS iteration
        """
        :type arr: List[int]
        :rtype: int
        """
        groups = collections.defaultdict(list)
        for k,v in enumerate(arr):
            groups[v].append(k)
        dp, ans, n = [0], 0, len(arr)
        seen = {0}
        while dp:
            ndp = []
            for x in dp:
                if x == n-1: return ans
                nei = set(groups[arr[x]] + [x-1, x+1])
                groups[arr[x]] = [] # this trim is VERY important to reduce complexity
                for y in nei:
                    if 0<=y<n and y not in seen:
                        ndp.append(y)
                        seen.add(y)
            ans += 1
            dp = ndp

    def minJumps_kamyu(self, arr):
        groups = collections.defaultdict(list)
        for i, x in enumerate(arr):
            groups[x].append(i)
        q = collections.deque([(0, 0)])
        lookup = {0}
        while q:
            pos, step = q.popleft()
            if pos == len(arr)-1:
                break
            neighbors = set(groups[arr[pos]] + [pos-1, pos+1])
            groups[arr[pos]] = []
            for p in neighbors:
                if p not in lookup and 0 <= p < len(arr):
                    lookup.add(p)
                    q.append((p, step+1))
        return step

print(Solution().minJumps([100,-23,-23,404,100,23,23,23,3,404])) # 3
print(Solution().minJumps([7])) # 0
print(Solution().minJumps([7,6,9,6,9,6,9,7])) # 1
print(Solution().minJumps([6,1,9])) # 2
print(Solution().minJumps([11,22,7,7,7,7,7,7,7,22,13])) # 3
print(Solution().minJumps([7]*1000 + [11])) # 2