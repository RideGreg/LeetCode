# Time:  O(m * n)
# Space: O(n)

# 1257 biweekly contest 13 11/16/2019
#
# You are given some lists of regions where the first region of each list includes all other regions in that list.
#
# Naturally, if a region X contains another region Y then X is bigger than Y.
#
# Given two regions region1, region2, find out the smallest region that contains both of them.
#
# If you are given regions r1, r2 and r3 such that r1 includes r3, it is guaranteed there is no r2 such that r2 includes r3.
#
# It's guaranteed the smallest region exists.

from typing import List

class Solution(object):
    # USE THIS: same as the 2nd algorithm in lowest-common-ancestor-of-a-binary-tree.py
    # 1. preprocess: reverse index data
    # 2. build ancestor list for r1. Find r2's ancestors first shown in the r1's list.
    def findSmallestRegion(self, regions, region1, region2):
        """
        :type regions: List[List[str]]
        :type region1: str
        :type region2: str
        :rtype: str
        """
        parents = {r : region[0]
                   for region in regions
                   for r in region[1:]}
        ''' 
        parents = {}
        for region in regions:
            for r in region[1:]:
                parents[r] = region[0]
        '''
        lookup = {region1}
        while region1 in parents:
            region1 = parents[region1]
            lookup.add(region1)
        while region2 not in lookup:
            region2 = parents[region2]
        return region2

print(Solution().findSmallestRegion([["Earth","North America","South America"],
["North America","United States","Canada"],
["United States","New York","Boston"],
["Canada","Ontario","Quebec"],
["South America","Brazil"]], "Canada", "Quebec")) # "Canada"

print(Solution().findSmallestRegion([["Earth","North America","South America"],
["North America","United States","Canada"],
["United States","New York","Boston"],
["Canada","Ontario","Quebec"],
["South America","Brazil"]], "Quebec", "New York")) # "North America"