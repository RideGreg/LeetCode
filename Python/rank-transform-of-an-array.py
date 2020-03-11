# Time:  O(nlogn)
# Space: O(n)

# 1331 biweekly contest 18 1/25/2020

# Given an array of integers arr, replace each element with its rank.
#
# The rank represents how large the element is. The rank has the following rules:
#
# Rank is an integer starting from 1.
# The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
# Rank should be as small as possible.

class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        A = sorted(set(arr))
        rank = {v: i + 1 for i, v in enumerate(A)}
        return [rank[a] for a in arr]

    def arrayRankTransform_kamyu(self, arr):
        return map({x: i+1 for i, x in enumerate(sorted(set(arr)))}.get, arr)

print(Solution().arrayRankTransform([40,10,20,30])) # [4,1,2,3]
print(Solution().arrayRankTransform([100,100,100])) # [1,1,1]
print(Solution().arrayRankTransform([37,12,28,9,100,56,80,5,12])) # [5,3,4,2,8,6,7,1,3]
