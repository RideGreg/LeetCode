# Time:  O(n + vlogv), v is the number of the level videos
# Space: O(w)

# 1311 weekly contest 170 1/4/2020

# There are n people, each person has a unique id between 0 and n-1. Given the arrays watchedVideos
# and friends, where watchedVideos[i] and friends[i] contain the list of watched videos and the list
# of friends respectively for the person with id = i.
#
# Level 1 of videos are all watched videos by your friends, level 2 of videos are all watched videos
# by the friends of your friends and so on. In general, the level k of videos are all watched videos
# by people with the shortest path equal to k with you. Given your id and the level of videos, return
# the list of videos ordered by their frequencies (increasing). For videos with the same frequency
# order them alphabetically from least to greatest.

# 2 <= n <= 100
# if friends[i] contains j, then friends[j] contains i

import collections
from typing import List

class Solution(object):
    def watchedVideosByFriends(self, watchedVideos, friends, id, level):
        """
        :type watchedVideos: List[List[str]]
        :type friends: List[List[int]]
        :type id: int
        :type level: int
        :rtype: List[str]
        """
        curr_level, lookup = set([id]), set([id])
        for _ in range(level):
            curr_level = set(j for i in curr_level for j in friends[i] if j not in lookup)
            lookup |= curr_level
        count = collections.Counter([v for i in curr_level for v in watchedVideos[i]])
        return sorted(count.keys(), key=lambda x: (count[x], x))

    def watchedVideosByFriends_ming(self, watchedVideos:List[List[str]], friends:List[List[int]], id: int,level: int) ->List[str]:
        import collections
        f, mask = set([id]), 0 | 1<<id
        while level:
            nf = set()
            for i in f:
                for j in friends[i]:
                    if mask & (1<<j) == 0:
                        nf.add(j)
                        mask |= 1<<j
            f = nf
            level -= 1
        ans = collections.defaultdict(int)
        for i in f:
            for video in watchedVideos[i]:
                ans[video] += 1

        return sorted(ans, key=lambda x: (ans[x], x))


print(Solution().watchedVideosByFriends([["A","B"],["C", "B"],["C","B"],["D"]], [[1,2],[0,3],[0,3],[1,2]], 0, 1))
print(Solution().watchedVideosByFriends([["A","B"],["C"],["B","C"],["D"]], [[1,2],[0,3],[0,3],[1,2]], 0, 2))
