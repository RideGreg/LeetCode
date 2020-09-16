# Time:  O(m * n)
# Space: O(m)

# 1424
# Given a list of lists of integers, nums, return all elements of nums
# in diagonal order as shown in the below images.

# 1 <= nums.length <= 10^5
# 1 <= nums[i].length <= 10^5
# 1 <= nums[i][j] <= 10^9
# There at most 10^5 elements in nums.

import itertools
import collections


class Solution(object):
    # Time:  O(m * n), Space: O(m * n)
    def findDiagonalOrder(self, nums): # USE THIS: work for 2d array with empty list
        diag = collections.defaultdict(list)
        for i in reversed(range(len(nums))):
            for j in range(len(nums[i])):
                diag[i+j].append(nums[i][j])
        return [x for k in sorted(diag) for x in diag[k]]
        '''
        res = []
        for idx in sorted(diag):
            res.extend(diag[idx])
        return res
        '''

    # similar to findDiagonalOrder: Time:  O(m * n), Space: O(m * n). Suitable to traverse a
    # full matrix, trouble to traverse non-full matrix as need to add multiple empty arrays.
    def findDiagonalOrder2(self, nums):
        result = []
        for r, row in enumerate(nums):
            for c, num in enumerate(row):
                if len(result) <= r+c:
                    result.extend([[] for _ in range(r+c-len(result)+1)])
                result[r+c].append(num)
        return [num for row in result for num in reversed(row)]


    # Level order traverse: treat each diagonal as a queue. each queue stores coordinates.
    # Use current queue to populate next queue.
    # Time:  O(m * n), Space: O(m)
    def findDiagonalOrder3(self, nums): # not working for matrix with empty list, connection broken.
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        result, m, n = [], len(nums), max(map(len, nums))
        dq = collections.deque()
        for i in range(m+n-1):
            new_dq = collections.deque()
            if i < len(nums):
                dq.appendleft((i, 0))
            for r, c in dq:
                result.append(nums[r][c])
                if c+1 < len(nums[r]):
                    new_dq.append((r, c+1))
            dq = new_dq
        return result


    # TLE Time O(m * (m+n-1)
    def findDiagonalOrder4(self, nums):
        m = len(nums)
        n = max(len(nums[i]) for i in range(m))
        ans = []
        for k in range(m+n-1):
            for i in reversed(range(m)):
                j = k - i
                if 0<=j<len(nums[i]):
                    ans.append(nums[i][j])
        return ans


print(Solution().findDiagonalOrder([
[1,2,3,4,5],
[6,7],
[8],
[9,10,11],
[12,13,14,15,16]
])) # [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]

print(Solution().findDiagonalOrder([
[1,2,3],
[4],
[5,6,7],
[8],
[9,10,11]
])) # [1,4,2,5,3,8,6,9,7,10,11]

print(Solution().findDiagonalOrder([
[1],
[],
[],
[],
[12,13,14,15,16]
])) # [1,12,13,14,15,16]