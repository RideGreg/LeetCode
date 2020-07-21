# Time:  O(nlogn)
# Space: O(n)

# 1086
# Given a list of scores of different students, return the average score of each student's
# top five scores in the order of each student's id.
#
# Each entry items[i] has items[i][0] the student's id, and items[i][1] the student's score.
# The average score is calculated using integer division.

import collections
import heapq


class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        min_heaps = collections.defaultdict(list)
        for i, val in items:
            heapq.heappush(min_heaps[i], val)
            if len(min_heaps[i]) > 5:
                heapq.heappop(min_heaps[i])
        return [[i, sum(min_heaps[i]) // len(min_heaps[i])] for i in sorted(min_heaps)]

print(Solution().highFive([
    [1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]
])) # [[1,87],[2,88]]
