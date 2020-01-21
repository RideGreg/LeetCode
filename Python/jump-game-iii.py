# Time:  O(n)
# Space: O(n)

# 1306 Jump Game III

# Given an array of non-negative integers arr, you are initially positioned at start index of the array.
# When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.
#
# Notice that you can not jump outside of the array at any time.

# Constraints:
#
#     1 <= arr.length <= 5 * 10^4
#     0 <= arr[i] < arr.length
#     0 <= start < arr.length

import collections


class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        q, lookup = collections.deque([start]), set([start])
        while q:
            i = q.popleft()
            if not arr[i]:
                return True
            for j in [i-arr[i], i+arr[i]]:
                if 0 <= j < len(arr) and j not in lookup:
                    lookup.add(j)
                    q.append(j) 
        return False

print(Solution().canReach([4,2,3,0,3,1,2], 5)) # True
print(Solution().canReach([4,2,3,0,3,1,2], 0)) # True
print(Solution().canReach([3,0,2,1,2], 2)) # False