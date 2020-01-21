# Time:  O(n)
# Space: O(n)

# 1282 weekly contest 166 12/7/2019

# There are n people whose IDs go from 0 to n - 1 and each person belongs exactly to one group.
# Given the array groupSizes of length n telling the group size each person belongs to, return the groups there are
# and the people's IDs each group includes.
#
# You can return any solution in any order and the same applies for IDs. Also, it is guaranteed that there exists at least one solution.

import collections


class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        groups, result = collections.defaultdict(list), []
        for i, size in enumerate(groupSizes):
            groups[size].append(i)
            if len(groups[size]) == size:
                result.append(groups.pop(size))
        return result

print(Solution().groupThePeople([3,3,3,3,3,1,3])) # [[5],[0,1,2],[3,4,6]]
print(Solution().groupThePeople([2,1,3,3,3,2])) # [[1], [0,5], [2,3,4]]
